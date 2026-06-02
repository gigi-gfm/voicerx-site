#!/usr/bin/env python3
"""Build a Missouri Disability + IME referral/TPA outreach list for Garcia Family Medicine."""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ---- Styling helpers ----
NAVY = "1F3864"
ORANGE = "C55A11"
LBLUE = "D6E4F0"
GREY = "F2F2F2"
thin = Side(style="thin", color="BFBFBF")
border = Border(left=thin, right=thin, top=thin, bottom=thin)
wrap = Alignment(vertical="top", wrap_text=True)
center = Alignment(vertical="center", horizontal="center", wrap_text=True)

def style_header(ws, ncols, row=1):
    for c in range(1, ncols + 1):
        cell = ws.cell(row=row, column=c)
        cell.font = Font(bold=True, color="FFFFFF", size=11)
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.alignment = center
        cell.border = border

def zebra(ws, nrows, ncols, start=2):
    for r in range(start, start + nrows):
        fill = PatternFill("solid", fgColor=GREY) if (r - start) % 2 else None
        for c in range(1, ncols + 1):
            cell = ws.cell(row=r, column=c)
            cell.alignment = wrap
            cell.border = border
            if fill:
                cell.fill = fill

# =====================================================================
# SHEET 1: Disability + IME outreach list
# =====================================================================
ws = wb.active
ws.title = "MO Disability + IME List"

headers = ["#", "Organization", "Category", "What they administer / refer",
           "Best GFM fit", "Website", "How to engage (provider / vendor sign-up)",
           "Missouri relevance", "Priority", "Status / Notes"]
ws.append(headers)

# Category P = VA disability, S = SSA disability, W = Workers' comp/legal/auto IME, G = Gov/state, R = Referral source
rows = [
    # ---------- VA DISABILITY (C&P) EXAM CONTRACTORS ----------
    ["VA disability — C&P exam TPAs (contract licensed MO physicians to perform Compensation & Pension exams)"],
    [1, "QTC Medical Services (a Leidos company)", "VA C&P exam TPA",
     "Largest VA contractor for Compensation & Pension (disability) exams nationwide.",
     "IME / disability exams for veterans", "qtcm.com",
     "Apply via 'Provider Network' / 'Join our network' page; credentialing required.",
     "Serves MO veterans; needs in-state examining providers.", "HIGH",
     "Top target — verify current provider intake email/phone."],
    [2, "VES – Veterans Evaluation Services (a Maximus company)", "VA C&P exam TPA",
     "Major VA disability exam contractor; builds nationwide examiner network.",
     "IME / disability exams for veterans", "vesservices.com",
     "'Providers' > join network; submit CV, licenses, board certs.",
     "Contracts MO-licensed physicians for veteran exams.", "HIGH",
     "Verify intake contact."],
    [3, "Optum Serve (formerly LHI / Logistics Health Inc)", "VA C&P exam TPA",
     "VA & federal medical exam contractor; disability + readiness exams.",
     "IME / disability exams for veterans", "optumserve.com",
     "'Providers' / network participation; credentialing via Optum.",
     "Active VA exam volume in MO.", "HIGH", "Verify provider onboarding path."],
    [4, "Loyal Source Government Services", "VA / federal medical staffing",
     "Staffs clinicians for VA & federal disability/medical exam contracts.",
     "IME / disability exams for veterans", "loyalsource.com",
     "Clinician opportunities / provider application.", "Places clinicians on MO-area contracts.",
     "MED", "Good secondary VA channel."],
    [5, "Sterling Medical Associates", "VA contract exams",
     "Contracts physicians for VA and government medical evaluations.",
     "IME / disability exams for veterans", "sterlingmedical.com",
     "Provider / careers inquiry.", "Recruits across states incl. MO.", "MED",
     "Verify if currently staffing MO."],

    # ---------- SSA DISABILITY (CONSULTATIVE EXAMS) ----------
    ["Social Security disability — Consultative Exam (CE) channels (SSA pays providers to examine claimants)"],
    [6, "Missouri Disability Determination Services (DDS)", "State SSA disability agency",
     "Decides MO Social Security disability claims; contracts local providers for Consultative Exams (CEs).",
     "Disability consultative exams (adult/peds, mental, physical)", "dss.mo.gov (Family Support Division / DDS)",
     "Contact MO DDS Professional Relations Officer to become a CE provider.",
     "THE primary in-state SSA disability channel.", "HIGH",
     "Ask specifically about CE provider enrollment + fee schedule."],
    [7, "MDExams / MDSI (Medical Diagnostic Services)", "SSA CE scheduling vendor",
     "National vendor that schedules SSA consultative exams into local clinics.",
     "Disability consultative exams", "mdexams.com",
     "'Become a provider' / clinic partnership inquiry.",
     "Places SSA CE volume with MO clinics.", "MED", "Verify MO coverage."],
    [8, "Dane Street", "IME + disability review network",
     "IME, peer review, and disability evaluation network for payers & SSA-related work.",
     "IME + disability exams", "danestreet.com",
     "'Join our panel' / physician panel application.",
     "Recruits MO examiners.", "HIGH", "Covers both IME and disability — strong fit."],

    # ---------- WORKERS' COMP / AUTO / LEGAL IME NETWORKS ----------
    ["Workers' comp / auto / legal IME networks (place IME cases with MO examining physicians)"],
    [9, "ExamWorks", "IME network (largest)",
     "Largest IME company in the U.S.; workers' comp, auto, liability, disability IMEs.",
     "IME (workers' comp, auto, legal)", "examworks.com",
     "'Join our panel of physicians' / provider recruitment.",
     "Active MO case volume; needs local examiners.", "HIGH", "Anchor IME target."],
    [10, "MES Solutions (ExamWorks group)", "IME network",
     "IME and peer review services for insurers and employers.",
     "IME (workers' comp, disability)", "mesgroup.com",
     "Provider / physician panel application.", "Serves MO payers.", "MED",
     "Same group as ExamWorks — one outreach may cover both."],
    [11, "MCN – Medical Consultants Network", "IME network",
     "IME, peer review, and utilization review provider network.",
     "IME (workers' comp, auto, legal)", "mcn.com",
     "'Providers' > join network.", "Recruits MO physicians.", "MED", "Verify MO need."],
    [12, "Genex Services (Enlyte)", "Workers' comp managed care / IME",
     "Workers' comp case management, IME and peer review.",
     "IME (workers' comp)", "genexservices.com",
     "Provider network inquiry.", "MO workers' comp footprint.", "MED", "Part of Enlyte/Mitchell."],
    [13, "IMX Medical Management Services", "IME network",
     "Independent medical exams and record reviews for insurers/attorneys.",
     "IME (auto, workers' comp, legal)", "imxmed.com",
     "Provider application.", "Places cases regionally incl. MO.", "LOW", "Verify MO coverage."],
    [14, "CorVel", "Workers' comp TPA",
     "Workers' comp third-party administrator; uses IME/exam providers.",
     "IME (workers' comp)", "corvel.com",
     "Provider / network inquiry.", "TPA active in MO.", "MED", "True 'TPA' in workers' comp sense."],

    # ---------- MISSOURI STATE / GOVERNMENT ----------
    ["Missouri state & government bodies (direct credentialing / listings)"],
    [15, "Missouri Division of Workers' Compensation (Dept. of Labor)", "State agency",
     "Administers MO workers' comp; independent medical exams & ratings used in claims.",
     "IME / impairment ratings", "labor.mo.gov/dwc",
     "Review provider/exam requirements; get listed where applicable.",
     "Statewide authority on MO workers' comp IMEs.", "MED",
     "Understand MO rating rules (AMA Guides) before marketing."],
    [16, "Missouri Veterans Commission", "State veterans agency",
     "State veterans services; CVSOs help vets file disability claims (need nexus/exam support).",
     "Nexus letters / veteran disability exams", "mvc.dps.mo.gov",
     "Introduce GFM IME/Nexus services to MVC & County Veterans Service Officers.",
     "Direct line to MO veterans needing evidence.", "HIGH",
     "Referral relationship, not a TPA — high-value."],

    # ---------- REFERRAL SOURCES (NOT TPAs) ----------
    ["Referral sources — attorneys & veteran orgs (send claimants who need IMEs / nexus letters)"],
    [17, "Missouri workers' comp & personal-injury attorneys", "Attorney referral",
     "Plaintiff & defense attorneys routinely order IMEs and medical opinions.",
     "IME / medical opinion letters", "Local firms (e.g., Boyd, Kenter, Thomas & Parrish – already in your files)",
     "Targeted outreach with fee schedule + turnaround (you already emailed BKTP).",
     "Local Jackson County / KC metro firms.", "HIGH",
     "Warm channel — you already have an IME report for a BKTP case (M. Mendez)."],
    [18, "Missouri Association of Trial Attorneys (MATA)", "Attorney association",
     "Plaintiff trial bar; members need independent medical experts.",
     "IME / expert medical opinions", "matalaw.com",
     "Sponsor / directory listing / educational outreach.",
     "Statewide plaintiff attorney audience.", "MED", "Marketing channel to many firms at once."],
    [19, "DAV / VFW / American Legion (Missouri departments)", "Veteran service orgs",
     "VSOs assist veterans with disability claims; refer for nexus letters & exams.",
     "Nexus letters / veteran disability exams", "dav.org · vfwmo.org · molegion.org",
     "Introduce Veterans@Work IME + Nexus services to MO service officers.",
     "Large MO veteran membership.", "HIGH", "Pairs with Missouri Veterans Commission outreach."],
    [20, "County Veterans Service Officers (Jackson, Clay, Cass, etc.)", "Local referral",
     "Frontline help for vets filing claims; trusted referrers.",
     "Nexus letters / veteran disability exams", "County govt veteran services pages",
     "Direct relationship-building with local CVSOs.", "Local, high-trust referrals.", "HIGH",
     "Start with your home counties."],
]

# Write rows, handling section banner rows (single-element lists)
r = 2
data_row_count = 0
ncols = len(headers)
for row in rows:
    if len(row) == 1:  # section banner
        ws.cell(row=r, column=1, value=row[0])
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=ncols)
        cell = ws.cell(row=r, column=1)
        cell.font = Font(bold=True, color="FFFFFF", size=10)
        cell.fill = PatternFill("solid", fgColor=ORANGE)
        cell.alignment = Alignment(vertical="center", horizontal="left", wrap_text=True)
        for c in range(1, ncols + 1):
            ws.cell(row=r, column=c).border = border
    else:
        for c, val in enumerate(row, start=1):
            cell = ws.cell(row=r, column=c, value=val)
            cell.alignment = wrap
            cell.border = border
            if c == 9:  # priority color
                p = str(val).upper()
                if p == "HIGH":
                    cell.fill = PatternFill("solid", fgColor="C6EFCE")
                elif p == "MED":
                    cell.fill = PatternFill("solid", fgColor="FFEB9C")
                elif p == "LOW":
                    cell.fill = PatternFill("solid", fgColor="F2F2F2")
                cell.alignment = center
            if c == 1:
                cell.alignment = center
        data_row_count += 1
    r += 1

style_header(ws, ncols)

widths = [4, 30, 18, 34, 20, 22, 34, 26, 9, 32]
for i, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(i)].width = w
ws.row_dimensions[1].height = 30
ws.freeze_panes = "A2"

# =====================================================================
# SHEET 2: How to use / read me
# =====================================================================
ws2 = wb.create_sheet("How to use")
notes = [
    ["Garcia Family Medicine — Missouri Disability & IME Outreach List", ""],
    ["", ""],
    ["Purpose", "Organizations to approach so GFM (Dr. Tess) receives a steady flow of disability and IME work: VA disability (C&P) exams, Social Security consultative exams, and workers'-comp/auto/legal IMEs."],
    ["", ""],
    ["Three ways the work flows in", ""],
    ["1. VA disability TPAs", "QTC, VES, Optum Serve, etc. contract you as a network examiner to perform veteran C&P disability exams. Highest volume; requires credentialing."],
    ["2. SSA disability (CE)", "Missouri DDS pays providers to examine Social Security claimants (Consultative Exams). MDExams/Dane Street also schedule these into clinics."],
    ["3. IME networks & attorneys", "ExamWorks, Dane Street, MCN, etc. place workers'-comp/auto/legal IME cases. Attorneys & VSOs send claimants directly for IMEs and nexus letters."],
    ["", ""],
    ["Priority key", "HIGH = start here (volume or warm relationship). MED = solid secondary. LOW = verify fit first."],
    ["", ""],
    ["Suggested first moves", "1) Apply to QTC + VES + Optum Serve (VA). 2) Call Missouri DDS about CE provider enrollment. 3) Join ExamWorks + Dane Street panels. 4) Re-contact BKTP and pitch CVSOs/DAV with your Veterans@Work IME + Nexus packet."],
    ["", ""],
    ["IMPORTANT — verify before sending", "Websites listed are the official company domains, but exact provider-intake emails/phone numbers change. Confirm the current 'join our network / become a provider' contact on each site before applying. Do not treat any contact detail here as final."],
    ["", ""],
    ["Assets you already have to attach", "• IME service + pricing sheet  • Veterans@Work IME Referral Flyer + sample MoU  • Nexus Letter Services doc  • A completed IME report (M. Mendez) as a work sample."],
]
for row in notes:
    ws2.append(row)
ws2.column_dimensions["A"].width = 30
ws2.column_dimensions["B"].width = 95
ws2["A1"].font = Font(bold=True, size=14, color=NAVY)
for r in range(1, len(notes) + 1):
    ws2.cell(row=r, column=1).font = Font(bold=True, color=NAVY) if ws2.cell(row=r, column=1).value else Font()
    ws2.cell(row=r, column=1).alignment = Alignment(vertical="top", wrap_text=True)
    ws2.cell(row=r, column=2).alignment = Alignment(vertical="top", wrap_text=True)
ws2["A1"].font = Font(bold=True, size=14, color=NAVY)

out = "/home/user/voicerx-site/GFM_Missouri_Disability_IME_List.xlsx"
wb.save(out)
print("saved", out, "| data rows:", data_row_count)
