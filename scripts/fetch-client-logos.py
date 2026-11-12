import io, json, os, re, sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from PIL import Image

ROOT = Path("logos")
ROOT.mkdir(exist_ok=True)
SITES = [
    ("eric-kayser", "Eric Kayser", "https://www.maison-kayser.com/gb/"),
    ("autochek", "Autochek", "https://www.autochek.africa/ng/"),
    ("novatrack", "NovaTrack", "https://www.novatrack.net/"),
    ("rytegate-technologies", "RyteGate Technologies", "https://www.rytegate.com/"),
    ("shine-shine-cosmetics", "Shine Shine Cosmetics", None),
    ("algorism", "Algorism Limited", "https://www.algorismng.com/"),
    ("vdt-communications", "VDT Communications", "https://vdtcomms.com/"),
    ("hub360", "Hub360 Circuits Limited", "https://hub360.cc/"),
    ("fifth-ascendant-group", "Fifth Ascendant Group", "https://fivestones.ng/"),
]
session = requests.Session()
session.headers.update({"User-Agent":"Mozilla/5.0 (compatible; AgileTalentLogoAssetBot/1.0)"})
results = []
for slug, name, page_url in SITES:
    if not page_url:
        results.append({"name":name,"status":"skipped","reason":"No verified official website located; no third-party logo substituted."})
        continue
    try:
        response = session.get(page_url, timeout=25)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        candidates = []
        header = soup.find("header")
        scopes = [header] if header else []
        scopes += [soup]
        seen = set()
        for scope in scopes:
            for img in scope.find_all("img"):
                src = img.get("src") or img.get("data-src") or img.get("data-lazy-src")
                if not src: continue
                absolute = urljoin(response.url, src)
                if absolute in seen: continue
                seen.add(absolute)
                marker = " ".join([str(img.get("alt","")), str(img.get("title","")), str(img.get("class","")), absolute]).lower()
                score = 0
                if "logo" in marker: score += 10
                if scope is header: score += 5
                if any(x in marker for x in ["icon", "favicon", "avatar", "product", "banner", "slider"]): score -= 8
                candidates.append((score, absolute, marker))
        candidates.sort(reverse=True)
        chosen = None
        for score, image_url, marker in candidates:
            if score < 5: continue
            try:
                asset = session.get(image_url, timeout=25)
                asset.raise_for_status()
                content_type = asset.headers.get("content-type","").lower()
                if not content_type.startswith("image/"): continue
                if "svg" in content_type or image_url.lower().split("?")[0].endswith(".svg"):
                    if b"<svg" not in asset.content[:2000].lower(): continue
                    out = ROOT / f"{slug}.svg"
                    out.write_bytes(asset.content)
                    chosen = out.name
                    break
                image = Image.open(io.BytesIO(asset.content))
                image.load()
                if image.width < 80 or image.height < 30: continue
                if image.width > 5000 or image.height > 5000: continue
                image = image.convert("RGBA")
                out = ROOT / f"{slug}.png"
                image.save(out, format="PNG", optimize=True)
                chosen = out.name
                break
            except Exception:
                continue
        if chosen:
            results.append({"name":name,"status":"downloaded","file":chosen,"source":response.url})
            print(f"FOUND {name}: {chosen} from {response.url}")
        else:
            results.append({"name":name,"status":"not-found","reason":"Official site returned no clear logo image asset; left blank rather than guessing."})
            print(f"NOT FOUND {name}: no unambiguous logo image")
    except Exception as exc:
        results.append({"name":name,"status":"not-found","reason":str(exc)[:180]})
        print(f"FAILED {name}: {exc}")
(ROOT / "fetch-results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2))
