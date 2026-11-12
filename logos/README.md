# Client and partner logo assets

This folder contains the logo image files used by the scrolling marquees on the About and Careers pages.

## Official logos currently installed

- `eric-kayser.svg` — sourced from Maison Kayser's official website
- `autochek.png` — sourced from Autochek's official website
- `algorism.svg` — sourced from Algorism Limited's official website
- `vdt-communications.png` — sourced from VDT Communications' official website
- `hub360.png` — sourced from Hub360's official website (the site's legal entity name is Hub360 Circuits Limited)
- `fifth-ascendant-group.svg` — sourced from FiveStones, the Fifth Ascendant Group platform

The manifest is `logos.json`. Only entries with a real file are shown in the carousel. The following organisations remain listed but do not yet have a verified official logo asset in this repository: NovaTrack, RyteGate Technologies and Shine Shine Cosmetics. They are deliberately omitted from the visual carousel until a suitable logo can be confirmed.

## Adding another organisation later

1. Upload its official logo image into this folder.
2. Open `logos.json` and add an object with the organisation name and exact filename. Example:
   `{"name":"New Client Limited","file":"new-client.png"}`
3. Save the change. Both About and Careers pages read from this shared manifest automatically; no HTML or JavaScript edits are needed.

Use an official logo file (transparent PNG or SVG where possible), preserve its aspect ratio, and keep it compact. Do not redraw, recolour or stretch the mark. Confirm an appropriate basis or permission to display each organisation's logo.
