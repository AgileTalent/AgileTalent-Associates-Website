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

1. Upload its official logo to this folder (prefer transparent PNG or SVG; keep the original aspect ratio).
2. Add a matching `<li><img ...></li>` entry to the first list in the marquee on both `about/index.html` and `careers/index.html`.
3. Add the same entry to the immediately following `aria-hidden="true"` list. This second list creates the seamless scrolling loop; leave its image alt text empty.
4. Add the organisation's name to each marquee's `aria-label`.

Use a consistent, compact logo treatment. Do not stretch, recolour, redraw or otherwise alter a company's official brand mark. Confirm permission or an appropriate basis to display each logo.
