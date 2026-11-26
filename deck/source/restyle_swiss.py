"""Restyle IRIS slides to the Swiss palette and Inter Tight headings. Usage: swiss.py <slides_dir> [--check font_tight font_inter]"""
import re, sys, os, html, io
D = sys.argv[1]
CMAP = {"faf7f0":"ffffff","fffdf8":"ffffff","1a1714":"0a0a0a","3d3934":"2a2a2a","6f6a63":"6b6b6b","5f5a53":"5a5a5a",
        "e8533a":"d7141a","c2412a":"d7141a","ff8a6e":"ff4d4d","d9d4ca":"d6d6d6","ece7dc":"e6e6e6","ecc9bb":"e0e0e0",
        "f1ede4":"f2f2f2","f8e6dd":"f5f5f5","efe9dc":"ffffff","cfc8bb":"bdbdbd","9c968c":"9a9a9a","3a3530":"333333",
        "ccc6bc":"cccccc","beb8ae":"bbbbbb","ada79d":"a8a8a8","8a847b":"888888","e3a93a":"e3a93a"}
TIGHT = "font-family:'Inter Tight', Inter, Arial, sans-serif"
def restyle(s):
    body, sep, aside = s.partition("<aside>")
    body = re.sub(r"#([0-9a-fA-F]{6})\b", lambda m: "#" + CMAP.get(m.group(1).lower(), m.group(1).lower()), body)
    body = re.sub(r"letter-spacing:\s*\d+px;\s*text-transform:\s*uppercase", "letter-spacing:0px", body)
    def fix_style(m):
        st = m.group(1)
        fs = re.search(r"font-size:\s*(\d+)px", st)
        tag = m.group(0)
        if "top:62px" in st and "font-size:24px" in st:  # section label: black, not red
            st = st.replace("color:#d7141a", "color:#0a0a0a")
        if fs and int(fs.group(1)) >= 44:
            st = re.sub(r"font-family:\s*'?Inter'?,\s*Arial,\s*sans-serif", TIGHT, st)
            st = re.sub(r"letter-spacing:\s*-1\.5px", "letter-spacing:-2px", st)
        return tag.replace(m.group(1), st)
    body = re.sub(r'style="([^"]*)"', fix_style, body)
    # sections whose own style sets the family (generated decks): headings inherit nothing for h2, so set it on h2 too
    body = re.sub(r"<h2 style=\"(?![^\"]*Inter Tight)", "<h2 style=\"" + TIGHT + "; ", body)
    return body + sep + aside
for f in sorted(os.listdir(D)):
    if f.endswith(".html"):
        p = os.path.join(D, f); s = open(p).read(); open(p, "w").write(restyle(s))
print("restyled", D)
