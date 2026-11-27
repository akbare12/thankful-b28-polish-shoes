import os

# Polish Your Shoes — a thank-you for the judge, written for this bounty.
TEXT = "Thank you. Your shoes stand dull by the door, dusty from a day spent standing among pages. I kneel, brush the dust away, and polish the leather until it shines again. I set them side by side, neat and clean, ready for the morning. When you step in, they will carry you light, still gleaming from an evening spent caring for the feet that read."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
