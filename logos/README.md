# Client and partner logo assets

This folder stores the official logo image files used by the scrolling organisation marquees on the About and Careers pages.

## File names currently referenced

Add the official logo files using these exact names:

- `eric-kayser.png`
- `autochek.png`
- `novatrack.png`
- `rytegate-technologies.png`
- `shine-shine-cosmetics.png`
- `algorism.png`
- `vdt-communications.png`
- `hub360.png`
- `fifth-ascendant-group.png`

## Adding another organisation later

1. Upload the official logo image into this folder.
2. Open `logos/logos.json` and add one object to the list, using the logo's exact file name and the organisation's display name. Example:
   `{"name":"New Client Limited","file":"new-client.png"}`
3. Save the change. The About and Careers marquees read from this shared manifest automatically; you do not need to edit either page.

Use transparent PNG or SVG where possible, preserve the original aspect ratio, and keep the logo treatment compact. Do not stretch, recolour, redraw or otherwise alter an organisation's official brand mark. Confirm permission or an appropriate basis to display each logo.
