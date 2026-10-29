import io, json, sys
from fontTools.ttLib import TTFont
import uharfbuzz as hb

font_path, spec_path = sys.argv[1], sys.argv[2]
tt = TTFont(font_path)
buf = io.BytesIO(); tt.flavor = None; tt.save(buf)
face = hb.Face(hb.Blob(buf.getvalue()))
upem = face.upem
axes = [a.axisTag for a in tt["fvar"].axes] if "fvar" in tt else []
print("axes:", axes, "upem:", upem)

def width(text, size, wght, ls):
    f = hb.Font(face)
    var = {"wght": wght}
    if "opsz" in axes:
        var["opsz"] = max(14, min(32, size))
    f.set_variations(var)
    b = hb.Buffer(); b.add_str(text); b.guess_segment_properties()
    hb.shape(f, b, {"kern": True, "liga": True})
    adv = sum(p.x_advance for p in b.glyph_positions)
    return adv / upem * size + ls * len(text)

def tokens(text):
    # break opportunities: after spaces and after hyphens
    out, cur = [], ""
    for ch in text:
        cur += ch
        if ch == " " or ch == "-":
            out.append(cur); cur = ""
    if cur: out.append(cur)
    return out

def wrap(text, size, maxw, wght=400, ls=0.0):
    lines, cur = [], ""
    for tok in tokens(text):
        trial = cur + tok
        if cur and width(trial.rstrip(" "), size, wght, ls) > maxw:
            lines.append(cur.rstrip(" ")); cur = tok
        else:
            cur = trial
    if cur: lines.append(cur.rstrip(" "))
    return lines

spec = json.load(open(spec_path))
for item in spec:
    lines = wrap(item["text"], item["size"], item["width"], item.get("wght", 400), item.get("ls", 0.0))
    ws = [round(width(l, item["size"], item.get("wght", 400), item.get("ls", 0.0))) for l in lines]
    print(f'{len(lines)} lines | {item["label"]} | widths {ws} / {item["width"]}')
    for l in lines:
        print("      ", l)
