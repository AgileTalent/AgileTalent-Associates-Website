import io, json
from pathlib import Path
import requests
from PIL import Image

ROOT = Path("logos")
ROOT.mkdir(exist_ok=True)
SOURCES = [
    ("Eric Kayser", "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=61579593071897", "eric-kayser.png", "eric-kayser.svg"),
    ("NovaTrack", "https://lookaside.fbsbx.com/lookaside/crawler/media/?media_id=61583801346451", "novatrack.png", None),
    ("Rytegate Technologies", "https://pbs.twimg.com/profile_images/981160788160385025/h1L66k7m_400x400.jpg", "rytegate-technologies.png", "rytegate-technologies.jpg"),
    ("Shine Shine Cosmetics", "https://www.shineshinecosmetics.net/cdn/shop/files/Screenshot_2023-03-16_125626-removebg-preview_0b8b92f7-6266-4921-b3e6-09b3c275d907.png?v=1711235292", "shine-shine-cosmetics.png", None),
    ("Hub360 Limited", "https://asoc.com.ng/logos/hub360.png", "hub360.png", None),
    ("Fifth Ascendant Group", "https://thefifthascendantgroup.com/companies/fivestones.png", "fifth-ascendant-group.png", "fifth-ascendant-group.svg"),
]
session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})
results = []
for name, url, filename, fallback in SOURCES:
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))
        image.load()
        if image.width < 40 or image.height < 30 or image.width > 6000 or image.height > 6000:
            raise ValueError("Image dimensions are outside the accepted range")
        image = image.convert("RGBA")
        image.save(ROOT / filename, format="PNG", optimize=True)
        results.append({"name": name, "status": "downloaded", "file": filename})
        print(f"DOWNLOADED {name} -> {filename}")
    except Exception as exc:
        if fallback and (ROOT / fallback).exists():
            results.append({"name": name, "status": "fallback-local", "file": fallback, "reason": str(exc)[:180]})
            print(f"USING EXISTING LOCAL LOGO FOR {name}: {fallback}")
        else:
            results.append({"name": name, "status": "failed", "file": None, "reason": str(exc)[:180]})
            print(f"FAILED {name}: {exc}")

(ROOT / "fetch-results.json").write_text(json.dumps(results, indent=2) + "\\n", encoding="utf-8")
manifest_path = ROOT / "logos.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
resolved = {item["name"]: item["file"] for item in results if item.get("file")}
for item in manifest:
    if item["name"] in resolved:
        item["file"] = resolved[item["name"]]
manifest_path.write_text(json.dumps(manifest, indent=2) + "\\n", encoding="utf-8")
