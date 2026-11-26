"""Recolour IRIS slides to the Swiss palette and leave the typography untouched.
Usage: colours.py <slides_dir>
White background, neutral greys, one red #D7141A; the section label (top 62px) in near-black."""
import re, sys, os
D = sys.argv[1]
CMAP = {"faf7f0": "ffffff", "fffdf8": "ffffff", "1a1714": "0a0a0a", "3d3934": "2a2a2a", "6f6a63": "6b6b6b", "5f5a53": "5a5a5a",
        "e8533a": "d7141a", "c2412a": "d7141a", "ff8a6e": "ff4d4d", "d9d4ca": "d6d6d6", "ece7dc": "e6e6e6", "ecc9bb": "e0e0e0",
        "f1ede4": "f2f2f2", "f8e6dd": "f5f5f5", "efe9dc": "ffffff", "cfc8bb": "bdbdbd", "9c968c": "9a9a9a", "3a3530": "333333",
        "ccc6bc": "cccccc", "beb8ae": "bbbbbb", "ada79d": "a8a8a8", "8a847b": "888888"}
def recolour(s):
    body, sep, aside = s.partition("<aside>")
    body = re.sub(r"#([0-9a-fA-F]{6})\b", lambda m: "#" + CMAP.get(m.group(1).lower(), m.group(1).lower()), body)
    def label(m):
        st = m.group(1)
        if "top:62px" in st and "font-size:24px" in st:
            st = st.replace("color:#d7141a", "color:#0a0a0a")
        return 'style="' + st + '"'
    body = re.sub(r'style="([^"]*)"', label, body)
    return body + sep + aside
for f in sorted(os.listdir(D)):
    if f.endswith(".html"):
        p = os.path.join(D, f); s = open(p).read(); open(p, "w").write(recolour(s))
print("recoloured", D)
