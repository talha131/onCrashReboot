## onCrash = "Reboot();

[![Netlify Status](https://api.netlify.com/api/v1/badges/f8b6454d-b64f-45ff-a0c6-de28791568d4/deploy-status)](https://app.netlify.com/sites/oncrashreboot/deploys)

This repository serves the redirect site for [onCrashReboot.com](https://www.oncrashreboot.com/).

The site has permanently moved to [talhamansoor.com](https://talhamansoor.com/). All URLs redirect automatically to their equivalent pages on the new domain.

## How it works

- `static/index.html` — "We've moved" landing page shown at the root URL
- `static/_redirects` — Netlify redirect rules; all paths are 301-redirected to `talhamansoor.com`

## License

Code in this repository is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license.
