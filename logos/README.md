# Client and partner logo assets

This folder contains the logo assets used by the scrolling marquees on the About and Careers pages.

## Organisations represented

The organisation list follows the existing V3 homepage's "Organisations we have worked with" section, with Hub360 Limited and Fifth Ascendant Group added as separately confirmed by the business owner:

- Eric Kayser
- Autochek
- NovaTrack
- Rytegate Technologies
- Shine Shine Cosmetics
- Hub360 Limited
- Fifth Ascendant Group

Algorism Limited and VDT Communications have been removed from the list. They must not be presented as AgileTalent clients or organisations worked with.

## Logo sources and maintenance

The shared manifest is `logos.json`. Each entry can use either:
- `file`: a logo file stored in this folder; or
- `src`: a direct image URL supplied or verified for that organisation.

The About and Careers marquees read from the same manifest automatically. To add an organisation later, upload its image to this folder and add its name and filename to `logos.json`. No HTML or JavaScript edits are needed.

Use accurate organisation names, preserve logo proportions, and keep the marks compact. Do not add an organisation to this list unless the business owner confirms the working relationship. If a remote image source changes or becomes unavailable, replace it with a locally stored image file.
