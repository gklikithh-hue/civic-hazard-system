import re

HAZARD_KEYWORDS = {
    "pothole": ["pothole", "broken road", "road damage", "crack in road", "deep hole"],
    "open_manhole": ["open manhole", "manhole", "missing cover", "exposed drainage"],
    "exposed_wire": ["electric wire", "exposed wire", "live wire", "electrical cable", "sparking wire"],
    "waterlogging": ["waterlogging", "flooded road", "water on road", "stagnant water", "logged street"],
    "garbage_blocked_drain": ["garbage blocked drain", "drain blocked", "clogged drain", "trash in drain", "blocked drainage"],
    "damaged_streetlight": ["streetlight", "damaged light", "broken pole", "dark street light", "non working streetlight"],
    "broken_footpath": ["broken footpath", "damaged sidewalk", "cracked pavement", "raised sidewalk", "unsafe footpath"],
    "garbage_dump": ["garbage", "trash", "dumping", "overflowing bins", "waste accumulation"]
}

def detect_hazard(filename: str, description: str = "", image_bytes: bytes | None = None) -> str:
    text = f"{filename or ''} {description or ''}".lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    for hazard_name, keywords in HAZARD_KEYWORDS.items():
        if any(keyword in text for keyword in keywords):
            return hazard_name

    return "garbage_dump"
