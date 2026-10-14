# Website refresh — 9 September 2026

## Completed

- Preserved the Jekyll / Academic Pages / Minimal Mistakes architecture, theme, portrait, colors, navigation structure, and established tutorial permalinks.
- Updated the homepage, sidebar description, and CV for the IFSC/USP appointment beginning April 2025. Replaced promotional language with a direct account of research and teaching.
- Reworked the two ssNake processing and fitting tutorials with consistent sections, retained screenshots, current upstream installation links, and clearer scientific qualifications.
- Repaired malformed tags metadata in three tutorials; explicit tags prevent YAML from appending the tag list to the permalink value.
- Labeled Czjzek and WCPMG material as unfinished, retained their content, corrected the central-transition/static-versus-MAS distinction, and removed the unsupported universal 4-sigma grid limit.
- Repaired the LinkedIn URL, repository setting, timezone, three download links, unused favicon references, app manifest identity, and obsolete 404 assistance script.
- Excluded template demonstration pages and portfolio entries from publication while retaining source files.
- Repaired the duplicated publication URL, wrong journal, and unrelated copied abstract in the niobium/aluminophosphate record using the supplied paper22.pdf.
- Added three publication records from existing PDFs: the 2023 Acta Materialia lithium silicate study and the 2024 Biomolecules and lithium niobate glass-ceramic papers.
- Populated the empty resources page, clarified that the bibliography is selected, and identified conference links that refer to earlier editions.
- Added minimal responsive-content and keyboard-focus CSS plus maintenance instructions in README.md.

## Verification

Parsed published front matter and data YAML; checked duplicate explicit permalinks, navigation destinations, literal image/download references, and newly added relative_url links. Checked whitespace with git diff --check. These checks passed.

A full Jekyll build and visual browser check have NOT been performed. Ruby and Bundler are absent from this environment; attempting to install the runtime failed because the package manager could not switch users. Build with bundle install followed by bundle exec jekyll build before publishing. Existing dependencies were preserved, with no speculative version upgrades.

Software installation sources checked: the old GitHub README and current GitLab README at https://gitlab.science.ru.nl/mrrc/nmrzoo/ssnake/-/blob/master/README.md. Interactive ssNake workflows were not rerun. Publication corrections/additions use the PDFs already in files/. Crossref reports the 2024 glass-ceramic article's issue date as October 2024; its record uses October 1 for sorting, not as an independently verified exact publication day.

## Remaining content decisions

- Complete the Czjzek worked example with an actual downloadable dataset, acquisition settings, grid settings, fitted values, and screenshots. Its public text currently states that it is a working draft.
- Complete the WCPMG tutorial, which previously contained only an introduction.
- Supply a verified publication export or DOI list to bring selected publications through 2025–2026; no unpublished manuscripts or private collaboration plans were added.
- Refresh the selected talks and media entries with items you want publicly listed.
- Historical conference links remain explicitly identified as past editions. They have not all been externally checked.
- Existing analytics configuration still references a UA identifier; any analytics migration needs the intended replacement property. The inherited terms/privacy page also needs a separate factual review against the tracking setup you choose.

## Review and apply

No changes were pushed to GitHub or published. Work was prepared on local branch cleanup/site-refresh-2026-09.

The full-source ZIP contains the edited site and all existing assets, excluding Git history, editor state, and generated output. The changes-only ZIP contains only changed/new source files and can be overlaid onto a backup copy of the repository. No tracked files were deleted. Both include this review note, which is excluded from the generated website.
