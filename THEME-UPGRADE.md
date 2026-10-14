# Academic Pages upgrade

Upstream: https://github.com/academicpages/academicpages.github.io

Snapshot: c77da751a8124450d5fb818056c0cf081fea08e1 (11 September 2026).
This records the latest upstream commit at migration time; upstream version labels are not consistent across its documentation and package manifest.

Imported current layouts, includes, Sass organization, JavaScript, Font Awesome assets, UI translations, Gemfile and npm build definition. No pages, posts, publications, talks, navigation links, images or downloads were replaced.

## Personal integrations

- `_sass/_site-custom.scss` preserves the light palette, tutorial readability, keyboard focus, and sidebar spacing.
- `head/custom.html` retains the personal favicons, local Academicons and MathJax configuration.
- `archive-single.html` and `single.html` preserve concise publication cards and one citation per detail page.
- The original linked-image lightbox and responsive video plugins remain included in the rebuilt JavaScript bundle.
- The theme switch is keyboard accessible; the initial light appearance is retained, with an optional dark theme.
- The contact address and obfuscated page text, content, permalinks, metadata, PDFs and tutorial screenshots are unchanged.

## Maintenance

Run `npm ci` and `npm run build:js` after changing JavaScript. Run `bundle install` and `bundle exec jekyll build` for a local Jekyll build. The pull-request workflow checks the GitHub Pages Jekyll build and generated routes/assets before changes are merged.

Keep these integrations when comparing against a future upstream snapshot. Do not copy upstream demo content or personal-profile configuration into this repository.
