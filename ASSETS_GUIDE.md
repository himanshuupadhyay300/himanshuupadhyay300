# Supporting files for the GitHub profile README

The profile README references these local image paths:

- `assets/banner.svg` — profile header banner (required)
- `assets/stack.svg` — categorized technology-stack graphic (required by this README version)

Optional reusable assets:

- `assets/btn-linkedin.svg` — LinkedIn button graphic
- `assets/btn-email.svg` — email button graphic
- `tools/make_assets.py` — original Python standard-library script for regenerating the SVG assets

## Upload layout

Keep the directory structure exactly like this in the special profile repository:

```text
himanshuupadhyay300/
├── README.md
├── PROFILE_CHECKLIST.md        (optional)
├── ASSETS_GUIDE.md             (optional)
├── assets/
│   ├── banner.svg
│   ├── stack.svg
│   ├── btn-linkedin.svg
│   └── btn-email.svg
└── tools/
    └── make_assets.py          (optional)
```

Do not rename the two required SVG files unless you also update their `src` paths in `README.md`.
