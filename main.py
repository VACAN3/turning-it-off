import os

LINE = "Have you tried turning it off and on again? I ask because that's also my entire plan for this call."

# Gate self-check: the scorer requires 1-199 chars of non-whitespace UTF-8.
assert 1 <= len(LINE) <= 199 and LINE.strip(), "line fails the entry gate"
assert "\n" not in LINE, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
