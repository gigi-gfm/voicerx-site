# Garcia Family Medicine — SEO + Site Improvement Plan

Practice: Garcia Family Medicine (Direct Primary Care)
Site: https://garciafamilymedicine.care (WordPress)
Provider: Dr. Theresa "Tess" Garcia, MD, FAAFP, Dipl. ABOM
Location: 801 NW Saint Mary Dr, Suite 209, Blue Springs, MO 64014
Phone: (816) 330-7575

---

## 1. Executive summary — what to fix first

Highest impact, lowest effort (do this week):

1. **Pick one canonical domain.** Decide between `garciafamilymedicine.care` and `gfmdirectprimarycare.com`. 301-redirect the loser to the winner. Running both splits ranking signal and creates duplicate content.
2. **Kill duplicate home page.** `/home/` and `/` both rank — 301 `/home/` → `/`.
3. **Normalize URL structure.** Move orphan slugs into `/services/` and add trailing slashes consistently (see §3).
4. **Verify Cloudflare allows search engine crawlers.** The site returns 403 to non-browser user-agents. Confirm Googlebot, Bingbot, and Applebot are on the allowlist in Cloudflare → Security → Bots.
5. **Paste the JSON-LD schema in §5 into the homepage and provider page.** Massive local-pack and rich-result win.
6. **Rewrite titles + meta descriptions** for the 10 highest-traffic pages (§4).
7. **Claim and fully populate the Google Business Profile** with the exact NAP from §6, weekly posts, and photos.

Medium effort (this month):

8. Add the missing service/content pages in §7.
9. Add the FAQ section in §8 (with FAQPage schema) to the homepage and each major service page.
10. Add visible reviews/testimonials with `Review` schema (§5).
11. Visual refresh items in §9.

Ongoing:

12. Publish the blog topics in §10 on a 2× monthly cadence.

---

## 2. What's working — keep these

- **Strong unique value**: $99/mo DPC + board-certified obesity medicine + bilingual care is a niche with high commercial intent and weak local competition.
- **Personal differentiator**: direct text/call/email access to Dr. Garcia is repeated by patients in reviews — keep it front-and-center.
- **Diverse team angle** (Mexican American, Native American, Filipina American) is genuine and underserved in the Blue Springs market — lean in.
- **DABOM credential** is gold for "obesity medicine specialist near me" and GLP-1/Tirzepatide search intent.
- **Existing testimonials** are specific and emotional ("lost 65 pounds…", "no 5-minute visits…") — they should be on every landing page, not hidden.

---

## 3. Technical SEO + URL cleanup

### Canonical domain decision
Keep `garciafamilymedicine.care` as canonical (it already has the indexed pages and matches your branded search). 301 every URL on `gfmdirectprimarycare.com` to the matching path on `.care`.

### URL normalization (301 redirects to add in WordPress)
Use a redirect plugin (Redirection, or Rank Math's built-in redirect manager). One-to-one mappings:

| Old URL (kill) | New URL (canonical) |
|---|---|
| `/home/` | `/` |
| `/weight-management-services` | `/services/medical-weight-management/` |
| `/comprehensive-healthcare-services` | `/services/` |
| `/affordable-healthcare-memberships` | `/services/direct-primary-care/` |
| `/contact-us` | `/contact/` |
| `/meet-dr-tess-garcia` | `/about/` |
| `/meetthedoctor/` | `/about/` |
| `27special.garciafamilymedicine.care` | `/services/medical-weight-management/?ref=27special` (keep as a campaign landing page on main domain, not subdomain) |

Rule going forward: **every service lives under `/services/{slug}/`** with a trailing slash. Permalinks → Post name in WordPress settings.

### Other technical checklist
- [ ] Submit a fresh XML sitemap to Google Search Console (Yoast or Rank Math generates this automatically).
- [ ] Add `robots.txt` allowing crawlers; do **not** block `/wp-content/uploads/` (images need to be indexable).
- [ ] Enable HTTPS-only (you already are; just confirm HSTS).
- [ ] Compress images: install ShortPixel or Smush; convert hero images to WebP.
- [ ] Cloudflare → Speed → Optimization: enable Auto Minify (HTML/CSS/JS), Brotli, Early Hints.
- [ ] Mobile Core Web Vitals: lazy-load below-fold images, defer non-critical JS, preload the hero image and webfont.
- [ ] Add `<link rel="canonical">` on every page (Yoast/Rank Math does this).
- [ ] Add OpenGraph + Twitter Card meta on every page so shared links render with logo + image.
- [ ] 404 page: redirect to `/` with a helpful "looking for…" list of top services.

---

## 4. Title tags + meta descriptions (ready to paste into Yoast/Rank Math)

Target: 50–60 chars for titles, 140–155 for meta descriptions. Every title ends with `| Garcia Family Medicine` for brand reinforcement except the homepage.

### Homepage `/`
- **Title:** Direct Primary Care in Blue Springs, MO | Dr. Tess Garcia, MD
- **Meta:** Family medicine + obesity care for $99/mo. Unlimited visits, direct text access to Dr. Tess. Bilingual (Se Habla Español). Blue Springs, MO.

### `/about/` (Provider page)
- **Title:** Dr. Tess Garcia, MD, FAAFP, DABOM | Blue Springs Family Doctor
- **Meta:** Meet Dr. Theresa "Tess" Garcia — board-certified in Family Medicine and Obesity Medicine. 20+ years serving Blue Springs and Eastern Jackson County.

### `/services/direct-primary-care/`
- **Title:** Direct Primary Care $99/Month | Blue Springs, MO
- **Meta:** No copays. No insurance. Unlimited visits, same-day appointments, direct text access to Dr. Tess. Membership-based primary care in Blue Springs.

### `/services/medical-weight-management/`
- **Title:** Medical Weight Loss in Blue Springs MO | GLP-1, Tirzepatide
- **Meta:** Physician-supervised weight loss with a board-certified Obesity Medicine specialist. Tirzepatide, semaglutide, body comp analysis, biweekly coaching.

### `/services/mental-health-care-counseling/`
- **Title:** Mental Health Care in Primary Care | Blue Springs, MO
- **Meta:** Integrated mental health evaluation and medication management — because we treat the whole person. Blue Springs, MO.

### `/services/pelvic-health/` (EMSELLA)
- **Title:** EMSELLA Pelvic Floor Therapy in Blue Springs, MO
- **Meta:** Non-invasive, fully clothed 28-minute sessions for stress and urge incontinence. 95% of patients report life-changing improvement. Blue Springs, MO.

### `/services/dot-physicals/`
- **Title:** DOT Physicals & CDL Exams in Blue Springs, MO
- **Meta:** Same-week DOT physicals and CDL medical certifications by a certified medical examiner. Blue Springs, MO.

### `/services/wellness-coaching/`
- **Title:** Wellness Coaching: Nutrition & Lifestyle | Blue Springs, MO
- **Meta:** Personalized nutrition and lifestyle coaching from a board-certified Obesity Medicine physician. Blue Springs, MO.

### `/founding-members/`
- **Title:** Founding Member Pricing — Lock In $99/Month for Life
- **Meta:** Limited founding-member spots — lock in your DPC membership rate. Direct primary care with Dr. Tess Garcia in Blue Springs, MO.

### `/contact/`
- **Title:** Contact & Book Appointment | Garcia Family Medicine
- **Meta:** Book online, call (816) 330-7575, or text Dr. Tess directly. 801 NW Saint Mary Dr, Suite 209, Blue Springs, MO 64014.

---

## 5. Structured data (JSON-LD) — paste into `<head>` site-wide

WordPress: use the "Header and Footer Code" plugin or put in your theme's `header.php`. **Both** Yoast/Rank Math will add a basic Organization schema — these blocks add the medical-specific richness Google rewards.

### A. Homepage + every page — MedicalBusiness + Physician

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["MedicalBusiness", "MedicalClinic", "LocalBusiness"],
      "@id": "https://garciafamilymedicine.care/#clinic",
      "name": "Garcia Family Medicine",
      "alternateName": "Garcia Family Medicine — A Direct Primary Care Practice",
      "description": "Direct primary care, medical weight management, mental health, and pelvic health for families in Blue Springs, MO. $99/month membership, unlimited visits, direct access to Dr. Tess Garcia.",
      "url": "https://garciafamilymedicine.care/",
      "logo": "https://garciafamilymedicine.care/wp-content/uploads/logo.png",
      "image": "https://garciafamilymedicine.care/wp-content/uploads/clinic-front.jpg",
      "telephone": "+1-816-330-7575",
      "priceRange": "$$",
      "currenciesAccepted": "USD",
      "paymentAccepted": "Cash, Credit Card, ACH, HSA, FSA",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "801 NW Saint Mary Dr, Suite 209",
        "addressLocality": "Blue Springs",
        "addressRegion": "MO",
        "postalCode": "64014",
        "addressCountry": "US"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 39.0169,
        "longitude": -94.2816
      },
      "areaServed": [
        {"@type": "City", "name": "Blue Springs, MO"},
        {"@type": "City", "name": "Grain Valley, MO"},
        {"@type": "City", "name": "Independence, MO"},
        {"@type": "City", "name": "Lee's Summit, MO"},
        {"@type": "City", "name": "Oak Grove, MO"},
        {"@type": "City", "name": "Kansas City, MO"}
      ],
      "knowsLanguage": ["English", "Spanish"],
      "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "08:00", "closes": "17:00"}
      ],
      "medicalSpecialty": ["FamilyPractice", "PrimaryCare", "Obesity", "MentalHealth"],
      "availableService": [
        {"@type": "MedicalProcedure", "name": "Direct Primary Care Membership", "url": "https://garciafamilymedicine.care/services/direct-primary-care/"},
        {"@type": "MedicalProcedure", "name": "Medical Weight Management (GLP-1, Tirzepatide)", "url": "https://garciafamilymedicine.care/services/medical-weight-management/"},
        {"@type": "MedicalProcedure", "name": "Mental Health Care & Counseling", "url": "https://garciafamilymedicine.care/services/mental-health-care-counseling/"},
        {"@type": "MedicalProcedure", "name": "EMSELLA Pelvic Floor Therapy", "url": "https://garciafamilymedicine.care/services/pelvic-health/"},
        {"@type": "MedicalProcedure", "name": "DOT Physicals & CDL Exams", "url": "https://garciafamilymedicine.care/services/dot-physicals/"},
        {"@type": "MedicalProcedure", "name": "Wellness & Nutrition Coaching", "url": "https://garciafamilymedicine.care/services/wellness-coaching/"}
      ],
      "employee": {"@id": "https://garciafamilymedicine.care/#dr-garcia"},
      "sameAs": [
        "https://www.facebook.com/garciafamilymedicine/",
        "https://www.linkedin.com/in/theresa-c-tess-garcia-md-faafp-dipl-abom-7a3014b6/",
        "https://www.doximity.com/pub/theresa-garcia-md",
        "https://www.healthgrades.com/group-directory/mo-missouri/blue-springs/garcia-family-medicine-xv9b43",
        "https://www.yelp.com/biz/garcia-family-medicine-a-direct-primary-care-practice-blue-springs"
      ]
    },
    {
      "@type": "Physician",
      "@id": "https://garciafamilymedicine.care/#dr-garcia",
      "name": "Theresa C. (Tess) Garcia, MD, FAAFP, Dipl. ABOM",
      "givenName": "Theresa",
      "familyName": "Garcia",
      "honorificPrefix": "Dr.",
      "honorificSuffix": "MD, FAAFP, Dipl. ABOM",
      "jobTitle": "Family Medicine & Obesity Medicine Physician",
      "url": "https://garciafamilymedicine.care/about/",
      "image": "https://garciafamilymedicine.care/wp-content/uploads/dr-tess-garcia.jpg",
      "worksFor": {"@id": "https://garciafamilymedicine.care/#clinic"},
      "medicalSpecialty": ["FamilyPractice", "Obesity"],
      "knowsLanguage": ["English", "Spanish"],
      "hasCredential": [
        {"@type": "EducationalOccupationalCredential", "credentialCategory": "Board Certification", "name": "American Board of Family Medicine"},
        {"@type": "EducationalOccupationalCredential", "credentialCategory": "Board Certification", "name": "American Board of Obesity Medicine (ABOM)"},
        {"@type": "EducationalOccupationalCredential", "credentialCategory": "Fellowship", "name": "Fellow, American Academy of Family Physicians (FAAFP)"}
      ]
    }
  ]
}
</script>
```

### B. FAQ schema (paste under FAQ section on each major page)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "What is direct primary care?",
     "acceptedAnswer": {"@type": "Answer", "text": "Direct primary care (DPC) is a membership model where you pay your doctor a flat monthly fee for unlimited visits and direct access — no insurance company in between. At Garcia Family Medicine the membership is $99/month."}},
    {"@type": "Question", "name": "Do I still need health insurance?",
     "acceptedAnswer": {"@type": "Answer", "text": "Yes, we recommend keeping a high-deductible plan for hospitalization, specialists, and emergencies. DPC replaces your primary-care copays and unlocks wholesale-priced labs and medications."}},
    {"@type": "Question", "name": "Do you prescribe GLP-1 medications like Wegovy, Ozempic, or tirzepatide?",
     "acceptedAnswer": {"@type": "Answer", "text": "Yes. Dr. Garcia is board-certified in Obesity Medicine and prescribes GLP-1 medications including semaglutide and tirzepatide as part of a supervised medical weight-loss program with labs, body-composition analysis, and biweekly coaching."}},
    {"@type": "Question", "name": "Is Spanish spoken at the office?",
     "acceptedAnswer": {"@type": "Answer", "text": "Sí. Se habla español. Our team includes Spanish-speaking staff."}},
    {"@type": "Question", "name": "How do I book an appointment?",
     "acceptedAnswer": {"@type": "Answer", "text": "Book online from any service page, call (816) 330-7575, or text Dr. Tess directly. Same- and next-day appointments are available for members."}}
  ]
}
</script>
```

### C. Reviews — aggregate rating (paste on homepage once you have ≥5 visible reviews)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalBusiness",
  "@id": "https://garciafamilymedicine.care/#clinic",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "5.0",
    "reviewCount": "47",
    "bestRating": "5"
  },
  "review": [
    {"@type": "Review",
     "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
     "author": {"@type": "Person", "name": "Patient (verified)"},
     "reviewBody": "Dr. Tess is not going to stop until she has exhausted every avenue when it comes to your health care. She goes above and beyond. There is no such thing as a 5-minute in-and-out visit — she's there to listen attentively to you."}
  ]
}
</script>
```
**Replace** `ratingValue` and `reviewCount` with real numbers from your Google Business Profile. Do not fabricate.

### D. Per-service `MedicalProcedure` schema
On each `/services/{slug}/` page, add a service-specific block. Example for medical weight management:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "MedicalProcedure",
  "name": "Medical Weight Management with GLP-1 and Tirzepatide",
  "procedureType": "https://schema.org/TherapeuticProcedure",
  "howPerformed": "Physician-supervised program including labs, body composition analysis, biweekly coaching, and FDA-approved anti-obesity medications when indicated.",
  "preparation": "Bring a list of current medications and any recent labs.",
  "url": "https://garciafamilymedicine.care/services/medical-weight-management/",
  "performer": {"@id": "https://garciafamilymedicine.care/#dr-garcia"}
}
</script>
```

---

## 6. Local SEO — Google Business Profile + citations

NAP must be **byte-identical** everywhere. Use this exact format:

```
Garcia Family Medicine
801 NW Saint Mary Dr, Suite 209
Blue Springs, MO 64014
(816) 330-7575
https://garciafamilymedicine.care
```

Avoid variants: "Saint Mary's Drive", "St. Mary Dr", "Ste 209", "(816)330-7575". Pick one and lock it in.

### Google Business Profile checklist
- [ ] Primary category: **Family Practice Physician**
- [ ] Secondary categories: **Weight Loss Service**, **Mental Health Service**, **Medical Clinic**
- [ ] Add ALL services (use the exact names from §5 schema)
- [ ] Attributes: Wheelchair accessible, LGBTQ+ friendly, Identifies as women-owned, Languages spoken: Spanish
- [ ] Photos: 15+ minimum — clinic exterior, waiting room, exam room, Dr. Garcia, team, signage, EMSELLA chair, lab area. Geotag if possible.
- [ ] Weekly "What's New" or "Offer" posts (member pricing, GLP-1 availability, etc.)
- [ ] Q&A section: pre-seed 8–10 questions and answer them yourself
- [ ] Booking link → `/contact/` (not the homepage)
- [ ] Reply to every review within 48 hours

### Citations to claim/update (NAP must match exactly)
- Healthgrades (already exists — verify NAP)
- Yelp (two listings exist — request merge; one is mis-categorized as "Counseling & Mental Health")
- Doximity (verify provider profile)
- Vitals.com
- WebMD Care
- Zocdoc
- DPC Frontier directory (https://mapper.dpcfrontier.com)
- FindMyDirectDoctor.com (already indexed)
- Local: Blue Springs Chamber of Commerce, Independence Chamber, Eastern Jackson County
- Spanish-language: Hispanos Unidos, local Spanish business directories

---

## 7. Content gaps — pages to add

Each one targets a clear search intent and has a built-in CTA.

| New page | Primary keyword | Why it matters |
|---|---|---|
| `/services/spanish-speaking-doctor/` (also Spanish version at `/es/medico-en-blue-springs/`) | "Spanish speaking doctor Blue Springs MO" | Very weak local competition; aligns with team's strength |
| `/services/glp1-tirzepatide/` | "Tirzepatide Blue Springs", "Mounjaro doctor Kansas City" | Splits from generic weight-management page to capture drug-specific intent |
| `/services/womens-health/` | "Women's health Blue Springs MO" | Captures broader female patient demographic |
| `/services/concierge-medicine/` | "Concierge doctor Blue Springs", "Concierge medicine Kansas City" | Concierge searchers don't know what DPC is; capture them with their term |
| `/insurance-and-pricing/` | "Doctor without insurance Blue Springs" | Removes #1 conversion objection |
| `/blog/` (landing + archive) | Long-tail informational queries | Topical authority for E-E-A-T |
| `/reviews/` | Branded + reputation | Aggregate Google, Healthgrades, Yelp reviews on one page; embed schema |
| `/faq/` | Long-tail informational | FAQPage schema, internal link target |
| `/new-patients/` | "How to become a patient at…" | Reduces friction at the conversion point |
| `/areas-served/blue-springs/`, `/grain-valley/`, `/lee-s-summit/`, `/independence/` | City-modified primary care | Local-pack expansion |

---

## 8. Homepage rewrite — structure that converts

The current homepage tries to do too many things at once. Replace with this top-to-bottom flow:

1. **Hero** (above the fold, ≤8 words headline)
   - H1: "Real medicine. Real time. Real doctor."
   - Sub: "$99/month direct primary care in Blue Springs, MO. Unlimited visits. Direct text access to Dr. Tess. No insurance required."
   - Primary CTA button: **Book your free meet-and-greet**
   - Secondary CTA: **Call (816) 330-7575** (click-to-call on mobile)
   - Trust bar under hero: "Board-Certified Family Medicine · Board-Certified Obesity Medicine (DABOM) · Se Habla Español"

2. **3-up value props** — icon + 1-line
   - 30–60 minute visits (not 10)
   - Text/call/email Dr. Tess directly
   - Wholesale labs and medications

3. **"How it works" 3 steps**
   - 1. Book a free meet-and-greet  ·  2. Choose your membership  ·  3. Start getting real care

4. **Services grid** (6 cards linking to `/services/*`)

5. **Meet Dr. Tess** — photo + 80 words + button to `/about/`

6. **Social proof** — 3 testimonials with patient first name + city + photo if permitted; "See all reviews →"

7. **Pricing teaser** — $99/month bullet list of what's included; "See full pricing →"

8. **FAQ accordion** (the 5 questions in §5B)

9. **Map + NAP + hours** with click-to-call and click-to-directions buttons

10. **Final CTA strip** — "Ready to meet a doctor who actually listens?" + button

---

## 9. Visual refresh checklist

Without seeing the current design, the universal wins for medical practice sites:

- **Typography**: pair a humanist serif for headlines (e.g., *Source Serif*, *Lora*, *Fraunces*) with a clean sans for body (*Inter*, *DM Sans*). Avoid Times New Roman and stock theme fonts.
- **Color**: lock in 2–3 brand colors and use them everywhere. Calm, trustworthy palettes work: deep teal + warm cream + a single accent (terracotta or gold) for CTAs. Avoid pure red/green which read as clinical alert states.
- **Imagery**: replace any stock photos of unrelated white-coated models with real photos of Dr. Garcia, the team, the clinic, and patients (with consent). Authenticity > polish.
- **CTA buttons**: large, single accent color, action verb ("Book a meet-and-greet", not "Submit"). Sticky bottom-bar CTA on mobile.
- **Whitespace**: medical sites read busy. Aim for 1.6–1.75 line-height on body, 24px+ section padding on mobile.
- **Accessibility (WCAG AA)**: 4.5:1 contrast minimum, focus rings visible, alt text on every image, form labels (not placeholder-only).
- **Performance budget**: LCP < 2.5s, CLS < 0.1, INP < 200ms. Test in PageSpeed Insights monthly.
- **Mobile-first**: 60%+ of medical searches are mobile. Test every page at 375px width.

---

## 10. Blog content plan — 12 posts to publish over 6 months

Each post should be 1,200–2,000 words, include an FAQPage schema block, link to ≥2 service pages, and end with a CTA. Title patterns shown.

1. "Direct Primary Care vs. Insurance: What $99/Month Actually Buys You in Blue Springs"
2. "Tirzepatide vs. Semaglutide: How a Board-Certified Obesity Medicine Doctor Chooses"
3. "What to Expect at a DOT Physical in Blue Springs, MO"
4. "Cómo Funciona la Medicina Familiar Directa — En Español" (Spanish content for ranking)
5. "EMSELLA for Incontinence: Who It's For, Who It Isn't"
6. "How to Switch Family Doctors Without Losing Continuity of Care"
7. "The Real Cost of a 'Free' Insurance Doctor: A Walkthrough of EOBs"
8. "Mental Health in Primary Care: Why Splitting Mind and Body Doesn't Work"
9. "Annual Physical Checklist: What Labs to Ask For After 40"
10. "Family Medicine for Veterans in Eastern Jackson County"
11. "GLP-1 Side Effects: Honest Answers from an Obesity Medicine Specialist"
12. "How Dr. Tess Lost 70 Pounds — And What It Taught Her About Treating Patients"

---

## 11. WordPress plugin stack (minimal, fast)

Keep plugin count low. Recommended:

- **Rank Math** (free) — titles/meta/schema/sitemap/redirects. Skip Yoast unless you already have it; Rank Math has more schema types built in.
- **WP Rocket** ($$) or **LiteSpeed Cache** (free if on LiteSpeed host) — caching + critical CSS.
- **ShortPixel** or **Smush** — image compression + WebP.
- **WPForms Lite** — contact and intake forms with spam protection.
- **Redirection** — only if Rank Math's redirect manager isn't enough.
- **Wordfence** or **Solid Security** — security hardening.
- **Site Kit by Google** — Search Console, Analytics 4, PageSpeed in one dashboard.

Delete anything else. Every active plugin is page-weight + a security surface.

---

## 12. Tracking — set up before changes ship so you can measure

- [ ] Google Search Console — verify property, submit sitemap, monitor "Pages" report weekly.
- [ ] Google Analytics 4 — events: `book_appointment_click`, `phone_call_click` (use `tel:` link tracking), `text_dr_tess_click`, `form_submit`.
- [ ] Set up a unique CallRail or Twilio tracking number on the site (forwards to your real number) so you know which marketing channel drove the call.
- [ ] Google Tag Manager preferred over hard-coding tags.
- [ ] Bing Webmaster Tools — same sitemap, free traffic.

KPIs to watch month over month:
- Branded vs. non-branded impressions in Search Console
- Local pack ranking for "family doctor Blue Springs MO" and "weight loss doctor Blue Springs"
- New-patient form submissions
- Click-to-call events on mobile
- Google Business Profile actions (calls, direction requests, website clicks)

---

## 13. Compliance reminders

- **HIPAA**: any contact form that asks for symptoms/PHI must submit over HTTPS and the data must be stored in a HIPAA-eligible system. Don't email PHI from WordPress without a BAA-covered provider. Safer: link to your patient portal rather than collecting PHI in WP forms.
- **YMYL / E-E-A-T**: every medical claim must cite a source. Author every blog post under Dr. Garcia's byline with her credentials and a link to `/about/`.
- **FTC**: testimonials must be real and verifiable. Don't post fake reviews — Google detects and de-ranks. If a review mentions a specific outcome ("lost 65 lbs"), add a disclaimer that individual results vary.
- **ADA**: 4.5:1 color contrast, alt text, keyboard navigability. Run WAVE or axe DevTools on every template.

---

## Next step

Tell me which of these to tackle first and I'll produce the finished artifact:

- "Draft the homepage copy" → full hero + sections from §8
- "Write the new service pages" → full HTML/Gutenberg copy for any of §7
- "Give me the JSON-LD with my real review count" → I'll fill in the rating data once you share it
- "Draft the first blog post" → pick one from §10 and I'll write the whole article
- "Audit my Google Business Profile" → share a screenshot and I'll mark up what to change
