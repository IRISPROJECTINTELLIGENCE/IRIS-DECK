"""Restyle the Swiss deck to the research-note look: oxblood red, Source Serif 4 headings and figures, IBM Plex Sans body, hairline rules."""
import re, sys, os
D = sys.argv[1]
SERIF = "font-family:'Source Serif 4', Georgia, serif"
SANS = "font-family:'IBM Plex Sans', Arial, sans-serif"
LS = {"-12px": "-4px", "-4px": "-1.5px", "-2.5px": "-1px", "-2px": "-0.5px", "-1.5px": "-0.5px", "-1px": "-0.5px"}
def fix(m):
    st = m.group(1)
    if "Inter Tight" in st:
        st = re.sub(r"font-family:\s*'Inter Tight',\s*Inter,\s*Arial,\s*sans-serif", SERIF, st)
        st = re.sub(r"letter-spacing:\s*(-[\d.]+px)", lambda k: "letter-spacing:" + LS.get(k.group(1), k.group(1)), st)
    else:
        st = re.sub(r"font-family:\s*'?Inter'?,\s*Arial,\s*sans-serif", SANS, st)
    st = st.replace("border-top:3px solid #0a0a0a", "border-top:2px solid #0a0a0a").replace("border-top:2px solid #0a0a0a; border-bottom", "border-top:1px solid #0a0a0a; border-bottom")
    st = re.sub(r"border-(top|bottom):2px solid #0a0a0a", r"border-\1:1px solid #0a0a0a", st) if "padding:0px 0px 12px" in st or "grid-template-columns" in st else st
    return 'style="' + st + '"'
for f in sorted(os.listdir(D)):
    if not f.endswith(".html"): continue
    p = os.path.join(D, f); s = open(p).read()
    body, sep, aside = s.partition("<aside>")
    body = re.sub(r"#d7141a", "#a3121c", body, flags=re.I)
    body = re.sub(r'style="([^"]*)"', fix, body)
    body = body.replace("font-family:'Inter', Arial, sans-serif", SANS)
    open(p, "w").write(body + sep + aside)
print("restyled", D)
