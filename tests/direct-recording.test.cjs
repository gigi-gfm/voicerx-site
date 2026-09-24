const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const html=fs.readFileSync('deploy/voicerx-tess/public/index.html','utf8');
const source=[...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)].map(x=>x[1]).join('\n');
function setup({micError,requestError,saveError,pollError,emptySpeech,formatError,formatMessage,apiUrl}={}) {
  const elements=new Map(), storage=new Map([['vrx_worker_url',apiUrl||'https://example.test'],['vrx_token','fictional-test-token']]);
  const element=id=>{if(!elements.has(id))elements.set(id,{value:'',style:{},dataset:{},textContent:'',classList:{add(){},remove(){},toggle(){}},addEventListener(){},setAttribute(){},removeAttribute(){},appendChild(){},remove(){},click(){},querySelectorAll(){return[];}});return elements.get(id);};
  element('patientName').value='Fictional Test';element('noteLang').value='en';element('pronounsSelect').value='she/her';
  const track={handlers:{},addEventListener(n,fn){this.handlers[n]=fn;},stop(){this.stopped=true;}};
  class Recorder {
    static isTypeSupported(type){return type==='audio/mp4';}
    constructor(stream,options){this.mimeType=options?.mimeType||'audio/webm';this.handlers={};this.state='inactive';Recorder.last=this;}
    addEventListener(n,fn){this.handlers[n]=fn;}
    start(){this.state='recording';}
    stop(){this.state='inactive';this.handlers.dataavailable({data:new Blob(['fictional audio'],{type:this.mimeType})});this.done=this.handlers.stop();}
  }
  const calls=[],saved=[],deleted=[];
  const context=vm.createContext({console:{log(){},error(){},warn(){}},Blob,URL,URLSearchParams,AbortController,TextEncoder,crypto:require('node:crypto').webcrypto,MediaRecorder:Recorder,
    localStorage:{getItem:k=>storage.get(k)||null,setItem:(k,v)=>{if(saveError&&k!=='vrx_token')throw Error('Storage full');storage.set(k,v);},removeItem:k=>storage.delete(k)},
    document:{getElementById:element,querySelector:()=>element('selected'),querySelectorAll:()=>[],addEventListener(){},createElement:()=>element('created'),body:{appendChild(){}},visibilityState:'visible'},
    window:{isSecureContext:true,addEventListener(){}},location:{hash:''},navigator:{mediaDevices:{getUserMedia:async()=>{if(micError)throw Object.assign(Error(),{name:micError});return{getAudioTracks:()=>[track],getTracks:()=>[track]};}}},
    setInterval:()=>1,clearInterval(){},setTimeout:(fn,ms)=>ms===2000?setImmediate(fn):1,clearTimeout(){},confirm:()=>true,
    fetch:async(url,options)=>{calls.push(url);if(requestError&&url.includes('/transcribe'))throw Error('Network unavailable');if(pollError&&url.includes('/poll/'))throw Error('Network unavailable');return {ok:!(formatError&&url.includes('/format')),status:formatError?500:200,json:async()=>url.includes('/transcribe')?{id:'fictional-job'}:url.includes('/poll/')?{status:'completed',text:emptySpeech?'':'Fictional encounter transcript.'}:url.includes('/format')&&formatMessage?{error:formatMessage}:url.includes('/format')?{note:'Subjective: Fictional encounter.\nAssessment: Test only.'}:{}};},
    testSave:async(id,blob,meta)=>{saved.push({id,blob,meta});return true;},testDelete:async id=>deleted.push(id)
  });
  vm.runInContext(source,context);
  vm.runInContext('audioSave=testSave;audioDelete=testDelete;',context);
  return {context,element,storage,calls,saved,deleted,track,Recorder,run:code=>vm.runInContext(code,context)};
}
test('inline application JavaScript parses',()=>new vm.Script(source));
test('direct Record → Stop retains final chunk, transcribes and formats automatically',async()=>{
  const t=setup();await t.run('startRecording()');assert.equal(t.run('isRecording'),true);assert.equal(t.Recorder.last.mimeType,'audio/mp4');
  t.run('stopRecording()');await t.Recorder.last.done;
  assert.ok(t.saved[0].blob.size);assert.equal(t.run('currentTranscript'),'Fictional encounter transcript.');assert.match(t.run('currentSOAP'),/Fictional/);
  assert.equal(t.calls.filter(x=>x.includes('/transcribe')).length,1);assert.ok(t.calls.some(x=>x.includes('/format')));assert.equal(t.deleted.length,1);assert.ok(t.track.stopped);
});
for(const [name,message] of [['NotAllowedError','permission'],['NotFoundError','No microphone'],['NotReadableError','could not start']])test(name+' gets actionable startup error',async()=>{
  const t=setup({micError:name});await t.run('startRecording()');assert.match(t.element('statusText').textContent,new RegExp(message));assert.equal(t.run('isRecording'),false);assert.equal(t.element('recordBtn').disabled,false);
});
test('network failure retains audio and unlocks retry without changing patient',async()=>{
  const t=setup({requestError:true});await t.run('startRecording()');t.run('stopRecording()');await t.Recorder.last.done;
  assert.equal(t.run('hasUntranscribedAudio'),true);assert.equal(t.deleted.length,0);assert.equal(t.element('recordingRecovery').hidden,false);assert.equal(t.element('retryAudioBtn').disabled,false);assert.equal(t.element('patientName').disabled,true);
});
test('poll retry reuses transcript ID instead of uploading twice',async()=>{
  const t=setup({pollError:true});await t.run('startRecording()');t.run('stopRecording()');await t.Recorder.last.done;await t.run('processAudio()');
  assert.equal(t.calls.filter(x=>x.includes('/transcribe')).length,1);assert.equal(t.deleted.length,0);assert.equal(t.saved.at(-1).meta.transcriptId,'fictional-job');
});
test('microphone interruption saves final audio and waits for review',async()=>{
  const t=setup();await t.run('startRecording()');t.track.handlers.ended();await t.Recorder.last.done;
  assert.equal(t.run('hasUntranscribedAudio'),true);assert.ok(t.saved.at(-1).blob.size);assert.equal(t.calls.length,0);assert.match(t.element('statusText').textContent,/disconnected/);
});
test('failed transcript persistence never deletes recovery audio',async()=>{
  const t=setup({saveError:true});await t.run('startRecording()');t.run('stopRecording()');await t.Recorder.last.done;
  assert.equal(t.deleted.length,0);assert.equal(t.run('hasUntranscribedAudio'),true);
});
test('empty speech keeps audio for playback and retry',async()=>{
  const t=setup({emptySpeech:true});await t.run('startRecording()');t.run('stopRecording()');await t.Recorder.last.done;
  assert.equal(t.deleted.length,0);assert.equal(t.run('pendingTranscriptId'),null);assert.match(t.element('statusText').textContent,/No speech/);
});
test('note service failure preserves transcript and offers Format retry',async()=>{
  const t=setup({formatError:true});await t.run('startRecording()');t.run('stopRecording()');await t.Recorder.last.done;
  assert.equal(t.run('currentTranscript'),'Fictional encounter transcript.');assert.equal(t.run('currentSOAP'),'');assert.match(t.element('statusText').textContent,/Format to retry/);
});
test('declining recovery leaves saved audio intact',async()=>{
  const t=setup();t.context.confirm=()=>false;t.context.testList=async()=>[{id:'old',blob:new Blob(['test']),savedAt:1}];t.run('audioListAll=testList');await t.run('checkForRecoverableAudio()');assert.equal(t.deleted.length,0);
});

test('formatting displays the server error and preserves the transcript',async()=>{
  const message='VoiceRx cannot format notes because the Anthropic API credit balance is too low.';
  const t=setup({formatError:true,formatMessage:message});
  t.run("currentTranscript='Fictional brief encounter.'");await t.run('formatSOAP()');
  assert.ok(t.element('statusText').textContent.includes(message));
  assert.equal(t.run('currentTranscript'),'Fictional brief encounter.');
  assert.equal(t.element('formatBtn').disabled,false);
});
test('formatting normalizes a saved API URL with a trailing slash',async()=>{
  const t=setup({apiUrl:'https://example.test/'});
  t.run("currentTranscript='Fictional brief encounter.'");await t.run('formatSOAP()');
  assert.ok(t.calls.some(url=>url.startsWith('https://example.test/format?')));
  assert.ok(t.calls.every(url=>!url.includes('test//')));
});

test('provider setup keeps credentials local and clears them on close',async()=>{
  const t=setup();
  t.element('newprov_id').value='test';t.element('newprov_display_name').value='Test Provider';
  const requests=[];
  t.context.fetch=async(url)=>{requests.push(url);return {ok:true,json:async()=>({display_name:'Test Provider',token:'fictional-new-token'})};};
  await t.run('submitAddProvider()');
  assert.deepEqual(requests,['https://example.test/admin/providers']);
  assert.equal(t.element('newprov_result_token').textContent,'fictional-new-token');
  assert.equal(t.element('newprov_result').style.display,'block');
  assert.doesNotMatch(html,/qrserver|autoLoginUrl|newprov_result_qr/);
  t.run('closeAddProvider()');
  assert.equal(t.element('newprov_result_token').textContent,'');
});


test('finished encounter autosaves transcript AND SOAP without Save Note',async()=>{
  const t=setup(), writes=[];const original=t.context.fetch;
  t.context.fetch=async(url,options)=>{if(url.endsWith('/notes'))writes.push(JSON.parse(options.body));return original(url,options);};
  await t.run('startRecording()');t.run('stopRecording()');await t.Recorder.last.done;
  assert.ok(writes.some(n=>n.transcript && !n.soap));
  assert.match(writes.at(-1).soap,/Fictional/);
  assert.match(t.element('cloudSaveStatus').textContent,/Saved to cloud/);
});
test('failed cloud save stays pending and never announces success',async()=>{
  const t=setup();t.context.fetch=async()=>({ok:false,status:401,json:async()=>({})});
  t.run("currentTranscript='Fictional offline note';currentNoteId='offline'");
  await t.run('saveNote()');
  assert.match(t.element('toast').textContent,/waiting to sync/);
  assert.match(t.element('cloudSaveStatus').textContent,/Saved on this device/);
  const c=await t.run('noteSyncContext()');
  assert.equal(JSON.parse(t.storage.get(c.key)).offline.note.transcript,'Fictional offline note');
  t.run("showTranscript(currentTranscript)");
  assert.doesNotMatch(t.element('saveIndicator').textContent,/Saved to cloud/);
});
test('pending notes survive reload and an empty cloud list, then retry automatically',async()=>{
  const t=setup();t.context.fetch=async()=>{throw Error('offline');};
  t.run("currentTranscript='Fictional pending';currentNoteId='pending'");await t.run('autoSaveTranscript()');
  const restored=setup();for(const [k,v] of t.storage)restored.storage.set(k,v);
  restored.context.fetch=async()=>({ok:true,json:async()=>({notes:[]})});
  await restored.run('renderNotesList()');
  assert.equal(restored.run('notesCache[0].transcript'),'Fictional pending');
  const writes=[];restored.context.fetch=async(url,opts)=>{writes.push(JSON.parse(opts.body));return{ok:true,json:async()=>({})};};
  await restored.run('resumeNoteSync()');
  assert.equal(writes[0].transcript,'Fictional pending');
  const c=await restored.run('noteSyncContext()');assert.deepEqual(JSON.parse(restored.storage.get(c.key)),{});
});
test('edits during an in-flight save are sent in order and keep newest SOAP',async()=>{
  const t=setup(), writes=[];let release;
  t.context.fetch=async(url,options)=>{writes.push(JSON.parse(options.body));if(writes.length===1)await new Promise(r=>release=r);return{ok:true,json:async()=>({})};};
  t.run("currentTranscript='Fictional';currentNoteId='serial'");const first=t.run('autoSaveTranscript()');
  while(!release)await new Promise(setImmediate);
  const second=t.run("currentSOAP='Latest SOAP';autoSaveTranscript()");
  const c=await t.run('noteSyncContext()');
  while(!JSON.parse(t.storage.get(c.key)).serial.note.soap)await new Promise(setImmediate);
  release();await Promise.all([first,second]);
  assert.equal(writes.length,2);assert.equal(writes[1].soap,'Latest SOAP');
  assert.deepEqual(JSON.parse(t.storage.get(c.key)),{});
});
test('changing accounts never retries old pending notes with new credentials',async()=>{
  const t=setup();t.context.fetch=async()=>{throw Error('offline');};
  t.run("currentTranscript='Provider A fictional note';currentNoteId='private'");await t.run('autoSaveTranscript()');
  const old=await t.run('noteSyncContext()');t.storage.set('vrx_token','different-fictional-provider');
  let writes=0;t.context.fetch=async()=>{writes++;return {ok:true,json:async()=>({})};};
  await t.run('resumeNoteSync()');assert.equal(writes,0);assert.ok(JSON.parse(t.storage.get(old.key)).private);
});
test('formatting an existing transcript with no note id still autosaves SOAP',async()=>{
  const t=setup(), writes=[];const original=t.context.fetch;
  t.context.fetch=async(url,options)=>{if(url.endsWith('/notes'))writes.push(JSON.parse(options.body));return original(url,options);};
  t.run("currentTranscript='Fictional encounter'");await t.run('formatSOAP()');
  assert.ok(writes.at(-1).id);assert.match(writes.at(-1).soap,/Fictional/);
});
