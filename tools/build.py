#!/usr/bin/env python3
"""Builds the five static pages of The Beacon Centre site into OUT."""
import os, sys, shutil, html

OUT = sys.argv[1]
SRC = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(OUT, "assets/css"), exist_ok=True)
os.makedirs(os.path.join(OUT, "assets/js"), exist_ok=True)
shutil.copy(os.path.join(SRC, "style.css"), os.path.join(OUT, "assets/css/style.css"))
shutil.copy(os.path.join(SRC, "main.js"), os.path.join(OUT, "assets/js/main.js"))

WA = "https://wa.me/2348181057549?text=Hello%2C%20I%27d%20like%20to%20book%20a%20session."
EMAIL = "beaconwellnesscentre@gmail.com"
IG = "https://www.instagram.com/thebeaconcentre.co"
ARROW = '<span class="arr" aria-hidden="true">→</span>'

NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("resources.html", "Resources")]

def head(title, desc, page):
    return f"""<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#C87C78">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="canonical" href="https://beaconcentreglobal.com/{'' if page == 'index.html' else page}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><symbol id="sp" viewBox="0 0 24 24"><path fill="currentColor" d="M12 0c0 7 5 12 12 12-7 0-12 5-12 12 0-7-5-12-12-12 7 0 12-5 12-12z"/></symbol></svg>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="index.html" aria-label="The Beacon Centre, home"><img src="assets/img/wordmark.png" alt="The Beacon Centre" width="170" height="52"></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {''.join(f'<a href="{h}"' + (' aria-current="page"' if h == page else '') + f'>{t}</a>' for h, t in NAV)}
      <a class="btn sm" href="book.html">Book a session {ARROW}</a>
    </nav>
  </div>
</header>
<main id="main">
"""

def foot():
    return f"""</main>
<div class="quick"><a class="btn" href="{WA}" target="_blank" rel="noopener">Book on WhatsApp {ARROW}</a></div>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="assets/img/wordmark.png" alt="The Beacon Centre">
        <p>Counselling and therapy for people who are ready to heal, find clarity and feel whole again.</p>
      </div>
      <div><h5>Explore</h5><ul>
        <li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li>
        <li><a href="resources.html">Resources</a></li><li><a href="book.html">Book a session</a></li></ul></div>
      <div><h5>Talk to us</h5><ul>
        <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
        <li><a href="tel:+2348181057549">0818 105 7549</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul></div>
      <div><h5>Hours</h5><ul>
        <li>9am – 6pm</li><li>Online sessions</li><li>In person on request</li>
        <li><a href="{IG}" target="_blank" rel="noopener">@thebeaconcentre.co</a></li></ul></div>
    </div>
    <div class="legal">
      <span>© <span id="yr">2026</span> The Beacon Centre. Healing · Clarity · Wholeness.</span>
      <span>We are not an emergency service. If you are in immediate danger, contact your local emergency services (in Nigeria, 112).</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""

def spark(cls=""):
    return f'<svg class="spark {cls}" aria-hidden="true"><use href="#sp"/></svg>'

def marquee(items):
    unit = "".join(f'<span>{t}<svg aria-hidden="true"><use href="#sp"/></svg></span>' for t in items)
    return f'<div class="marquee" aria-hidden="true"><div class="marquee-track">{unit*4}</div></div>'

TICKER = ["Healing", "Clarity", "Wholeness", "Online sessions", "In person on request", "Trauma-informed", "CBT-based", "Fully confidential"]

def mosaic(a, b, c):
    return f'''<div class="mosaic">
  <figure class="m1 rv"><img src="assets/img/{a[0]}" alt="{a[1]}" loading="lazy"><figcaption>{a[2]}</figcaption></figure>
  <figure class="m2 rv d1"><img src="assets/img/{b[0]}" alt="{b[1]}" loading="lazy"><figcaption>{b[2]}</figcaption></figure>
  <figure class="m3 rv d2"><img src="assets/img/{c[0]}" alt="{c[1]}" loading="lazy"><figcaption>{c[2]}</figcaption></figure>
</div>'''

MOS = mosaic(("michelle-listening.jpg", "Michelle seated at a café table, looking on attentively", "Listening first"),
             ("michelle-writing.jpg", "Michelle leaning in over a table, writing", "Unhurried, practical, yours"),
             ("michelle-speaking.jpg", "Michelle speaking at an event with a microphone", "Honest conversations"))

SPIN = f'<a class="spin" href="{WA}" target="_blank" rel="noopener" aria-label="Book a session on WhatsApp"><svg viewBox="0 0 120 120" aria-hidden="true"><defs><path id="circ" d="M60 60m-47 0a47 47 0 1 1 94 0a47 47 0 1 1-94 0"/></defs><text><textPath href="#circ" textLength="292" lengthAdjust="spacing">Book a session · Healing · Clarity · Wholeness ·</textPath></text></svg><span class="arw">→</span></a>'

RING = '<svg viewBox="0 0 220 90" preserveAspectRatio="none" aria-hidden="true"><path pathLength="1" d="M14 48C6 16 92 4 132 6c60 2 84 26 76 48-8 26-86 32-136 28C26 78 4 62 18 38"/></svg>'

def faq(items):
    out = '<div class="faq">'
    for i, (q, a) in enumerate(items):
        out += f'<details class="rv" {"open" if i == 0 else ""}><summary>{q}</summary><div class="ans">{a}</div></details>'
    return out + "</div>"

FAQS = [
    ("How do I know if I need therapy?",
     "<p>You don’t have to be falling apart to need therapy. If you feel overwhelmed, stuck, anxious, emotionally heavy, constantly overthinking, grieving, or caught in patterns you can’t seem to break, therapy can help.</p><p>You can also come because you want clarity, growth, or someone steady to think out loud with.</p>"),
    ("What happens in the first session?",
     "<p>The first session is about understanding you. We build rapport, talk through confidentiality, explore your background and the challenges you’re facing now, and what you hope will change.</p>"),
    ("Is what I say kept private?",
     "<p>Yes. Everything shared in session is confidential and handled professionally. The only exceptions are rare legal or safety situations, and those will always be explained to you clearly.</p>"),
    ("How long does therapy last?",
     "<p>There’s no one-size-fits-all timeline. Some people come for short-term work (around 6 to 8 sessions). Others stay longer, depending on their goals. We review your progress together and decide what works best for you.</p>"),
    ("Are sessions online or in person?",
     "<p>Sessions are held online by Zoom, Google Meet or WhatsApp video, whichever is easiest for you. In-person sessions are available on request. Online therapy is just as structured and intentional as meeting face to face, and we welcome clients outside Nigeria too.</p>"),
    ("What approach do you use?",
     "<ul><li>Trauma-informed</li><li>CBT-based (Cognitive Behavioural Therapy)</li><li>Faith-integrated, when appropriate and requested</li></ul>"),
    ("Do you only work with women?",
     "<p>No. The Beacon Centre serves individuals, couples, groups, leaders and organisations. Therapy is for anyone ready to grow, heal and gain clarity.</p>"),
    ("What if I’ve tried therapy before and it didn’t work?",
     "<p>Sometimes the issue isn’t therapy itself. The relationship between you and your therapist matters a great deal. If you’re willing to try again, we can build a clearer, more intentional path forward.</p>"),
    ("How do I book?",
     f"<p>The quickest way is to <a href=\"{WA}\" target=\"_blank\" rel=\"noopener\"><u>message us on WhatsApp</u></a>. You can also use the <a href=\"book.html\"><u>booking page</u></a> or email <a href=\"mailto:{EMAIL}\"><u>{EMAIL}</u></a>. Once you reach out, we’ll guide you through the next steps.</p>"),
]

SERVICES = [
    ("Individual therapy & counselling", "individual",
     "One-to-one sessions with a trained CBT therapist, at your pace.",
     ["Anxiety and stress", "Depression and emotional distress", "Trauma recovery", "Grief and loss", "Identity and self-esteem",
      "Life transitions and personal growth", "Emotional regulation", "Addiction and behavioural challenges", "Burnout and work-related stress"],
     "Anyone who feels overwhelmed, stuck or emotionally heavy, or who simply wants clarity and room to grow.",
     "Online sessions of 60 minutes by Zoom, Google Meet or WhatsApp video. In person on request."),
    ("Couples & relationship counselling", "couples",
     "Space for two people to be heard, and to build something steadier together.",
     ["Premarital counselling", "Marital counselling", "Relationship challenges", "Communication and conflict resolution", "Marriage check-ups"],
     "Couples preparing for marriage, married couples, and partners facing difficult seasons.",
     "Online sessions of 60 minutes. In person on request."),
    ("Group therapy & support", "groups",
     "Healing alongside others who understand what you’re carrying.",
     ["Grief support groups", "Emotional healing groups", "Relationship and marriage groups", "Personal growth groups"],
     "People who find strength in shared experience.",
     "Format and dates are shared when a group opens. Ask us to be notified."),
    ("Corporate mental health & workplace wellness", "corporate",
     "Practical mental-health support for teams and the people who lead them.",
     ["Employee counselling and support", "Workplace mental health programmes", "Stress and burnout management",
      "Emotional intelligence training", "Leadership wellbeing programmes", "Employee wellness seminars"],
     "Organisations, leaders and HR teams who want healthier, steadier workplaces.",
     "Shaped around your organisation. Tell us what you need and we’ll propose a plan."),
    ("Workshops, training & masterclasses", "workshops",
     "Learning that you can use the same week.",
     ["Emotional healing and self-awareness", "Trauma awareness and recovery", "CBT-based practical workshops",
      "Emotional intelligence", "Personal development", "Relationship and marriage enrichment"],
     "Individuals, churches, communities and organisations.",
     "Delivered online or in person, depending on the event."),
    ("Specialised healing programmes", "programmes",
     "Structured programmes for specific areas of healing.",
     [], "People who want focused, time-bound support on one area of their life.",
     "Details are shared on request."),
    ("Speaking & facilitation", "speaking",
     "Michelle is available to speak, facilitate and host.",
     ["Keynote speaking", "Conference speaking", "Panel discussions", "Workshop facilitation", "Retreat facilitation", "Corporate and organisational engagements"],
     "Event organisers, churches, companies and communities.",
     "Share the date, audience and theme and we’ll come back to you."),
]

pages = {}

# ---------------- HOME ----------------
home = head("The Beacon Centre | Counselling & Therapy",
            "Online counselling and therapy with CBT-trained therapist Michelle Tobi-Adesanya. Healing, clarity and wholeness, at your pace.", "index.html")
home += f"""
<section class="hero stage">
  <div class="wrap hero-grid">
    <div class="stage-copy">
      <span class="eyebrow rv">Counselling &amp; therapy · online</span>
      <h1 class="rv d1">You don’t have to be falling apart to <span class="ring">need therapy.{RING}</span></h1>
      <p class="lede rv d2">Overwhelmed, stuck, grieving, or tired of repeating the same patterns? Talk it through with a trained CBT therapist, in a space that’s private, unhurried and entirely yours.</p>
      <div class="cta-row rv d3">
        <a class="btn" href="{WA}" target="_blank" rel="noopener">Book a session {ARROW}</a>
        <a class="btn ghost" href="#how">How it works</a>
      </div>
      <div class="trust rv d3">
        <span>ADI-trained professional counsellor</span><span>CBT-trained therapist</span><span>Fully confidential</span>
      </div>
    </div>
    <figure class="frame rv d2">
      <div class="ph"><img src="assets/img/michelle-hero.jpg" alt="Michelle Tobi-Adesanya, counsellor and CBT therapist" width="1100" height="1375" fetchpriority="high"></div>
      <span class="chip"><i></i>Sessions open · 9am – 6pm</span>
    </figure>
  </div>
</section>
{marquee(TICKER)}

<section class="sec blush curve-top">
  <div class="wrap split">
    <div>
      <span class="eyebrow rv">Who this space is for</span>
      <h2 class="rv" style="margin-top:1rem">Come as you are. <em>Come as you’re able.</em></h2>
      <p class="lede rv">The Beacon Centre offers structured, professional support at every level of need: personal, relational and organisational.</p>
    </div>
    <div>
      <div class="pills rv" aria-label="Reasons people come to therapy">
        <span class="pill">Overwhelmed</span><span class="pill">Stuck</span><span class="pill">Anxious</span>
        <span class="pill">Emotionally heavy</span><span class="pill">Overthinking</span><span class="pill">Grieving</span>
        <span class="pill">Repeating old patterns</span><span class="pill">Wanting clarity</span><span class="pill">Ready to grow</span>
      </div>
      <p class="muted rv">Some people arrive in the middle of a storm. Others arrive because life looks fine and something still feels off. Both are good reasons.</p>
    </div>
  </div>
</section>

<section class="sec" id="services">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow rv">How we can help</span>
      <h2 class="rv">Support that fits where you are.</h2>
    </div>
    <div class="svc-list">
"""
for i, (name, anchor, short, *_rest) in enumerate(SERVICES, 1):
    home += f'<a class="svc rv" href="services.html#{anchor}"><span class="n">{i:02d}</span><div><h3>{name}</h3><p>{short}</p></div><span class="go">Read more →</span></a>\n'
home += f"""
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow rv">The room you’ll step into</span>
      <h2 class="rv">A steady presence, not a lecture.</h2>
      <p class="lede rv">Sessions are conversations. Michelle listens first, then brings practical, proven tools to help you move from confusion to clarity.</p>
    </div>
    {MOS}
  </div>
</section>

<section class="sec blush" id="how">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow rv">How it works</span>
      <h2 class="rv">Three steps, no pressure.</h2>
    </div>
    <div class="steps">
      <div class="step rv"><h3>Say hello</h3><p>Send a message on WhatsApp or by email. Tell us a little about what’s going on, and we’ll guide you from there.</p></div>
      <div class="step rv d1"><h3>A first session to understand you</h3><p>We build rapport, talk through confidentiality, and explore your background, what’s hard right now and what you hope will change.</p></div>
      <div class="step rv d2"><h3>Plan it together</h3><p>Some people need around 6 to 8 sessions, others longer. We review your progress as we go and decide what’s working.</p></div>
    </div>
  </div>
</section>

<section class="sec rose-bg curve-top">
  <div class="wrap profile">
    <div class="bio-photo arch-top rv"><div class="ph"><img src="assets/img/michelle-portrait.jpg" alt="Michelle Tobi-Adesanya, counsellor and CBT-trained therapist" loading="lazy"></div></div>
    <div>
      <span class="eyebrow rv">Your therapist</span>
      <p class="quote rv">I combine empathy with practical professional tools to help you find clarity, heal deeply, and grow into the best version of yourself.</p>
      <p class="cite rv">Michelle Tobi-Adesanya</p>
      <div class="creds rv"><span>Professional counsellor, ADI</span><span>CBT-trained therapist</span><span>Trauma-informed</span><span>Faith-sensitive on request</span></div>
      <p class="rv" style="margin-top:1.8rem"><a class="btn light" href="about.html">Read more about Michelle {ARROW}</a></p>
    </div>
  </div>
</section>

<section class="statement">
  {spark("lg a")}{spark("b")}
  <div class="wrap"><p class="rv">Somewhere to set it all down, and <em>be heard.</em></p></div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow rv">Fees</span>
      <h2 class="rv">Clear prices, up front.</h2>
      <p class="lede rv">Sessions are 60 minutes. Packages are paid together and give you a steady rhythm of support.</p>
    </div>
    <div class="ledger">
      <div class="card rv"><h3>One-to-one</h3><p class="sub">Individual counselling</p>
        <div class="row"><span>Single 60-minute session</span><b>₦75,000</b></div>
        <div class="row"><span>4 sessions</span><b>₦250,000</b></div>
        <div class="row"><span>6 sessions</span><b>₦350,000</b></div>
        <div class="row"><span>8 sessions</span><b>₦450,000</b></div>
        <div class="row"><span>10 sessions</span><b>₦550,000</b></div></div>
      <div class="card rv d1"><h3>Couples</h3><p class="sub">Premarital and marital counselling</p>
        <div class="row"><span>6 sessions · Essential</span><b>₦450,000</b></div>
        <p class="note">For couples who want to address the major foundations of marriage.</p>
        <div class="row"><span>8 sessions · Comprehensive</span><b>₦550,000</b></div>
        <p class="note">For deeper conversations and practical preparation.</p>
        <div class="row"><span>10 sessions · Intensive</span><b>₦650,000</b></div>
        <p class="note">For more thorough assessment, significant areas of disagreement, or extra support.</p></div>
    </div>
    <p class="fine rv">Group therapy, corporate programmes, workshops and speaking are quoted on request.</p>
  </div>
</section>

<section class="sec blush">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow rv">Good to know</span><h2 class="rv">Questions people ask before they book.</h2></div>
    {faq(FAQS[:6])}
    <p class="rv" style="margin-top:1.6rem"><a href="book.html#faq" class="btn ghost sm">More questions {ARROW}</a></p>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <span class="eyebrow rv">Ready when you are</span>
    <h2 class="rv">Healing starts with one message.</h2>
    <p class="lede rv">Tell us a little about what’s going on. We’ll reply during working hours (9am – 6pm) and guide you through the next step.</p>
    <div class="cta-row rv"><a class="btn" href="{WA}" target="_blank" rel="noopener">Book on WhatsApp {ARROW}</a><a class="btn ghost" href="book.html">Other ways to reach us</a></div>
  </div>
</section>
""" + foot()
pages["index.html"] = home

# ---------------- ABOUT ----------------
about = head("About | The Beacon Centre", "Meet Michelle Tobi-Adesanya and learn how The Beacon Centre works: warm, structured, trauma-informed and CBT-based.", "about.html")
about += f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow rv">About The Beacon Centre</span>
  <h1 class="rv d1">A steady light for when things feel unclear.</h1>
  <p class="lede rv d2">The Beacon Centre is a therapy and counselling practice built around three ideas: healing, clarity and wholeness. We offer structured, professional support for individuals, couples, groups, leaders and organisations.</p>
</div></section>

<section class="sec" style="padding-top:2rem">
  <div class="wrap profile">
    <div class="bio-photo rv"><div class="ph"><img src="assets/img/michelle-portrait.jpg" alt="Michelle Tobi-Adesanya, counsellor and CBT-trained therapist" loading="lazy"></div></div>
    <div>
      <span class="eyebrow rv">Meet your therapist</span>
      <h2 class="rv" style="margin:1rem 0 1.2rem">Michelle Tobi-Adesanya</h2>
      <p class="rv">Michelle is an emotional healing and growth specialist, professional counsellor and CBT-trained therapist, whose work is dedicated to helping people find healing, purpose and wholeness. She trained as a professional counsellor at ADI.</p>
      <p class="rv" style="margin-top:1rem">What sets her apart is the way she brings faith-based principles together with evidence-based strategies, creating a safe space where people feel seen, heard and empowered. In her own words, she combines empathy with practical professional tools, so you can find clarity, heal deeply and grow into the best version of yourself.</p>
      <p class="rv" style="margin-top:1rem">Her work spans children, teenagers and adults, walking with them through seasons of transition, healing and self-discovery. She is also the founder of <a href="https://creatorshavenglobal.com" target="_blank" rel="noopener"><u>Creators Haven Global</u></a>.</p>
      <p class="rv" style="margin-top:1rem">In session, you can expect a safe, respectful and non-judgemental space where you can be honest, feel heard, and take the steps toward healing and growth at your own pace.</p>
      <div class="creds rv"><span>Professional counsellor, ADI</span><span>CBT-trained therapist</span></div>
      <p class="rv" style="margin-top:1.8rem"><a class="btn" href="{WA}" target="_blank" rel="noopener">Book a session with Michelle {ARROW}</a></p>
    </div>
  </div>
</section>

<section class="sec" style="padding-bottom:0"><div class="wrap">{MOS}</div></section>

<section class="sec blush" style="margin-top:4rem">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow rv">Our approach</span><h2 class="rv">Insight, with tools you can actually use.</h2>
      <p class="lede rv">We combine professional psychological insight with emotional depth and practical, proven tools, to help you move from confusion to clarity, and from clarity to purposeful living.</p></div>
    <div class="steps">
      <div class="step rv"><h3>Trauma-informed</h3><p>We pay attention to what has happened to you, not only what’s happening now, and we go at a pace that feels safe.</p></div>
      <div class="step rv d1"><h3>CBT-based</h3><p>Cognitive Behavioural Therapy helps you notice the thoughts and patterns that keep you stuck, and practise new ones.</p></div>
      <div class="step rv d2"><h3>Faith-sensitive</h3><p>Where you ask for it and where it’s appropriate, your faith can be part of the conversation. It’s never imposed.</p></div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow rv">What to expect</span><h2 class="rv">Healing · Clarity · Wholeness</h2></div>
    <div class="steps">
      <div class="step rv"><h3>Healing</h3><p>A safe, non-judgemental space where what you’ve carried can finally be said out loud.</p></div>
      <div class="step rv d1"><h3>Clarity</h3><p>A personalised, professional approach that helps you understand yourself and your next step, with progress tracked along the way.</p></div>
      <div class="step rv d2"><h3>Wholeness</h3><p>Growth that lasts, built on confidentiality and trust, at your own pace.</p></div>
    </div>
  </div>
</section>

<section class="sec blush">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow rv">Before we begin</span><h2 class="rv">How sessions work.</h2></div>
    <div class="ledger">
      <div class="card rv"><h3>Format and length</h3><p>Sessions are typically 60 minutes. They’re held online by Zoom, Google Meet or WhatsApp video, whichever is most comfortable for you. Michelle always makes sure her end is private and safe. In-person sessions are available on request.</p><p style="margin-top:.8rem">Some things take more than one session. When that happens, we agree on a plan that supports your healing, whether that means booking more sessions or shaping a plan around your life.</p></div>
      <div class="card rv d1"><h3>Rescheduling</h3><p>Please let us know at least 24 hours before your session if you need to reschedule. Life happens. Late cancellations (under 24 hours) attract a 50% fee, and a missed session without notice counts as used.</p><h3 style="margin-top:1.4rem">Confidentiality</h3><p>Everything you share stays private, except where there’s a risk of harm to you or others, where the law requires disclosure, or where you give written consent.</p></div>
    </div>
    <p class="fine rv">If your needs would be better met by another professional, Michelle will tell you and refer you appropriately. Counselling is only offered within her area of training and expertise.</p>
  </div>
</section>

<section class="band"><div class="wrap">
  <span class="eyebrow rv">Start gently</span>
  <h2 class="rv">If you’re wondering whether this is for you, it probably is.</h2>
  <div class="cta-row rv"><a class="btn" href="{WA}" target="_blank" rel="noopener">Message us on WhatsApp {ARROW}</a><a class="btn ghost" href="services.html">See our services</a></div>
</div></section>
""" + foot()
pages["about.html"] = about

# ---------------- SERVICES ----------------
sv = head("Services | The Beacon Centre", "Individual and couples counselling, group support, corporate wellness, workshops, specialised programmes and speaking.", "services.html")
sv += f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow rv">Services</span>
  <h1 class="rv d1">Find the right kind of support.</h1>
  <p class="lede rv d2">Not sure where you fit? Start with one-to-one counselling or message us. We’ll help you work out the right place to begin.</p>
</div></section>
<section class="sec" style="padding-top:0"><div class="wrap">{MOS}</div></section>
<section class="sec" style="padding-top:1rem"><div class="wrap">
"""
for i, (name, anchor, short, topics, who, how) in enumerate(SERVICES, 1):
    price = ""
    if anchor == "individual":
        price = '<h4>Fees</h4><div class="row"><span>60-minute session</span><b>₦75,000</b></div><div class="row"><span>4 sessions</span><b>₦250,000</b></div><div class="row"><span>6 sessions</span><b>₦350,000</b></div><div class="row"><span>8 sessions</span><b>₦450,000</b></div><div class="row"><span>10 sessions</span><b>₦550,000</b></div>'
    elif anchor == "couples":
        price = '<h4>Fees</h4><div class="row"><span>6 sessions · Essential</span><b>₦450,000</b></div><p class="note">For couples who want to address the major foundations of marriage.</p><div class="row"><span>8 sessions · Comprehensive</span><b>₦550,000</b></div><p class="note">For deeper conversations and practical preparation.</p><div class="row"><span>10 sessions · Intensive</span><b>₦650,000</b></div><p class="note">For more thorough assessment, significant areas of disagreement, or extra support.</p>'
    else:
        price = '<h4>Fees</h4><p class="muted">Quoted on request.</p>'
    topics_html = ("<h4>What it can help with</h4><ul>" + "".join(f"<li>{t}</li>" for t in topics) + "</ul>") if topics else ""
    sv += f"""<article class="svc-block" id="{anchor}">
  <div class="sticky rv"><span class="num">{i:02d}</span><h2>{name}</h2><p class="muted">{short}</p></div>
  <div class="rv d1">
    <h4 style="margin-top:0">Who it’s for</h4><p>{who}</p>
    {topics_html}
    <h4>How it works</h4><p>{how}</p>
    {price}
    <div class="cta-row"><a class="btn" href="{WA}" target="_blank" rel="noopener">{'Book a session' if anchor in ('individual','couples') else 'Make an enquiry'} {ARROW}</a></div>
  </div>
</article>
"""
sv += """</div></section>
<section class="band"><div class="wrap">
  <span class="eyebrow rv">Not sure which?</span>
  <h2 class="rv">Tell us what’s going on and we’ll point you the right way.</h2>
  <div class="cta-row rv"><a class="btn" href="book.html">Make an enquiry """ + ARROW + """</a></div>
</div></section>
""" + foot()
pages["services.html"] = sv

# ---------------- RESOURCES ----------------
rs = head("Resources | The Beacon Centre", "Gentle, practical reading on therapy and emotional wellbeing from The Beacon Centre.", "resources.html")
rs += f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow rv">Resources</span>
  <h1 class="rv d1">Something to hold on to between sessions.</h1>
  <p class="lede rv d2">Our guides, worksheets and articles are on their way. Until they’re ready, here’s where to start.</p>
</div></section>

<section class="sec" style="padding-top:1rem"><div class="wrap split">
  <div>
    <span class="eyebrow rv">Start here</span>
    <h2 class="rv" style="margin:1rem 0 1.2rem">How do I know if I need therapy?</h2>
    <p class="rv">You don’t have to be falling apart. If you feel overwhelmed, stuck, anxious, emotionally heavy, constantly overthinking, grieving, or repeating patterns you can’t seem to break, therapy can help.</p>
    <p class="rv" style="margin-top:1rem">You can also come into therapy because you want clarity, growth or emotional support.</p>
    <p class="rv" style="margin-top:1.8rem"><a class="btn ghost" href="{IG}" target="_blank" rel="noopener">Read more on Instagram {ARROW}</a></p>
  </div>
  <div class="card rv d1">
    <h3>Be the first to know</h3>
    <p class="sub">We’ll write to you when new resources are ready. No spam, and you can leave whenever you like.</p>
    <form class="form" id="signup">
      <div class="field"><label for="su-email">Email address</label><input id="su-email" name="email" type="email" required autocomplete="email" placeholder="you@example.com"></div>
      <label class="check"><input type="checkbox" name="consent" required><span>I’d like to receive occasional emails from The Beacon Centre, and I understand I can unsubscribe at any time.</span></label>
      <button class="btn" type="submit">Keep me posted {ARROW}</button>
    </form>
  </div>
</div></section>

<section class="sec blush"><div class="wrap">
  <div class="sec-head"><span class="eyebrow rv">Common questions</span><h2 class="rv">What people often want to know.</h2></div>
  {faq(FAQS)}
</div></section>
""" + foot()
pages["resources.html"] = rs

# ---------------- BOOK ----------------
bk = head("Book a Session | The Beacon Centre", "Book a counselling or therapy session at The Beacon Centre by WhatsApp, email or enquiry form.", "book.html")
bk += f"""
<section class="page-hero"><div class="wrap">
  <span class="eyebrow rv">Book a session</span>
  <h1 class="rv d1">Take the first step. We’ll take it from there.</h1>
  <p class="lede rv d2">The fastest way to book is WhatsApp. If you’d rather write properly, use the form or send an email.</p>
</div></section>

<section class="sec" style="padding-top:1rem"><div class="wrap contact-grid">
  <div>
    <div class="wa-card rv">
      <span class="eyebrow">Quickest</span>
      <h2>Message us on WhatsApp</h2>
      <p>Say hello and tell us roughly what you’d like help with. We’ll reply during working hours and suggest a time.</p>
      <a class="btn light" href="{WA}" target="_blank" rel="noopener">Open WhatsApp {ARROW}</a>
    </div>
    <dl class="info rv">
      <div><dt>WhatsApp</dt><dd><a href="{WA}" target="_blank" rel="noopener">0818 105 7549</a></dd></div>
      <div><dt>Call</dt><dd><a href="tel:+2348181057549">0818 105 7549</a></dd></div>
      <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
      <div><dt>Hours</dt><dd>9am – 6pm</dd></div>
      <div><dt>Sessions</dt><dd>Online by Zoom, Google Meet or WhatsApp video. In person on request. Clients outside Nigeria are welcome.</dd></div>
      <div><dt>Instagram</dt><dd><a href="{IG}" target="_blank" rel="noopener">@thebeaconcentre.co</a></dd></div>
    </dl>
  </div>
  <div class="card rv d1">
    <h3>Prefer to write it down?</h3>
    <p class="sub">Share a little. You choose whether it goes to us by WhatsApp or email. Nothing is stored on this website.</p>
    <form class="form" id="enquiry" onsubmit="return false">
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-email">Email (only needed if you’re sending by email)</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
      <div class="field"><label for="f-service">What are you interested in?</label>
        <select id="f-service" name="service"><option value="">Not sure yet</option>
          <option>Individual counselling</option><option>Couples counselling</option><option>Group therapy</option>
          <option>Corporate wellness</option><option>Workshop or training</option><option>Specialised healing programme</option><option>Speaking or facilitation</option></select></div>
      <div class="field"><label for="f-when">When suits you best?</label><input id="f-when" name="when" placeholder="e.g. weekday evenings"></div>
      <div class="field"><label for="f-note">Anything you’d like us to know? (optional)</label><textarea id="f-note" name="note"></textarea></div>
      <div class="cta-row"><button class="btn" type="button" id="send-wa">Send by WhatsApp {ARROW}</button><button class="btn ghost" type="button" id="send-mail">Send by email</button></div>
    </form>
  </div>
</div></section>

<section class="sec blush"><div class="wrap split" style="align-items:start">
  <div><span class="eyebrow rv">What happens next</span><h2 class="rv" style="margin:1rem 0">No forms to fight with.</h2>
    <p class="lede rv">Once you reach out, we’ll reply in working hours, agree a time with you, and send the link for your session. Your first session is about understanding you.</p></div>
  <div class="card rv d1"><h3>Good to know</h3>
    <div class="row"><span>Session length</span><b>60 min</b></div>
    <div class="row"><span>Reschedule notice</span><b>24 hours</b></div>
    <p class="fine">Late cancellations (under 24 hours) attract a 50% fee, and a missed session without notice counts as used.</p></div>
</div></section>

<section class="sec" id="faq"><div class="wrap">
  <div class="sec-head"><span class="eyebrow rv">Questions</span><h2 class="rv">Before you book.</h2></div>
  {faq(FAQS)}
</div></section>
""" + foot()
pages["book.html"] = bk

for name, content in pages.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(content)
print("built", list(pages))
