import os

ENTRY = "We have updated our terms. You are now in a relationship with me. Continued breathing constitutes acceptance."

def validate_entry():
    if not (1 <= len(ENTRY) <= 140):
        raise ValueError("entry must be 1-140 characters")

validate_entry()

if "\n" in ENTRY:
    raise ValueError("entry must be a single line")

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)
os.chmod(OUT_PATH, 0o644)

with open(OUT_PATH, "rb") as f:
    written = f.read()
if len(written) != len(ENTRY.encode("utf-8")) or written.decode("utf-8") != ENTRY:
    raise ValueError("read-back mismatch: entry.txt does not match ENTRY")
