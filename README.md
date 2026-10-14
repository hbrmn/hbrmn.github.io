# Henrik Bradtmüller’s website

Jekyll website hosted at https://hbrmn.github.io, based on Academic Pages / Minimal Mistakes.

## Content map

- `_config.yml`: identity, social profiles, collections, and build settings.
- `_data/navigation.yml`: main navigation.
- `_pages/`: biography, CV, publication index, and resource pages.
- `_posts/`: NMR tutorials. Keep existing permalinks when editing published posts.
- `_publications/` and `_talks/`: individual publication and presentation records.
- `images/` and `files/`: screenshots, figures, manuscripts, and downloads.
- `_includes/`, `_layouts/`, `_sass/`, and `assets/`: shared theme and behavior.

## Local build

Install Ruby and Bundler, then run:

```sh
bundle install
bundle exec jekyll build
bundle exec jekyll serve
```

The Gemfile uses `github-pages` to match GitHub Pages dependencies. Avoid updating vendored theme libraries independently without checking the built site.

## Editing

Use valid YAML front matter, including an explicit `tags:` key for tag lists. Keep dates as `YYYY-MM-DD`. Set `published: false` for material that should remain in source but should not appear on the website. Use `relative_url` for new internal links. Preserve screenshot and download filenames unless all references are updated.

The two older ssNake tutorials retain their existing dates and URLs. Their screenshots are historical examples, not a claim of testing against the newest release. The Czjzek guide is marked as a working draft pending example data and screenshots. Publication records are selected historical entries; do not treat the collection as an automatically updated bibliography.
