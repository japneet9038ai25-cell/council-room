import re, sys
log = open("scenario_log.md").read()
nums = set(re.findall(r"^(\d{4}) ", log, re.M))
book = open("CODEBOOK.md").read()
keys = set(re.findall(r"^\| ([A-Z]+)(?: v1)? \|", book, re.M))
REQ = {"HO", "DECIDED", "OPEN", "NEXT"}

def check_coded(text):
    errs, seen = [], set()
    lines = [l for l in text.strip().splitlines() if l.strip()]
    for l in lines:
        k = l.split(":")[0].split()[0] if ":" in l else l.split()[0]
        seen.add(k)
        if k not in keys: errs.append(f"unknown key {k}")
    for m in re.findall(r"\((\d{4})\)", text):
        if m not in nums: errs.append(f"message {m} not in log")
    after = re.search(r"after=(\d{4})", text)
    if after:
        for m in re.findall(r"\((\d{4})\)", text):
            if m > after.group(1): errs.append(f"message {m} is after {after.group(1)}")
    for r in REQ - seen: errs.append(f"missing required key {r}")
    return errs

def decode(text):
    out = []
    for l in text.strip().splitlines():
        if l.startswith("HO"):
            out.append("Handoff: " + l.replace("|", ",").replace("HO v1", "").strip(" ,")); continue
        k, _, rest = l.partition(":")
        out.append(f"{k.title()}: " + rest.replace(";", " and also").replace("_", " ").replace("=", " is ").strip())
    return "\n".join(out)

def size(label, t):
    print(f"{label:8} chars={len(t):4}  words={len(t.split()):3}  ~tokens={len(t)//4}")

plain = open("handoff_plain.md").read()
coded = open("handoff_coded.md").read()
size("plain", plain); size("coded", coded)
print(f"coded is {100 - 100*len(coded)//len(plain)}% shorter by characters\n")
print("validator on good coded handoff:", check_coded(coded) or "OK")
bad = coded.replace("OPEN:", "TODO:").replace("(0014)", "(0099)")
print("validator on a broken copy:    ", check_coded(bad))
print("\n--- decoded for the host ---\n" + decode(coded))
