import os

ENTRY = "We have updated our terms. You are now in a relationship with me. Continued breathing constitutes acceptance."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")

os.makedirs(OUT_DIR, exist_ok=True)
with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(ENTRY)
os.chmod(OUT_PATH, 0o644)
