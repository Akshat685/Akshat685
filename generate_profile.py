#!/usr/bin/env python3
"""Generate v3 animated GitHub profile SVGs - redesigned layout matching reference."""
import os, random
DIR = os.path.dirname(os.path.abspath(__file__))
random.seed(42)

with open(os.path.join(DIR, 'char_full_b64.txt')) as f:
    CHAR_B64 = f.read().strip()
with open(os.path.join(DIR, 'char_face_b64.txt')) as f:
    FACE_B64 = f.read().strip()

# ═══════════════════════════════════════════════════════════
#  BANNER (1280x850) — Reference-matched layout
# ═══════════════════════════════════════════════════════════
def banner_svg(theme='dark'):
    H = 850
    # -- Colors --
    if theme == 'dark':
        bg1,bg2,bg3='#0d0221','#130730','#1a0a3e'
        tx='#e2e8f0'; txb='#f8fafc'; txd='#94a3b8'; txdd='#64748b'
        tg='#4ade80'; tp='#c084fc'
        cbg='#0f0825'; cbd='#4c1d95'; chd='#1a0e3a'
        pbg='rgba(124,58,237,0.10)'; pbo='0.35'; ptx='#c4b5fd'
        qbg='rgba(192,38,211,0.06)'; qbd='#c026d3'
        sbb='rgba(255,255,255,0.06)'; nt='#f9a8d4'
        eln='#4c1d95'; fr='#c026d3'
        pc=['#c084fc','#f9a8d4','#a78bfa','#818cf8']
        hc='#f472b6'; sc='#fbbf24'
        oc=['rgba(139,92,246,0.12)','rgba(192,38,211,0.10)','rgba(124,58,237,0.08)']
        stat_card='rgba(124,58,237,0.06)'; stat_border='rgba(76,29,149,0.4)'
        contact_bg='rgba(13,2,33,0.6)'; dots_color='#7c3aed'
    else:
        bg1,bg2,bg3='#f8fafc','#f1f5f9','#ede9fe'
        tx='#334155'; txb='#1e293b'; txd='#64748b'; txdd='#94a3b8'
        tg='#16a34a'; tp='#7c3aed'
        cbg='#ffffff'; cbd='#c4b5fd'; chd='#f5f3ff'
        pbg='rgba(124,58,237,0.05)'; pbo='0.25'; ptx='#6d28d9'
        qbg='rgba(192,38,211,0.04)'; qbd='#c026d3'
        sbb='rgba(0,0,0,0.04)'; nt='#7c3aed'
        eln='#a78bfa'; fr='#c026d3'
        pc=['#c084fc','#f9a8d4','#a78bfa','#818cf8']
        hc='#f472b6'; sc='#f59e0b'
        oc=['rgba(139,92,246,0.05)','rgba(192,38,211,0.04)','rgba(124,58,237,0.03)']
        stat_card='rgba(124,58,237,0.04)'; stat_border='rgba(196,181,253,0.4)'
        contact_bg='rgba(241,245,249,0.6)'; dots_color='#c4b5fd'

    # ─── Name letters (TWO LINES: "Akshat" + "Shettigar") ───
    name_line1 = "Akshat"
    name_line2 = "Shettigar"
    ns1 = ""
    ns2 = ""
    idx = 0
    for ch in name_line1:
        d = round(1.5 + idx * 0.12, 2)
        ns1 += (f'<tspan opacity="0">{ch}'
                f'<animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{d}s" fill="freeze"/>'
                f'</tspan>')
        idx += 1
    for ch in name_line2:
        d = round(1.5 + idx * 0.12, 2)
        ns2 += (f'<tspan opacity="0">{ch}'
                f'<animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{d}s" fill="freeze"/>'
                f'</tspan>')
        idx += 1

    # ─── Tech pills ───
    skills = [
        ("HTML","#e34f26"),("CSS","#1572b6"),("JavaScript","#f7df1e"),("TypeScript","#3178c6"),("React","#61dafb"),
        ("Next.js","#888" if theme=='light' else "#fff"),("Node.js","#339933"),("GraphQL","#e535ab"),("Tailwind","#06b6d4"),("RAG","#8b5cf6"),
        ("OpenAI","#412991"),("Gemini","#4285f4"),("Vectors","#00d4aa"),("Prompts","#f59e0b"),("LLM","#ef4444")
    ]
    pills = ""
    for i,(sk,cl) in enumerate(skills):
        r,c = i//5, i%5
        x = 42 + c*116; y = 370 + r*35
        dl = round(4.5 + i*0.1, 2)
        pills += (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{dl}s" fill="freeze"/>'
                  f'<rect x="{x}" y="{y}" width="108" height="27" rx="6" fill="{pbg}" stroke="{cl}" stroke-opacity="{pbo}" stroke-width="1.2"/>'
                  f'<text x="{x+54}" y="{y+18}" text-anchor="middle" font-size="13" fill="{ptx}" font-family="Cascadia Code,Fira Code,monospace" font-weight="500">{sk}</text></g>\n')

    # ─── Code editor (positioned top-center) ───
    CE_X, CE_Y, CE_W, CE_H = 510, 38, 265, 255
    code_lines_data = [
        [("#c084fc","function "),("#f9a8d4","buildDreams"),("#94a3b8","() {")],
        [("#94a3b8","&#160;&#160;"),("#c084fc","return"),("#94a3b8"," (")],
        [("#94a3b8","&#160;&#160;&#160;&#160;&lt;div className="),("#a5f3fc","\"dreams\""),("#94a3b8","&gt;")],
        [("#94a3b8","&#160;&#160;&#160;&#160;&#160;&#160;&lt;"),("#f9a8d4","Code"),("#94a3b8"," /&gt;")],
        [("#94a3b8","&#160;&#160;&#160;&#160;&#160;&#160;&lt;"),("#f9a8d4","Coffee"),("#94a3b8"," /&gt;")],
        [("#94a3b8","&#160;&#160;&#160;&#160;&#160;&#160;&lt;"),("#f9a8d4","Repeat"),("#94a3b8"," /&gt;")],
        [("#94a3b8","&#160;&#160;&#160;&#160;&#160;&#160;&lt;"),("#f9a8d4","Success"),("#94a3b8"," /&gt;")],
        [("#94a3b8","&#160;&#160;&#160;&#160;&lt;/div&gt;);")],
        [("#94a3b8","} "),("#64748b","// export default")],
    ]
    editor_svg = ""
    for i,parts in enumerate(code_lines_data):
        yp = CE_Y + 52 + i*22; dl = round(7.5 + i*0.4, 2)
        txt = "".join(f'<tspan fill="{c}">{t}</tspan>' for c,t in parts)
        editor_svg += (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.25s" begin="{dl}s" fill="freeze"/>'
                       f'<text x="{CE_X+18}" y="{yp}" font-size="14" font-family="Cascadia Code,Fira Code,Consolas,monospace" xml:space="preserve">{txt}</text></g>\n')

    # ─── Stats row ───
    stat_items = [
        ("&#128230;","Repos","8+","#4ade80"),
        ("&#128221;","Commits","234+","#60a5fa"),
        ("&#11088;","Stars","15+","#fbbf24"),
        ("&#128101;","Followers","10+","#f472b6"),
    ]
    stats_svg = ""
    col_w = 128
    for i,(em,lb,val,cl) in enumerate(stat_items):
        cx = 42 + 8 + i*col_w + col_w//2
        dl = round(7.0 + i*0.2, 1)
        stats_svg += (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{dl}s" fill="freeze"/>'
                      f'<text x="{cx}" y="641" text-anchor="middle" font-size="11" fill="{txd}" font-family="Segoe UI,sans-serif">{em} {lb}</text>'
                      f'<text x="{cx}" y="673" text-anchor="middle" font-size="26" fill="{cl}" font-weight="bold" font-family="Segoe UI,sans-serif">{val}</text></g>\n')

    # ─── About Me ───
    about_lines = [
        ("&gt;_","I build responsive, user-friendly and impactful web experiences."),
        ("&#128161;","Exploring RAG, LLMs &amp; the future of AI."),
        ("&#9999;","Turning ideas into real world solutions."),
    ]
    about_svg = ""
    for i,(em,ln) in enumerate(about_lines):
        y = 535 + i*26; dl = round(6.2 + i*0.25, 2)
        about_svg += (f'<text x="42" y="{y}" font-size="15" fill="{tx}" opacity="0" font-family="Segoe UI,sans-serif">'
                      f'{em} {ln}<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{dl}s" fill="freeze"/></text>\n')

    # ─── Particles ───
    particles = ""
    for i in range(15):
        px=random.randint(30,1250); py=random.randint(700,H)
        sz=round(random.uniform(1.5,3),1); dur=round(random.uniform(5,9),1)
        dl=round(random.uniform(0,5),1); cl=pc[i%4]
        particles += (f'<circle cx="{px}" cy="{py}" r="{sz}" fill="{cl}" opacity="0">'
                      f'<animate attributeName="cy" from="{py}" to="{py-280}" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/>'
                      f'<animate attributeName="opacity" values="0;0.6;0.4;0" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/></circle>\n')

    # ─── Hearts ───
    hearts = ""
    hpos = [(850,650,5,0.8),(920,700,4.2,2.5),(1000,670,5.5,0.3),(1080,720,4.5,3),(1160,640,5.2,1.5),(780,710,4.8,2)]
    for hx,hy,dur,dl in hpos:
        rise = random.randint(100,180)
        hearts += (f'<g><animateTransform attributeName="transform" type="translate" '
                   f'values="0 0;0 -{rise}" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/>'
                   f'<path d="M{hx},{hy-5} C{hx},{hy-9} {hx-6},{hy-9} {hx-6},{hy-4} '
                   f'C{hx-6},{hy+1} {hx},{hy+5} {hx},{hy+7} C{hx},{hy+5} {hx+6},{hy+1} {hx+6},{hy-4} '
                   f'C{hx+6},{hy-9} {hx},{hy-9} {hx},{hy-5}Z" fill="{hc}" opacity="0">'
                   f'<animate attributeName="opacity" values="0;0.5;0.3;0" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/>'
                   f'</path></g>\n')

    # ─── Sparkles ───
    sparkles = ""
    spos = [(120,80),(500,50),(280,790),(620,810),(1050,760),(1200,500),(70,450),(380,550)]
    for i,(sx,sy) in enumerate(spos):
        dur=round(random.uniform(1.5,3),1); dl=round(random.uniform(0,3),1)
        sparkles += (f'<g transform="translate({sx},{sy})" opacity="0.15">'
                     f'<animate attributeName="opacity" values="0.1;0.8;0.1" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/>'
                     f'<line x1="-4" y1="0" x2="4" y2="0" stroke="{sc}" stroke-width="1.2"/>'
                     f'<line x1="0" y1="-4" x2="0" y2="4" stroke="{sc}" stroke-width="1.2"/></g>\n')

    # ─── Orbs ───
    orbs = ""
    opos = [(160,600,30),(550,80,22),(1050,550,38),(350,780,25)]
    for i,(ox,oy,sz) in enumerate(opos):
        dur=round(random.uniform(3,6),1); dl=round(random.uniform(0,2),1); cl=oc[i%3]
        orbs += (f'<circle cx="{ox}" cy="{oy}" r="{sz}" fill="{cl}" opacity="0.2">'
                 f'<animate attributeName="r" values="{sz};{sz+6};{sz}" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/>'
                 f'<animate attributeName="opacity" values="0.1;0.3;0.1" dur="{dur}s" begin="{dl}s" repeatCount="indefinite"/></circle>\n')

    # ─── Dot grid decoration (top-right) ───
    dots = ""
    for i in range(14):
        for j in range(7):
            dots += f'<rect x="{1050+i*14}" y="{55+j*14}" width="3" height="3" rx="1" fill="{dots_color}" opacity="0.2"/>\n'

    # ─── Character position ───
    CX, CY, CW, CH_IMG = 710, 130, 510, 638

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 1280 {H}" width="1280" height="{H}">
<defs>
  <linearGradient id="bgG" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="{bg1}"/><stop offset="50%" stop-color="{bg2}"/><stop offset="100%" stop-color="{bg3}"/></linearGradient>
  <linearGradient id="nG" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#7c3aed"><animate attributeName="stop-color" values="#7c3aed;#c026d3;#f472b6;#7c3aed" dur="4s" repeatCount="indefinite"/></stop>
    <stop offset="50%" stop-color="#c026d3"><animate attributeName="stop-color" values="#c026d3;#f472b6;#7c3aed;#c026d3" dur="4s" repeatCount="indefinite"/></stop>
    <stop offset="100%" stop-color="#f472b6"><animate attributeName="stop-color" values="#f472b6;#7c3aed;#c026d3;#f472b6" dur="4s" repeatCount="indefinite"/></stop></linearGradient>
  <linearGradient id="slG" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#7c3aed" stop-opacity="0"/><stop offset="40%" stop-color="#a855f7" stop-opacity="0.5"/>
    <stop offset="50%" stop-color="#c084fc" stop-opacity="1"/><stop offset="60%" stop-color="#a855f7" stop-opacity="0.5"/>
    <stop offset="100%" stop-color="#7c3aed" stop-opacity="0"/></linearGradient>
  <filter id="gl"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="ng"><feGaussianBlur stdDeviation="4" result="b"/><feFlood flood-color="{nt}" flood-opacity="0.5" result="c"/>
    <feComposite in="c" in2="b" operator="in" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="sg"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <filter id="cs"><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#7c3aed" flood-opacity="0.25"/></filter>
  <clipPath id="bc"><rect width="1280" height="{H}" rx="16"/></clipPath>
  <clipPath id="hrc"><rect x="{CX}" y="{CY}" width="{CW+20}" height="0">
    <animate attributeName="height" from="0" to="{CH_IMG+20}" dur="2.5s" begin="0.5s" fill="freeze"/></rect></clipPath>
  <clipPath id="tc"><rect x="40" y="22" width="0" height="28">
    <animate attributeName="width" from="0" to="460" dur="2s" begin="0.3s" fill="freeze"/></rect></clipPath>
  <clipPath id="r1c"><rect x="55" y="202" width="0" height="32">
    <animate attributeName="width" values="0;0;290;290;0;0;0;0;0" keyTimes="0;0.02;0.20;0.30;0.33;0.34;0.67;0.68;1" dur="9s" repeatCount="indefinite" begin="3.5s"/></rect></clipPath>
  <clipPath id="r2c"><rect x="55" y="202" width="0" height="32">
    <animate attributeName="width" values="0;0;0;0;0;180;180;0;0;0;0" keyTimes="0;0.33;0.34;0.35;0.36;0.52;0.63;0.66;0.67;0.68;1" dur="9s" repeatCount="indefinite" begin="3.5s"/></rect></clipPath>
  <clipPath id="r3c"><rect x="55" y="202" width="0" height="32">
    <animate attributeName="width" values="0;0;0;0;0;0;0;0;310;310;0" keyTimes="0;0.33;0.34;0.66;0.67;0.68;0.69;0.70;0.86;0.96;1" dur="9s" repeatCount="indefinite" begin="3.5s"/></rect></clipPath>
  <clipPath id="tgc"><rect x="53" y="255" width="0" height="48">
    <animate attributeName="width" from="0" to="340" dur="2s" begin="3.8s" fill="freeze"/></rect></clipPath>
  <pattern id="sl" width="1" height="4" patternUnits="userSpaceOnUse"><rect width="1" height="2" fill="rgba(0,0,0,0.05)"/></pattern>
</defs>
<style>
  @keyframes cb {{ 0%,100% {{ opacity:1; }} 50% {{ opacity:0; }} }}
  @keyframes nf {{ 0% {{ opacity:0; }} 8% {{ opacity:0.8; }} 10% {{ opacity:0.2; }} 12% {{ opacity:0.9; }} 14% {{ opacity:0.3; }} 18% {{ opacity:1; }} 20% {{ opacity:0.6; }} 23% {{ opacity:1; }} 100% {{ opacity:1; }} }}
  .cur {{ animation: cb 1s step-end infinite; }}
  .neo {{ opacity:0; animation: nf 2s ease-out 11s forwards; }}
</style>
<g clip-path="url(#bc)">
  <!-- BG -->
  <rect width="1280" height="{H}" fill="url(#bgG)"/>
  {orbs}

  <!-- Border frame -->
  <rect x="8" y="8" width="1264" height="{H-16}" rx="14" fill="none" stroke="{fr}" stroke-width="1.2" stroke-opacity="0.25"/>

  <!-- Dot grid decoration -->
  {dots}

  <!-- ══════ CHARACTER (drawn first = behind overlays) ══════ -->
  <g clip-path="url(#hrc)" filter="url(#cs)">
    <image href="data:image/png;base64,{CHAR_B64}" xlink:href="data:image/png;base64,{CHAR_B64}"
           x="{CX}" y="{CY}" width="{CW}" height="{CH_IMG}" opacity="0.95"/>
    <rect x="{CX}" y="{CY}" width="{CW}" height="{CH_IMG}" fill="url(#sl)" opacity="0.15"/></g>
  <!-- Reveal scan line -->
  <rect x="{CX-10}" y="{CY}" width="{CW+30}" height="7" fill="url(#slG)" filter="url(#sg)" opacity="0">
    <animate attributeName="opacity" values="0;0.8;0.8;0" keyTimes="0;0.05;0.85;1" dur="2.8s" begin="0.3s" fill="freeze"/>
    <animate attributeName="y" from="{CY}" to="{CY+CH_IMG}" dur="2.5s" begin="0.5s" fill="freeze"/></rect>

  <!-- ══════ LEFT COLUMN ══════ -->

  <!-- Terminal -->
  <text x="42" y="45" font-size="16" font-family="Cascadia Code,Fira Code,Consolas,monospace" fill="{tg}" clip-path="url(#tc)">
    <tspan fill="{tp}">akshat@fullstackdev</tspan><tspan fill="{txd}">:</tspan><tspan fill="#60a5fa">~</tspan><tspan fill="{txd}">$ </tspan><tspan fill="{tg}">cat README.md</tspan></text>
  <rect x="42" y="28" width="8" height="20" fill="{tg}" class="cur">
    <animate attributeName="x" from="42" to="460" dur="2s" begin="0.3s" fill="freeze"/></rect>

  <!-- Greeting -->
  <text x="42" y="92" font-size="24" fill="{tx}" opacity="0" font-family="Segoe UI,sans-serif">
    Hi, I'm &#128075;<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.2s" fill="freeze"/></text>

  <!-- Name (TWO LINES) -->
  <text x="42" y="140" font-size="52" font-family="Segoe Script,Brush Script MT,Dancing Script,cursive" fill="url(#nG)" font-weight="bold" filter="url(#gl)">
    {ns1}</text>
  <text x="42" y="192" font-size="52" font-family="Segoe Script,Brush Script MT,Dancing Script,cursive" fill="url(#nG)" font-weight="bold" filter="url(#gl)">
    {ns2}</text>
  <!-- Heart after name -->
  <text x="345" y="192" font-size="28" opacity="0" fill="{hc}">&#9829;<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="3.4s" fill="freeze"/></text>

  <!-- Role cycling -->
  <text x="42" y="222" font-size="18" fill="{tp}" opacity="0" font-family="Cascadia Code,monospace">
    &lt;<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="3.5s" fill="freeze"/></text>
  <text x="58" y="222" font-size="18" fill="{txb}" font-family="Cascadia Code,Fira Code,monospace" clip-path="url(#r1c)">Full Stack Developer</text>
  <text x="58" y="222" font-size="18" fill="{txb}" font-family="Cascadia Code,Fira Code,monospace" clip-path="url(#r2c)">AI Engineer</text>
  <text x="58" y="222" font-size="18" fill="{txb}" font-family="Cascadia Code,Fira Code,monospace" clip-path="url(#r3c)">Open Source Contributor</text>
  <text x="360" y="222" font-size="18" fill="{tp}" opacity="0" font-family="Cascadia Code,monospace">
    /&gt;<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="3.5s" fill="freeze"/></text>
  <!-- Typing cursor -->
  <rect y="206" width="2" height="21" fill="{txb}" class="cur">
    <animate attributeName="x" values="56;56;300;300;56;56;210;210;56;56;340;340;56"
             keyTimes="0;0.02;0.20;0.30;0.33;0.36;0.52;0.63;0.66;0.70;0.86;0.96;1"
             dur="9s" repeatCount="indefinite" begin="3.5s"/></rect>

  <!-- Quote box -->
  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="3.6s" fill="freeze"/>
    <rect x="42" y="248" width="370" height="55" rx="8" fill="{qbg}" stroke="{qbd}" stroke-width="1" stroke-opacity="0.2"/>
    <rect x="42" y="248" width="3" height="55" rx="1.5" fill="{qbd}"/></g>
  <text clip-path="url(#tgc)" font-size="14" fill="{tx}" font-family="Cascadia Code,monospace">
    <tspan x="55" y="272">I don't just use AI,</tspan>
    <tspan x="55" y="292">I code it.</tspan></text>

  <!-- Tech I Know -->
  <text x="42" y="345" font-size="16" fill="{tp}" opacity="0" font-family="Segoe UI,sans-serif" font-weight="bold">
    &#128187; Tech I Know<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="4.3s" fill="freeze"/></text>
  {pills}

  <!-- About Me -->
  <text x="42" y="510" font-size="16" fill="{tp}" opacity="0" font-family="Segoe UI,sans-serif" font-weight="bold">
    &#10024; About Me<animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="5.8s" fill="freeze"/></text>
  {about_svg}

  <!-- Stats row card -->
  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="6.8s" fill="freeze"/>
    <rect x="42" y="615" width="520" height="82" rx="10" fill="{stat_card}" stroke="{stat_border}" stroke-width="1"/>
    <!-- Dividers -->
    <line x1="172" y1="628" x2="172" y2="690" stroke="{stat_border}" stroke-width="1"/>
    <line x1="302" y1="628" x2="302" y2="690" stroke="{stat_border}" stroke-width="1"/>
    <line x1="432" y1="628" x2="432" y2="690" stroke="{stat_border}" stroke-width="1"/></g>
  {stats_svg}

  <!-- Contact row -->
  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="7.8s" fill="freeze"/>
    <!-- Github -->
    <rect x="42" y="725" width="130" height="32" rx="16" fill="{stat_card}" stroke="{stat_border}" stroke-width="1"/>
    <text x="60" y="746" font-size="14" fill="{tx}">&#128231;</text>
    <text x="82" y="745" font-size="14" fill="{txd}" font-family="Segoe UI,sans-serif">Akshat685</text>
    
    <!-- Email -->
    <rect x="182" y="725" width="260" height="32" rx="16" fill="{stat_card}" stroke="{stat_border}" stroke-width="1"/>
    <text x="200" y="746" font-size="14" fill="{tx}">&#9993;</text>
    <text x="222" y="745" font-size="14" fill="{txd}" font-family="Segoe UI,sans-serif">akshatshettigar2001@gmail.com</text>

    <!-- Collaborate -->
    <rect x="452" y="725" width="180" height="32" rx="16" fill="{stat_card}" stroke="{stat_border}" stroke-width="1"/>
    <text x="470" y="745" font-size="12" fill="#4ade80">&#9679;</text>
    <text x="486" y="745" font-size="14" fill="{txd}" font-family="Segoe UI,sans-serif">open to collaborate</text>
  </g>

  <!-- Bottom quote -->
  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="8.2s" fill="freeze"/>
    <text x="1240" y="822" text-anchor="end" font-size="17" fill="{txd}" font-style="italic" font-family="Segoe UI,Georgia,serif">
      "Turning caffeine into code &amp; ideas into interfaces." <tspan fill="{hc}">&#10084;</tspan></text></g>

  <!-- ══════ CODE EDITOR (overlays character) ══════ -->
  <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="7s" fill="freeze"/>
    <rect x="{CE_X}" y="{CE_Y}" width="{CE_W}" height="{CE_H}" rx="10" fill="{cbg}" stroke="{cbd}" stroke-width="1" opacity="0.95"/>
    <rect x="{CE_X}" y="{CE_Y}" width="{CE_W}" height="26" rx="10" fill="{chd}"/>
    <rect x="{CE_X}" y="{CE_Y+16}" width="{CE_W}" height="10" fill="{chd}"/>
    <circle cx="{CE_X+18}" cy="{CE_Y+13}" r="4.5" fill="#ef4444" opacity="0.8"/>
    <circle cx="{CE_X+33}" cy="{CE_Y+13}" r="4.5" fill="#f59e0b" opacity="0.8"/>
    <circle cx="{CE_X+48}" cy="{CE_Y+13}" r="4.5" fill="#22c55e" opacity="0.8"/>
    <text x="{CE_X+132}" y="{CE_Y+20}" text-anchor="middle" font-size="13" fill="{txd}" font-family="Segoe UI,sans-serif">dreams.jsx</text></g>
  {editor_svg}

  <!-- ══════ NEON SIGN (top-right) ══════ -->
  <g class="neo">
    <rect x="1015" y="38" width="225" height="100" rx="12" fill="none" stroke="{nt}" stroke-width="1.2" stroke-opacity="0.35"/>
    <text x="1127" y="72" text-anchor="middle" font-size="28" fill="{tp}" font-family="Cascadia Code,monospace" font-weight="bold" filter="url(#ng)">&lt;/&gt;</text>
    <text x="1127" y="100" text-anchor="middle" font-size="13" fill="{nt}" font-family="Cascadia Code,monospace" font-weight="bold" letter-spacing="2" filter="url(#ng)">KEEP CODING</text>
    <text x="1127" y="120" text-anchor="middle" font-size="13" fill="{nt}" font-family="Cascadia Code,monospace" font-weight="bold" letter-spacing="2" filter="url(#ng)">KEEP GROWING</text></g>

  <!-- Continuous scanner -->
  <rect x="0" y="0" width="1280" height="4" fill="url(#slG)" filter="url(#sg)" opacity="0.3">
    <animate attributeName="y" from="0" to="{H}" dur="3.5s" begin="3.5s" repeatCount="indefinite"/></rect>

  {hearts}
  {sparkles}
  {particles}
</g>
</svg>'''
    return svg


# ═══════════════════════════════════════════════════════════
#  LANYARD SVG
# ═══════════════════════════════════════════════════════════
def lanyard_svg():
    bars = ""
    bx = 75
    widths = [2,1,3,1,1,2,1,3,2,1,1,1,2,1,3,1,2,1,1,2,3,1,1,2,1,1,2]
    for w in widths:
        bars += f'<rect x="{bx}" y="495" width="{w}" height="35" fill="rgba(255,255,255,0.75)" rx="0.5"/>\n'
        bx += w + 1.5

    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
     viewBox="0 0 340 650" width="340" height="650">
<defs>
  <linearGradient id="mG" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#d1d5db"/><stop offset="50%" stop-color="#f9fafb"/><stop offset="100%" stop-color="#9ca3af"/></linearGradient>
  <linearGradient id="gR" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#7c3aed"/><stop offset="50%" stop-color="#c026d3"/><stop offset="100%" stop-color="#f472b6"/></linearGradient>
  <linearGradient id="hS" x1="0" y1="0" x2="1" y2="0.3"><stop offset="0%" stop-color="rgba(255,255,255,0)"/><stop offset="45%" stop-color="rgba(255,255,255,0)"/><stop offset="50%" stop-color="rgba(255,255,255,0.2)"/><stop offset="55%" stop-color="rgba(255,255,255,0)"/><stop offset="100%" stop-color="rgba(255,255,255,0)"/></linearGradient>
  <linearGradient id="sG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f472b6"/><stop offset="100%" stop-color="#c026d3"/></linearGradient>
  <linearGradient id="cG" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1a1a2e"/><stop offset="100%" stop-color="#16213e"/></linearGradient>
  <clipPath id="aC"><circle cx="170" cy="310" r="48"/></clipPath>
  <clipPath id="cC"><rect x="60" y="225" width="220" height="320" rx="14"/></clipPath>
  <filter id="cSh"><feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#000" flood-opacity="0.4"/></filter>
  <filter id="aGl"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<g>
  <animateTransform attributeName="transform" type="translate" values="0 -660;0 0" dur="0.8s" fill="freeze" calcMode="spline" keySplines="0.25 0.1 0.25 1"/>
  <g><animateTransform attributeName="transform" type="rotate" values="0 170 0;18 170 0;-14 170 0;10 170 0;-7 170 0;4 170 0;-2.5 170 0;1.5 170 0;0 170 0" dur="3s" begin="0.8s" fill="freeze"/>
    <g><animateTransform attributeName="transform" type="rotate" values="0 170 0;2 170 0;0 170 0;-2 170 0;0 170 0" dur="5s" begin="3.8s" repeatCount="indefinite"/>

      <!-- Strap & Hole -->
      <rect x="148" y="0" width="44" height="238" fill="url(#sG)"/>
      <!-- Rope border stripes (stitching) -->
      <line x1="151" y1="0" x2="151" y2="238" stroke="rgba(255,255,255,0.6)" stroke-width="1.5" stroke-dasharray="4,4"/>
      <line x1="189" y1="0" x2="189" y2="238" stroke="rgba(255,255,255,0.6)" stroke-width="1.5" stroke-dasharray="4,4"/>
      
      <text transform="rotate(-90, 170, 119)" x="170" y="119" text-anchor="middle" alignment-baseline="central" font-size="7" fill="rgba(255,255,255,0.6)" font-family="Segoe UI,sans-serif" letter-spacing="2" font-weight="bold">AKSHAT.DEV &#9679; CODE &#9679; AKSHAT.DEV &#9679; CODE &#9679; AKSHAT.DEV</text>

      <!-- Card with glow border -->
      <g filter="url(#cSh)">
        <rect x="60" y="225" width="220" height="320" rx="14" fill="url(#cG)" stroke="url(#gR)" stroke-width="1.5" stroke-opacity="0.8"/></g>
        
      <rect x="140" y="232" width="60" height="12" rx="6" fill="#0d0221" stroke="#334155" stroke-width="2"/>

      <!-- Header -->
      <text x="75" y="260" font-size="8" fill="#94a3b8" font-family="Segoe UI,sans-serif" letter-spacing="1" font-weight="bold">DEVELOPER ID</text>
      <text x="265" y="260" text-anchor="end" font-size="8" fill="#f472b6" font-family="Cascadia Code,monospace" font-weight="bold">AS-0685</text>
      
      <!-- Avatar glow ring (zoomed image) -->
      <circle cx="170" cy="310" r="53" fill="none" stroke="url(#gR)" stroke-width="2.5" opacity="0.8" filter="url(#aGl)">
        <animate attributeName="opacity" values="0.6;1;0.6" dur="3s" repeatCount="indefinite"/></circle>
      <image clip-path="url(#aC)" href="data:image/png;base64,{FACE_B64}" xlink:href="data:image/png;base64,{FACE_B64}" x="100" y="255" width="180" height="160"/>

      <!-- Name in neon cursive -->
      <text x="170" y="405" text-anchor="middle" font-size="22" fill="#f9a8d4" font-family="Segoe Script,Brush Script MT,cursive" font-weight="bold" filter="url(#ng)">Akshat Shettigar</text>
      <text x="170" y="405" text-anchor="middle" font-size="22" fill="#fff" font-family="Segoe Script,Brush Script MT,cursive" font-weight="bold">Akshat Shettigar</text>
      
      <!-- Role with glitch effect -->
      <text x="169" y="435" text-anchor="middle" font-size="10" fill="#f43f5e" font-family="Segoe UI,sans-serif" font-weight="bold" letter-spacing="2">FULL STACK DEVELOPER</text>
      <text x="171" y="435" text-anchor="middle" font-size="10" fill="#0ea5e9" font-family="Segoe UI,sans-serif" font-weight="bold" letter-spacing="2">FULL STACK DEVELOPER</text>
      <text x="170" y="435" text-anchor="middle" font-size="10" fill="#f8fafc" font-family="Segoe UI,sans-serif" font-weight="bold" letter-spacing="2">FULL STACK DEVELOPER</text>
      
      <!-- Username -->
      <text x="170" y="455" text-anchor="middle" font-size="9" fill="#93c5fd" font-family="Cascadia Code,monospace">@Akshat685</text>

      <!-- Footer: Barcode Left, Tech Right -->
      {bars}
      <text x="265" y="505" text-anchor="end" font-size="7" fill="#94a3b8" font-family="Cascadia Code,monospace" letter-spacing="1">REACT &#9679; NEXT.JS</text>
      <text x="265" y="515" text-anchor="end" font-size="7" fill="#94a3b8" font-family="Cascadia Code,monospace" letter-spacing="1">NODE.JS &#9679; GRAPHQL</text>
      <text x="265" y="525" text-anchor="end" font-size="7" fill="#94a3b8" font-family="Cascadia Code,monospace" letter-spacing="1">OPENAI &#9679; GEMINI</text>

      <!-- Holographic shine -->
      <rect x="-200" y="225" width="220" height="320" fill="url(#hS)" clip-path="url(#cC)" opacity="0.5">
        <animate attributeName="x" from="-200" to="340" dur="3s" begin="2s" repeatCount="indefinite"/></rect>
    </g>
  </g>
</g>
</svg>'''


# ═══════════════════════════════════════════════════════════
#  STATS SVG (improved with border glow)
# ═══════════════════════════════════════════════════════════
def stats_svg():
    items = [("&#11088;","Total Stars Earned:","15+","#fbbf24"),("&#128221;","Total Commits:","234+","#4ade80"),
             ("&#128193;","Public Repos:","8+","#60a5fa"),("&#128101;","Followers:","10+","#f472b6"),
             ("&#128296;","Projects Built:","6","#a78bfa")]
    rows = ""
    for i,(em,lb,val,cl) in enumerate(items):
        y = 58 + i*28; dl = round(0.8 + i*0.2, 2)
        rows += (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{dl}s" fill="freeze"/>'
                 f'<text x="22" y="{y}" font-size="12" fill="#e2e8f0" font-family="Segoe UI,sans-serif">{em} {lb}</text>'
                 f'<text x="280" y="{y}" font-size="13" fill="{cl}" font-weight="bold" font-family="Segoe UI,sans-serif" text-anchor="end">{val}</text></g>\n')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 230" width="500" height="230">
<defs><linearGradient id="cBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a0533"/><stop offset="100%" stop-color="#0d0221"/></linearGradient>
  <linearGradient id="rG" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#c026d3"/></linearGradient>
  <linearGradient id="bdr" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#c026d3"/></linearGradient></defs>
<rect width="500" height="230" rx="12" fill="url(#cBg)" stroke="url(#bdr)" stroke-width="1.5" stroke-opacity="0.3"/>
<text x="22" y="30" font-size="14" fill="#f472b6" font-family="Segoe UI,sans-serif" font-weight="bold">&#11088; Akshat Shettigar's GitHub Stats</text>
<line x1="22" y1="40" x2="280" y2="40" stroke="#4c1d95" stroke-width="1"/>
{rows}
<circle cx="410" cy="130" r="50" fill="none" stroke="rgba(255,255,255,0.04)" stroke-width="7"/>
<circle cx="410" cy="130" r="50" fill="none" stroke="url(#rG)" stroke-width="7"
        stroke-dasharray="314" stroke-dashoffset="314" stroke-linecap="round" transform="rotate(-90 410 130)">
  <animate attributeName="stroke-dashoffset" from="314" to="95" dur="2s" begin="0.5s" fill="freeze"/></circle>
<text x="410" y="125" text-anchor="middle" font-size="24" fill="#c084fc" font-family="Segoe UI,sans-serif" font-weight="bold" opacity="0">B+<animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.8s" fill="freeze"/></text>
<text x="410" y="145" text-anchor="middle" font-size="10" fill="#94a3b8" font-family="Segoe UI,sans-serif" opacity="0">RANK<animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="1.8s" fill="freeze"/></text>
</svg>'''


def langs_svg():
    langs = [("JavaScript",38,"#f7df1e"),("TypeScript",24,"#3178c6"),("HTML",15,"#e34f26"),("CSS",13,"#1572b6"),("Python",10,"#3572a5")]
    # Top bar (combined)
    top_bar = ""
    bx = 22
    total_w = 306
    for nm,pct,cl in langs:
        w = int(pct/100*total_w)
        top_bar += f'<rect x="{bx}" y="42" width="0" height="10" rx="2" fill="{cl}"><animate attributeName="width" from="0" to="{w}" dur="0.8s" begin="0.5s" fill="freeze"/></rect>\n'
        bx += w
    rows = ""
    for i,(nm,pct,cl) in enumerate(langs):
        y = 72 + i*28; dl = round(0.5 + i*0.2, 1); bw = int(pct*2.2)
        rows += (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{dl}s" fill="freeze"/>'
                 f'<circle cx="25" cy="{y-3}" r="4" fill="{cl}"/>'
                 f'<text x="38" y="{y}" font-size="12" fill="#e2e8f0" font-family="Segoe UI,sans-serif">{nm}</text>'
                 f'<text x="308" y="{y}" font-size="11" fill="{cl}" font-family="Segoe UI,sans-serif" text-anchor="end" font-weight="bold">{pct}.0%</text>'
                 f'<rect x="140" y="{y-10}" width="140" height="8" rx="4" fill="rgba(255,255,255,0.06)"/>'
                 f'<rect x="140" y="{y-10}" width="0" height="8" rx="4" fill="{cl}" opacity="0.8">'
                 f'<animate attributeName="width" from="0" to="{bw}" dur="0.8s" begin="{dl+0.2}s" fill="freeze"/></rect></g>\n')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 230" width="340" height="230">
<defs><linearGradient id="cBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a0533"/><stop offset="100%" stop-color="#0d0221"/></linearGradient>
  <linearGradient id="bdr" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#7c3aed"/><stop offset="100%" stop-color="#c026d3"/></linearGradient></defs>
<rect width="340" height="230" rx="12" fill="url(#cBg)" stroke="url(#bdr)" stroke-width="1.5" stroke-opacity="0.3"/>
<text x="22" y="30" font-size="14" fill="#60a5fa" font-family="Segoe UI,sans-serif" font-weight="bold">&#128202; Top Languages</text>
{top_bar}
{rows}
</svg>'''


def trophies_svg():
    trophies = [("Commits","A","#fbbf24","&#128187;","234+"),("Stars","B","#c0c0c0","&#11088;","15+"),
                ("PRs","A","#fbbf24","&#128293;","12+"),("Repos","A","#fbbf24","&#128230;","8+"),
                ("Issues","B","#c0c0c0","&#128196;","8+"),("Followers","B","#c0c0c0","&#128101;","10+")]
    cells = ""
    for i,(nm,rank,cl,icon,count) in enumerate(trophies):
        x = 18 + i*128; dl = round(0.4 + i*0.15, 2)
        # Colored underline
        ucl = "#fbbf24" if rank=="A" else ("#c0c0c0" if rank=="B" else "#cd7f32")
        cells += (f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.35s" begin="{dl}s" fill="freeze"/>'
                  f'<rect x="{x}" y="50" width="120" height="120" rx="12" fill="rgba(13,2,33,0.5)" stroke="{cl}" stroke-width="1" stroke-opacity="0.25"/>'
                  f'<text x="{x+35}" y="88" font-size="22">{icon}</text>'
                  f'<text x="{x+70}" y="90" font-size="22" fill="{cl}" font-weight="bold" font-family="Segoe UI,sans-serif">{rank}</text>'
                  f'<text x="{x+60}" y="118" text-anchor="middle" font-size="11" fill="#e2e8f0" font-family="Segoe UI,sans-serif" font-weight="600">{nm}</text>'
                  f'<text x="{x+60}" y="136" text-anchor="middle" font-size="9" fill="#94a3b8" font-family="Segoe UI,sans-serif">{count}</text>'
                  f'<rect x="{x+20}" y="148" width="80" height="3" rx="1.5" fill="{ucl}" opacity="0.6"/>'
                  f'</g>\n')
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 790 185" width="790" height="185">
<defs><linearGradient id="cBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a0533"/><stop offset="100%" stop-color="#0d0221"/></linearGradient>
  <linearGradient id="tSh" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(255,255,255,0)"/><stop offset="45%" stop-color="rgba(255,255,255,0)"/><stop offset="50%" stop-color="rgba(255,255,255,0.12)"/><stop offset="55%" stop-color="rgba(255,255,255,0)"/><stop offset="100%" stop-color="rgba(255,255,255,0)"/></linearGradient></defs>
<rect width="790" height="185" rx="12" fill="url(#cBg)" stroke="#4c1d95" stroke-width="1"/>
<text x="22" y="30" font-size="14" fill="#e2e8f0" font-family="Segoe UI,sans-serif" font-weight="bold">&#127942; GitHub Profile Trophies</text>
<line x1="22" y1="42" x2="770" y2="42" stroke="#4c1d95" stroke-width="1"/>
{cells}
<rect x="-200" y="50" width="200" height="120" fill="url(#tSh)" opacity="0.5">
  <animate attributeName="x" from="-200" to="790" dur="4s" begin="1.5s" repeatCount="indefinite"/></rect>
</svg>'''



# ═══════════════════════════════════════════════════════════
#  PROJECTS SVG
# ═══════════════════════════════════════════════════════════
def projects_svg():
    projects = [
        ("Workforce Pulse", ["Next.js", "TypeScript", "Tailwind CSS", "Recharts", "Zod", "PapaParse", "jsPDF", "OpenAI API"]),
        ("Chat with Website", ["Next.js", "TypeScript", "Tailwind CSS", "Cheerio", "OpenAI SDK", "Gemini API"]),
        ("File Converter", ["React", "TypeScript", "Node.js", "Express.js", "Dropbox API", "Google API"]),
        ("InvyTrack", ["MongoDB", "Express.js", "React.js", "Node.js", "HTML", "CSS", "JavaScript"]),
        ("GymFuel", ["MongoDB", "Express.js", "React.js", "Node.js", "HTML", "CSS", "JavaScript"]),
        ("FlowBoard", ["Next.js", "TypeScript", "Tailwind CSS", "GraphQL", "Apollo", "Prisma", "PostgreSQL", "Sanity", "Node.js"])
    ]
    
    W = 500
    row_H = 80
    H = len(projects) * row_H + 50
    
    cards = ""
    for i, (title, tech) in enumerate(projects):
        y = 45 + i * row_H
        dl = round(0.5 + i * 0.1, 2)
        
        tech_svg = ""
        full_str = " • ".join(tech)
        if len(full_str) < 65:
            tech_svg = f'<text x="25" y="{y+48}" font-size="10" fill="#94a3b8" font-family="Cascadia Code,monospace">{" &#9679; ".join(tech)}</text>'
        else:
            mid = len(tech)//2 + 1
            l1 = " &#9679; ".join(tech[:mid])
            l2 = " &#9679; ".join(tech[mid:])
            tech_svg = f'<text x="25" y="{y+42}" font-size="10" fill="#94a3b8" font-family="Cascadia Code,monospace">{l1}</text>'
            tech_svg += f'<text x="25" y="{y+56}" font-size="10" fill="#94a3b8" font-family="Cascadia Code,monospace">{l2}</text>'
            
        cards += f'''
        <g opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="{dl}s" fill="freeze"/>
          <rect x="5" y="{y}" width="490" height="70" rx="10" fill="rgba(13,2,33,0.6)" stroke="#4c1d95" stroke-width="1.2" stroke-opacity="0.8"/>
          <text x="25" y="{y+24}" font-size="14" fill="#f472b6" font-family="Segoe UI,sans-serif" font-weight="bold">&#128640; {title}</text>
          {tech_svg}
          <circle cx="475" cy="{y+35}" r="12" fill="#1a0533" stroke="#c026d3" stroke-width="1.5"/>
          <path d="M472 30 L478 35 L472 40" stroke="#f8fafc" stroke-width="2" fill="none" stroke-linecap="round"/>
        </g>
        '''
        
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">
<defs><linearGradient id="cBg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#1a0533"/><stop offset="100%" stop-color="#0d0221"/></linearGradient></defs>
<rect width="{W}" height="{H}" rx="14" fill="url(#cBg)" stroke="#4c1d95" stroke-width="1"/>
<text x="15" y="28" font-size="16" fill="#e2e8f0" font-family="Segoe UI,sans-serif" font-weight="bold">&#128187; My Projects</text>
<line x1="15" y1="36" x2="485" y2="36" stroke="#4c1d95" stroke-width="1"/>
{cards}
</svg>'''

if __name__ == '__main__':

    print("Generating v3 SVGs (redesigned layout)...")
    files = {
        'banner.svg': banner_svg('dark'),
        'banner-light.svg': banner_svg('light'),
        'lanyard.svg': lanyard_svg(),
        'stats.svg': stats_svg(),
        'langs.svg': langs_svg(),
        'trophies.svg': trophies_svg(),
    }
    for name, content in files.items():
        path = os.path.join(DIR, name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  OK {name} ({len(content):,} bytes)')
    print("\nDone! All files regenerated.")
