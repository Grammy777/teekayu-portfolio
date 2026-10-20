#!/usr/bin/env python3
"""Generates index.html for the portfolio.

All copy lives in T (Thai, English). The HTML ships with Thai pre-filled so the
page reads without JavaScript; the script swaps to English from the same table.
Edit copy here, then run:  python3 src/gen.py
"""
import html, json, urllib.parse, pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "index.html"

# Contact links that do not exist yet stay hidden. Paste the URL to show them.
LINKS = {"github": "", "linkedin": ""}
EMAIL = "teekayu.13579@gmail.com"
# Public address of the site once it is on GitHub Pages, e.g. "https://<user>.github.io/<repo>/".
# When set, link previews (LINE, LinkedIn, Facebook) get an absolute image and canonical URL.
SITE_URL = "https://grammy777.github.io/teekayu-portfolio/"
PHONE_DISPLAY, PHONE_TEL = "062-594-4932", "+66625944932"

T = {
  # document
  "doc_title": ("ฑีฆายุ ปรัชญกุล · Frontend Developer & Business Analyst",
                "Teekayu Prachayakul · Frontend Developer & Business Analyst"),
  "doc_desc": ('พอร์ตโฟลิโอของ ฑีฆายุ ปรัชญกุล Frontend Developer & Business Analyst ที่ Zenith Comp: เก็บความต้องการกับลูกค้า เขียน SRS ออกแบบหน้าจอ และทดสอบระบบ', 'Portfolio of Teekayu Prachayakul, Frontend Developer & Business Analyst at Zenith Comp: client requirements, SRS writing, UI design and system testing.'),
  "skip": ("ข้ามไปที่เนื้อหา", "Skip to content"),
  "lang_label": ("ภาษา", "Language"),
  # intro
  "name": ("ฑีฆายุ ปรัชญกุล", "Teekayu Prachayakul"),
  "name_short": ("ฑีฆายุ ป.", "Teekayu P."),
  "where": ("ชลบุรี · ฝึกงานที่ Zenith Comp · 24 ส.ค. – 1 ธ.ค. 2569", "Chonburi, Thailand · Intern at Zenith Comp · 24 Aug – 1 Dec 2026"),
  "thesis": ('ผมคุยกับลูกค้าจนได้ความต้องการที่ชัด เขียนเป็น SRS ออกแบบหน้าจอ แล้วทดสอบจนระบบพร้อมใช้งาน', 'I turn client conversations into clear specs, screen designs and tested systems.'),
  "avail": ('เปิดรับงานประจำสาย Full Stack / Cybersecurity', 'Open to full-time Full Stack / Cybersecurity roles'),
  "avail_date": ("เริ่มงานได้ ธ.ค. 2569", "Available from Dec 2026"),
  "cta_email": ("ส่งอีเมลหาผม", "Email me"),
  "nav_label": ("เมนูหลัก", "Main"),
  "nav_exp": ("ประสบการณ์", "Experience"),
  "nav_proj": ("ผลงาน", "Projects"),
  "nav_skills": ("ทักษะ", "Skills"),
  "nav_about": ("เกี่ยวกับ", "About"),
  "nav_contact": ("ติดต่อ", "Contact"),
  # experience
  "exp_h": ("ประสบการณ์", "Experience"),
  "exp_role": ("Zenith Comp · ฝึกงานตำแหน่ง Frontend Developer & BA", "Zenith Comp · Frontend Developer & BA internship"),
  "exp_date": ("24 ส.ค. – 1 ธ.ค. 2569", "24 Aug – 1 Dec 2026"),
  "exp_lead": ("ผมทำครบทุกขั้นของงานระบบ ตั้งแต่เก็บ requirement จนถึงทดสอบกับลูกค้า ใน 3 โปรเจกต์ลูกค้าจริง",
               "Every stage of the work, from gathering requirements to testing with the client, across three client projects."),
  "pipe_label": ("ขั้นของงาน", "Stage of work"),
  "st_req": ("Requirement", "Requirement"), "st_req_s": ("เก็บความต้องการ", "gather needs"),
  "st_spec": ("Spec", "Spec"), "st_spec_s": ("เขียน SRS · วิเคราะห์", "SRS · analysis"),
  "st_design": ("Design", "Design"), "st_design_s": ("ออกแบบหน้าจอ", "screen design"),
  "st_test": ("Test", "Test"), "st_test_s": ("ทดสอบกับลูกค้า", "test with client"),
  "pj_bm": ('Behn Meyer TMS / Shipping Hub · ระบบติดตามการขนส่ง web + mobile · Go, PostgreSQL, MinIO', 'Behn Meyer TMS / Shipping Hub · logistics tracking, web + mobile · Go, PostgreSQL, MinIO'),
  "pj_gov": ("ระบบคำของบประมาณและติดตามผล · กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์",
             "Budget request & monitoring system · Ministry of Social Development and Human Security"),
  "pj_nsc": ("M-NSC · ระบบบริหารการประชุม web + iPad", "M-NSC · meeting management, web + iPad"),
  "e1": ("เข้าประชุมกับลูกค้า เก็บ requirement ได้กว่า 100 รายการ จาก 5 กลุ่มผู้ใช้: บริษัทขนส่ง, Admin, เซลล์, ลูกค้า และคนขับ",
         "Joined client meetings and gathered 100+ requirements from 5 user groups: carriers, admins, sales, customers and drivers."),
  "e2": ('เขียน SRS (Functional Requirements 69 รายการ, BPMN swimlane) และเอกสารแปล UI ภาษาอังกฤษ 157 รายการ', 'Wrote the SRS (69 functional requirements, BPMN swimlanes) and an English UI localization spec (157 strings).'),
  "e3": ('ร่วมเขียน SRS ครอบคลุม 5 ระบบย่อย (คำของบประมาณ, ติดตามการเบิกจ่าย, e-Inspection, PA-OPS, PMQA) และวิเคราะห์ระบบเดิมบน AppSheet', 'Co-wrote the SRS for 5 subsystems (Budget Proposal, Disbursement Monitoring, e-Inspection, PA-OPS, PMQA) and analyzed the legacy AppSheet system.'),
  "e4": ('วิเคราะห์ตรรกะคำนวณ CO2 จากการขนส่ง (Emission Factor ของ TGO องค์การบริหารจัดการก๊าซเรือนกระจก, ISO 14060) และการเชื่อมต่อ SAP, CRC, GHG API และ Mapbox', "Analyzed the transport CO2 calculation logic (emission factors from TGO, Thailand's greenhouse gas agency; ISO 14060) and the SAP, CRC, GHG API and Mapbox integrations."),
  "pj_design": ('Behn Meyer TMS และระบบคำของบประมาณ (พม.)', 'Behn Meyer TMS and the Ministry budget system'),
  "e6": ('ออกแบบหน้าจอ web และ mobile ของ Shipping Hub และหน้าจอ PA-OPS ของระบบคำของบประมาณ', 'Designed the Shipping Hub web and mobile screens and the PA-OPS screens of the budget system.'),
  "e5": ('ทดสอบการสร้างการประชุม ระเบียบวาระ แนบเอกสาร ประชุมลับ ลายน้ำ และ login ด้วย Thai ID บันทึกปัญหาและติดตามการแก้ไขร่วมกับลูกค้า', 'Tested meeting creation, agendas, attachments, confidential meetings, watermarks and Thai ID login; logged defects and verified fixes with the client.'),
  # projects
  "proj_h": ("ผลงาน", "Projects"),
  "neo_t": ("NeoFit · ลองสวมเครื่องประดับเสมือนจริง", "NeoFit · virtual jewelry try-on"),
  "neo_k": ('Senior Project · ทีม 3 คน', 'Senior project · team of 3'),
  "neo_d": ('เว็บขายเครื่องประดับที่ลองสวมได้ด้วย AR ผมรับผิดชอบฟังก์ชันหลัก คือการลองสวมแหวนแบบเรียลไทม์ผ่านกล้อง ด้วย MediaPipe Hands และ Three.js/WebGL ตัวเว็บเป็น React.js บน Firebase พร้อม Admin Dashboard เก็บความต้องการจากลูกค้าจริงและนำเสนอต่ออาจารย์', 'A jewelry store where shoppers try pieces on with AR. I built the core feature: real-time ring try-on through the camera with MediaPipe Hands and Three.js/WebGL. The site runs on React.js and Firebase with an admin dashboard; requirements came from real clients and the work was presented to faculty.'),
  "neo_r": ("ผลประเมิน 4.14/5 จากผู้ใช้ 35 คน · 4.20/5 จากผู้เชี่ยวชาญ 5 คน", "Rated 4.14/5 by 35 users · 4.20/5 by 5 experts"),
  "neo_alt": ("หน้าแรกของเว็บ NeoFit: หัวข้อ Virtual Try On Jewelry ข้างภาพแหวนบนนิ้ว", "NeoFit home page: the Virtual Try On Jewelry headline beside a ring on a finger"),
  "neo_link": ("เปิดเว็บจริง", "Open the live site"),
  "newtab": ("(เปิดในแท็บใหม่)", "(opens in a new tab)"),
  "myl_t": ("Match Your Life · แอปจับคู่ประกัน", "Match Your Life · insurance matching app"),
  "myl_k": ("Hackathon · ทำเป็นทีม", "Hackathon · team"),
  "myl_d": ('ต้นแบบแอปจับคู่แผนประกันตามไลฟ์สไตล์ของผู้ใช้ โดยไม่ต้องผ่านเซลส์ ทำงานเป็นทีมภายใต้เวลาจำกัดของการแข่งขัน', "A prototype app that matches insurance plans to a user's lifestyle without a sales agent, built as a team under a tight hackathon deadline."),
  "myl_alt1": ("หน้าเข้าสู่ระบบของแอป Match Your Life", "Match Your Life login screen"),
  "myl_alt2": ("หน้ากรอกวันเกิดของแอป", "Birthday entry screen"),
  "myl_alt3": ("หน้าสรุปความครอบคลุมของประกันเป็นกราฟใยแมงมุม", "Coverage summary as a radar chart"),
  "stock_t": ("Stock Management System · ระบบจัดการสต็อก", "Stock Management System"),
  "personal": ("โปรเจกต์ส่วนตัว", "Personal project"),
  "stock_d": ("ระบบหลังบ้านที่นำเข้าข้อมูลสินค้า รายงานขาย และประวัติลูกค้าจากไฟล์ Excel ได้โดยตรง ส่งออกกลับเป็น Excel ได้ มี Dashboard บิล โอนสินค้า และจัดการผู้ใช้",
              "An inventory back office that imports products, sales reports and customer history straight from Excel and exports back to it, with a dashboard, billing, stock transfers and user management."),
  "stock_alt": ("หน้า Import ข้อมูลจาก Excel ของระบบจัดการสต็อก", "The Excel import screen of the stock system"),
  "char_t": ("Charites · ระบบสมาชิกและใบรับประกัน", "Charites · membership & warranty"),
  "char_d": ("ระบบสมาชิกที่เก็บข้อมูลลูกค้า ประวัติการซื้อ และใบรับประกันไว้ในระบบ ลูกค้าไม่ต้องพกใบรับประกันเอง ส่วนพนักงานจัดการสต็อก การขาย และใบรับประกันได้ในที่เดียว",
             "A membership system that keeps customer data, purchase history and warranties, so customers never carry paper warranty cards, while staff manage stock, sales and warranties in one place."),
  "char_alt": ("หน้าเข้าสู่ระบบสำหรับพนักงานและลูกค้าของ Charites", "Charites sign-in options for staff and customers"),
  # skills
  "skills_h": ("ทักษะ", "Skills"),
  "sk_work": ('ภาษาโปรแกรม', 'Programming languages'),
  "sk_proj": ('Frameworks', 'Frameworks'),
  "sk_other": ('ฐานข้อมูลและที่เก็บไฟล์', 'Databases & storage'),
  "sk_learn": ('เครื่องมือ', 'Tools'),
  "sk_ba": ('Business Analysis', 'Business Analysis'),
  "sk_lang": ("ภาษาที่ใช้สื่อสาร", "Spoken languages"),
  "sk_reqg": ('เก็บความต้องการ', 'Requirement gathering'),
  "sk_cyber": ('ออกแบบหน้าจอ', 'UI design'),
  "sk_test": ('ทดสอบระบบ', 'System testing'),
  "sk_laravel": ('Laravel (กำลังเรียน)', 'Laravel (learning)'),
  "sp_th": ("ไทย (ภาษาแม่)", "Thai (native)"),
  "sp_en": ("อังกฤษ (ระดับกลาง)", "English (intermediate)"),
  # about
  "about_h": ("เกี่ยวกับผม", "About"),
  "about_p": ("จบวิทยาการคอมพิวเตอร์ คณะเทคโนโลยีสารสนเทศและนวัตกรรม มหาวิทยาลัยกรุงเทพ (2565–2569) อยู่ชลบุรี ได้ลงมือทำจริงผ่าน Senior Project, Hackathon และการฝึกงาน และกำลังต่อยอดด้าน Cybersecurity จากใบรับรองด้านล่าง",
              "B.Sc. Computer Science, School of Information Technology and Innovation, Bangkok University (2022–2026), based in Chonburi. Hands-on through a senior project, a hackathon and my internship, and building on the cybersecurity certificates below."),
  "certs_h": ("ใบรับรอง", "Certificates"),
  "c_ncsa": ("Basic Cybersecurity", "Basic Cybersecurity"),
  "c_ncsa_m": ("สกมช. (NCSA) · พ.ย. 2567", "NCSA Thailand · Nov 2024"),
  "c_fs": ("พื้นฐาน Cybersecurity ที่สำคัญเพื่อการปกป้องระบบและข้อมูล", "Essential Cybersecurity Fundamentals for Protecting Systems & Data"),
  "c_fs_m": ("FutureSkill · ก.ค. 2569", "FutureSkill · Jul 2026"),
  "c_gai": ("Generative AI for Data Visualization", "Generative AI for Data Visualization"),
  "c_gai_m": ("Coursera · ก.พ. 2568", "Coursera · Feb 2025"),
  "c_bot": ("Python Chatbot with ChatGPT", "Python Chatbot with ChatGPT"),
  "c_bot_m": ("Coursera · เม.ย. 2568", "Coursera · Apr 2025"),
  "view": ("ดูใบรับรอง", "View"),
  "verify": ("ตรวจสอบ", "Verify"),
  # contact
  "contact_h": ("ติดต่อ", "Contact"),
  "contact_p": ('กำลังหาคนสาย Full Stack หรือ Cybersecurity หรืออยากรู้รายละเอียดโปรเจกต์ไหน ส่งอีเมลมาได้เลยครับ', 'Hiring for a Full Stack or Cybersecurity role, or want details on any project? Send me an email.'),
  "phone": ("โทร", "Phone"),
  "phone_num": ("062-594-4932", "+66 62-594-4932"),
  "lang_done": ("เปลี่ยนเป็นภาษาไทยแล้ว", "Switched to English"),
  "email_short": ("อีเมล", "Email"),
  "copy": ("คัดลอกอีเมล", "Copy email"),
  "copied": ("คัดลอกแล้ว", "Copied"),
  "copy_fail": ("คัดลอกไม่ได้ กดค้างที่อีเมลเพื่อคัดลอกเอง", "Couldn't copy. Press and hold the address to copy it."),
  "foot": ("© 2569 ฑีฆายุ ปรัชญกุล · สร้างด้วย HTML, CSS และ JavaScript", "© 2026 Teekayu Prachayakul · Built with HTML, CSS and JavaScript"),
}

# Chrome's Thai dictionary does not know some loanwords and breaks them mid-word;
# a word joiner (U+2060) keeps them whole. Applied to Thai strings only.
NOBREAK = ["โปรเจกต์", "เริ่มงาน"]
def _join(t):
    for w in NOBREAK:
        t = t.replace(w, "\u2060".join(w))
    return t
T = {k: (_join(v[0]), v[1]) for k, v in T.items()}

def th(k): return html.escape(T[k][0])
def tx(k, tag="span", cls=None, extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-i18n="{k}"{extra}>{th(k)}</{tag}>'

def pdf(name): return "certificate/" + urllib.parse.quote(name)

NEWTAB = f'<span class="sr" data-i18n="newtab">{th("newtab")}</span>'

def ext(href, key, cls="arrow-link"):
    return (f'<a class="{cls}" href="{href}" target="_blank" rel="noopener">'
            f'{tx(key)}<svg class="ico" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 11 11 5M6 5h5v5"/></svg>{NEWTAB}</a>')

STAGES = [("req", "st_req", "st_req_s"), ("spec", "st_spec", "st_spec_s"),
          ("design", "st_design", "st_design_s"), ("test", "st_test", "st_test_s")]

ITEMS = [("req", "pj_bm", "e1", []),
         ("spec", "pj_bm", "e2", []),
         ("spec", "pj_bm", "e4", []),
         ("spec", "pj_gov", "e3", []),
         ("design", "pj_design", "e6", []),
         ("test", "pj_nsc", "e5", [])]

def stage_name(s): return {"req": "st_req", "spec": "st_spec", "design": "st_design", "test": "st_test"}[s]

pipeline = "\n".join(
    f'<li class="step" data-step="{s}"><span class="step-dot" aria-hidden="true"></span>'
    f'<span class="step-name" data-i18n="{n}">{th(n)}</span><span class="step-sub" data-i18n="{sub}">{th(sub)}</span></li>'
    for s, n, sub in STAGES)

items = "\n".join(
    f'<li class="work" data-stage="{s}">'
    f'<p class="work-stage"><span data-i18n="{stage_name(s)}">{th(stage_name(s))}</span></p>'
    f'<div class="work-body"><p class="work-proj" data-i18n="{p}">{th(p)}</p>'
    f'<p class="work-text" data-i18n="{e}">{th(e)}</p>'
    + (f'<p class="stack">{" · ".join(html.escape(x) for x in tags)}</p>' if tags else "")
    + '</div></li>' for s, p, e, tags in ITEMS)

def chips(items):
    out = []
    for it in items:
        if it.startswith("@"):
            out.append(f'<li data-i18n="{it[1:]}">{th(it[1:])}</li>')
        else:
            out.append(f"<li>{html.escape(it)}</li>")
    return "<ul class=\"skill-list\">" + "".join(out) + "</ul>"

SKILLS = [
  ("sk_work", ["JavaScript", "Go", "PHP", "Python", "SQL", "HTML / CSS"]),
  ("sk_proj", ["React.js", "Node.js", "Three.js", "MediaPipe", "@sk_laravel"]),
  ("sk_other", ["PostgreSQL", "MySQL", "Firebase", "MinIO"]),
  ("sk_learn", ["Docker", "DBeaver", "Git / GitHub", "VS Code", "Figma", "draw.io", "Linux"]),
  ("sk_ba", ["@sk_reqg", "SRS / TOR", "BPMN", "@sk_cyber", "@sk_test"]),
  ("sk_lang", ["@sp_th", "@sp_en"]),
]
skills = "\n".join(f'<div class="skill-row"><dt data-i18n="{k}">{th(k)}</dt><dd>{chips(v)}</dd></div>' for k, v in SKILLS)

CERTS = [("c_ncsa", "c_ncsa_m", pdf("HSKGR9U58ZL1S.pdf"), "view"),
         ("c_fs", "c_fs_m", pdf("พื้นฐาน Cybersecurity.pdf"), "view"),
         ("c_gai", "c_gai_m", "https://coursera.org/verify/PVITIWXBP2PM", "verify"),
         ("c_bot", "c_bot_m", "https://coursera.org/verify/ZMUPV2WB1IQL", "verify")]
certs = "\n".join(
    f'<li class="cert"><div><p class="cert-t" data-i18n="{t}">{th(t)}</p><p class="cert-m" data-i18n="{m}">{th(m)}</p></div>'
    f'{ext(href, act)}</li>' for t, m, href, act in CERTS)

def social(kind, label):
    url = LINKS[kind]
    hidden = "" if url else " hidden"
    return f'<a class="text-link" data-link="{kind}" href="{html.escape(url or "#")}" target="_blank" rel="noopener"{hidden}>{label}{NEWTAB}</a>'

socials = social("github", "GitHub") + social("linkedin", "LinkedIn")

I18N_JSON = json.dumps({k: {"th": v[0], "en": v[1]} for k, v in T.items()}, ensure_ascii=False)

CSS = (pathlib.Path(__file__).with_name("style.css")).read_text(encoding="utf-8")
JS = (pathlib.Path(__file__).with_name("app.js")).read_text(encoding="utf-8")

page = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{th("doc_title")}</title>
<meta name="description" content="{th("doc_desc")}">
<meta property="og:title" content="{th("doc_title")}">
<meta property="og:description" content="{th("doc_desc")}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE_URL}img/neofit.webp">
{f'<meta property="og:url" content="{SITE_URL}">' + chr(10) + f'<link rel="canonical" href="{SITE_URL}">' if SITE_URL else ''}
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%2315171a'/%3E%3Crect x='7' y='17' width='18' height='6' rx='1' fill='%23d4f53c'/%3E%3Cpath d='M9 9h14M16 9v14' stroke='%23f5f6f3' stroke-width='3.2' stroke-linecap='round'/%3E%3C/svg%3E">
<meta name="theme-color" content="#f5f6f3">
<link rel="preload" href="fonts/anuphan.woff" as="font" type="font/woff" crossorigin>
<style>
{CSS}
</style>
</head>
<body>
<a class="skip" href="#main" data-i18n="skip">{th("skip")}</a>
<p class="sr" id="lang-status" role="status" aria-live="polite"></p>

<header class="topbar">
  <span class="topbar-name" data-i18n="name_short">{th("name_short")}</span>
  <div class="topbar-actions">
    <a class="btn btn-sm" href="mailto:{EMAIL}"><svg class="ico" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12v8H2zM2 4l6 5 6-5"/></svg><span data-i18n="email_short">{th("email_short")}</span></a>
    <div class="lang" role="group" aria-label="{th("lang_label")}" data-i18n-aria="lang_label">
      <button type="button" data-lang="th" lang="th" aria-pressed="true">ไทย</button>
      <button type="button" data-lang="en" lang="en" aria-pressed="false" aria-label="English">EN</button>
    </div>
  </div>
</header>

<div class="shell">
  <aside class="intro">
    <div class="intro-inner">
      <h1 class="name" data-i18n="name">{th("name")}</h1>
      <p class="role"><mark>Frontend Developer</mark> &amp; <mark>Business Analyst</mark></p>
      <p class="where" data-i18n="where">{th("where")}</p>
      <p class="thesis" data-i18n="thesis">{th("thesis")}</p>
      <p class="avail"><span class="avail-dot" aria-hidden="true"></span><span><span data-i18n="avail">{th("avail")}</span><br><span class="avail-date" data-i18n="avail_date">{th("avail_date")}</span></span></p>
      <div class="actions">
        <a class="btn" href="mailto:{EMAIL}"><svg class="ico" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 4h12v8H2zM2 4l6 5 6-5"/></svg><span data-i18n="cta_email">{th("cta_email")}</span></a>
        {socials}
      </div>
      <p class="mail-line"><span class="mail-text">{EMAIL}</span><button type="button" class="copy-btn copy-mini" data-copy="{EMAIL}" aria-label="{th("copy")}" data-i18n-aria="copy" hidden><svg class="ico ico-copy" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 5h8v8H5zM3 11V3h8"/></svg><svg class="ico ico-check" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5"/></svg></button></p>
      <nav class="nav" aria-label="{th("nav_label")}" data-i18n-aria="nav_label">
        <ul>
          <li><a href="#experience" data-i18n="nav_exp">{th("nav_exp")}</a></li>
          <li><a href="#projects" data-i18n="nav_proj">{th("nav_proj")}</a></li>
          <li><a href="#skills" data-i18n="nav_skills">{th("nav_skills")}</a></li>
          <li><a href="#about" data-i18n="nav_about">{th("nav_about")}</a></li>
          <li><a href="#contact" data-i18n="nav_contact">{th("nav_contact")}</a></li>
        </ul>
      </nav>
      <div class="lang lang-side" role="group" aria-label="{th("lang_label")}" data-i18n-aria="lang_label">
        <button type="button" data-lang="th" lang="th" aria-pressed="true">ไทย</button>
        <button type="button" data-lang="en" lang="en" aria-pressed="false" aria-label="English">EN</button>
      </div>
    </div>
  </aside>

  <main id="main" class="content" tabindex="-1">
    <section id="experience" class="sec" aria-labelledby="exp-h">
      <h2 id="exp-h" data-i18n="exp_h">{th("exp_h")}</h2>
      <div class="job">
        <p class="job-role" data-i18n="exp_role">{th("exp_role")}</p>
        <p class="job-meta" data-i18n="exp_date">{th("exp_date")}</p>
        <p class="lead" data-i18n="exp_lead">{th("exp_lead")}</p>
      </div>
      <div class="pipe-wrap">
        <ol class="pipe" aria-label="{th("pipe_label")}" data-i18n-aria="pipe_label">
{pipeline}
        </ol>
      </div>
      <ol class="works">
{items}
      </ol>
    </section>

    <section id="projects" class="sec" aria-labelledby="proj-h">
      <h2 id="proj-h" data-i18n="proj_h">{th("proj_h")}</h2>

      <article class="feature">
        <div class="feature-shot">
          <img src="img/neofit.webp" srcset="img/neofit-sm.webp 640w, img/neofit.webp 1200w" sizes="(min-width: 1024px) 640px, 100vw" width="1200" height="568" alt="{th("neo_alt")}" data-i18n-alt="neo_alt" loading="lazy" decoding="async">
        </div>
        <h3 data-i18n="neo_t">{th("neo_t")}</h3>
        <p class="meta-line" data-i18n="neo_k">{th("neo_k")}</p>
        <p data-i18n="neo_d">{th("neo_d")}</p>
        <p class="rating" data-i18n="neo_r">{th("neo_r")}</p>
        <p class="stack">React.js · Firebase (Firestore / Auth / Storage) · MediaPipe Hands · Three.js / WebGL</p>
        {ext("https://neofit-jewelry.web.app/", "neo_link")}
      </article>

      <ul class="proj-list">
        <li class="proj">
          <div class="proj-media phones">
            <img src="img/myl-1.webp" width="300" height="537" alt="{th("myl_alt1")}" data-i18n-alt="myl_alt1" loading="lazy" decoding="async">
            <img src="img/myl-2.webp" width="300" height="535" alt="{th("myl_alt2")}" data-i18n-alt="myl_alt2" loading="lazy" decoding="async">
            <img src="img/myl-4.webp" width="300" height="518" alt="{th("myl_alt3")}" data-i18n-alt="myl_alt3" loading="lazy" decoding="async">
          </div>
          <div class="proj-text">
            <h3 data-i18n="myl_t">{th("myl_t")}</h3>
            <p class="meta-line" data-i18n="myl_k">{th("myl_k")}</p>
            <p data-i18n="myl_d">{th("myl_d")}</p>
          </div>
        </li>
        <li class="proj">
          <div class="proj-media"><img src="img/stock.webp" width="900" height="431" alt="{th("stock_alt")}" data-i18n-alt="stock_alt" loading="lazy" decoding="async"></div>
          <div class="proj-text">
            <h3 data-i18n="stock_t">{th("stock_t")}</h3>
            <p class="meta-line" data-i18n="personal">{th("personal")}</p>
            <p data-i18n="stock_d">{th("stock_d")}</p>
          </div>
        </li>
        <li class="proj">
          <div class="proj-media"><img src="img/charites.webp" width="900" height="433" alt="{th("char_alt")}" data-i18n-alt="char_alt" loading="lazy" decoding="async"></div>
          <div class="proj-text">
            <h3 data-i18n="char_t">{th("char_t")}</h3>
            <p class="meta-line" data-i18n="personal">{th("personal")}</p>
            <p data-i18n="char_d">{th("char_d")}</p>
          </div>
        </li>
      </ul>
    </section>

    <section id="skills" class="sec" aria-labelledby="skills-h">
      <h2 id="skills-h" data-i18n="skills_h">{th("skills_h")}</h2>
      <dl class="skills">
{skills}
      </dl>
    </section>

    <section id="about" class="sec" aria-labelledby="about-h">
      <h2 id="about-h" data-i18n="about_h">{th("about_h")}</h2>
      <p class="about" data-i18n="about_p">{th("about_p")}</p>
      <h3 class="sub-h" data-i18n="certs_h">{th("certs_h")}</h3>
      <ul class="certs">
{certs}
      </ul>
    </section>

    <section id="contact" class="sec contact" aria-labelledby="contact-h">
      <h2 id="contact-h" data-i18n="contact_h">{th("contact_h")}</h2>
      <p class="lead" data-i18n="contact_p">{th("contact_p")}</p>
      <div class="mail-row">
        <a class="mail-big" href="mailto:{EMAIL}">{EMAIL}</a>
        <button type="button" class="copy-btn" data-copy="{EMAIL}" hidden><svg class="ico ico-copy" viewBox="0 0 16 16" aria-hidden="true"><path d="M5 5h8v8H5zM3 11V3h8"/></svg><svg class="ico ico-check" viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5"/></svg><span data-i18n="copy">{th("copy")}</span></button>
      </div>
      <p class="copy-status" role="status" aria-live="polite"></p>
      <p class="contact-meta"><span data-i18n="phone">{th("phone")}</span> <a class="text-link" href="tel:{PHONE_TEL}" data-i18n="phone_num">{th("phone_num")}</a> {socials}</p>
    </section>

    <footer class="foot"><p data-i18n="foot">{th("foot")}</p></footer>
  </main>
</div>

<script>
const LINKS = {json.dumps(LINKS)};
const I18N = {I18N_JSON};
{JS}
</script>
</body>
</html>
"""
OUT.write_text(page, encoding="utf-8")
print("wrote", OUT, len(page.encode()), "bytes")
