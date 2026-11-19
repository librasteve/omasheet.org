# Omasheet.org: messages and links

One sentence per block on the homepage (`index.html`), in page order, then every link the site carries. Edit the sentence here first, then the page.

## Homepage messages

- **Nav**: Everything you need is one click away: features, command line, install, guide, posts and source code.
- **Hero (badge, headline, lead)**: What Markdown is to words, Omasheet is to numbers: a text-native spreadsheet for technical workflows, with exact arithmetic, SI units, scientific uncertainty and typed columns, in files you can diff, review and hand to an AI.
- **Hero buttons**: Install it now, or star the project on GitHub.
- **Hero screenshot**: This is the app: a Sales sheet where Profit, Tax and Running are calculated columns, defined once and checked as you work.
- **Facts strip**: One Rust binary for macOS, Windows and Linux, built on Polars. No account, no cloud, open source under the MIT licence.

### Section: What a binary workbook cannot do

Formulas are written once per column, files are plain text, and numbers keep their meaning. A spreadsheet you can understand, check, version and automate.

- **Feature 1, Text: The file is the spreadsheet**: An .omx file is readable text that diffs cleanly in Git, reviews like code and reads like a small typed program over its own data.
- **Feature 2, Units: Numbers that know their dimensions**: `5kg + 300g` is `5.3kg`; `5kg + 3m` is an error that explains why. Dimensional analysis catches mistakes before they become plausible results.
- **Feature 3, Types: Exact numbers, scientific meaning**: Fractions are exact without limit, Decimals keep money to the penny, and scientific notation carries uncertainty. From `1/3 + 1/6 = 1/2` to CODATA constants, numbers mean what they say.
- **Feature 4, Reports: Markdown in, finished report out**: Put a sheet inside a Markdown document and render it to HTML, so calculations, data and explanation live together in one reviewable file.
- **Feature 5, AI: Spreadsheets built for agents**: An agent skill lets Claude and friends write .omx files that are checked for types and units, turning many silent spreadsheet mistakes into explicit errors.

### Section: And the rest (six cards)

- **Windowed columns**: `cum_sum`, `diff`, `rank` and `rolling_mean` run on Polars, with partitioning using `by`.
- **Built-in constants**: `pi`, `c`, `planck`, `kB` and `NA` are ready in every file, drawing on the 2019 SI and CODATA 2022.
- **Real interchange**: Import and export XLSX, CSV, JSON and Parquet, preserving types and units wherever the format allows.
- **Booleans and logic**: Symbol formats such as ticks and crosses, logic functions and gate operators, all directly in the grid.
- **Native, everywhere**: One Rust binary with a Qt app for macOS, Windows, Arch and Omarchy, following your dark and light mode.
- **Listed in OmaStore**: Find Omasheet under Office in the Omarchy community app store and install it with one click.

### Remaining sections

- **Latest posts**: The three newest posts, each with a summary, lead to the full collection of notes on building a better spreadsheet.
- **The same on the command line**: Everything the app does is scriptable, so sheets work in CI, Git hooks and AI-agent loops.
- **Install**: One line installs it on macOS, Omarchy, Arch and Windows, the same line updates it, and releases are checksummed with build provenance.
- **Install note**: It is early and changing and may contain errors, so there is a build-from-source route and a releases page for anything else.
- **Footer**: Omasheet is MIT licensed, by Stephen Roe, and the site, guide, posts and releases are one link away.

## Other pages

- **Posts index** (`/posts/`): Notes on building Omasheet: why, how, and what you can do with it.
- **Each post**: The title, date and reading time come first, then the one-sentence summary from the post's excerpt, then the post.
- **Getting started** (`/getting-started/`): How to install and run Omasheet, taken from the README.
- **Guide** (`/guide/`): The reference for the file format, expressions, the app and CLI, and import and export, taken from the docs.

## Links on the site

### Site

| Link | URL |
| --- | --- |
| Home | `/` |
| Features (home anchor) | `/#features` |
| Command line (anchor) | `/#cli` |
| Install (anchor) | `/#install` |
| Getting started | `/getting-started/` |
| Guide | `/guide/` |
| Posts | `/posts/` (nav, footer and the homepage's Latest posts section) |
| Posts feed | `/feed.xml` |

### Posts

| Post | URL |
| --- | --- |
| Why Omasheet | `/blog/why-omasheet/` |
| Omasheet on OmaStore | `/blog/on-omastore/` |
| Omasheet & Markdown | `/blog/omasheet-and-markdown/` |
| Markdown Reports | `/blog/markdown-reports/` |
| Starship Flight 15: a Vignette | `/blog/starship-flight15/` |

The video post "A Bank Statement Report" is written but marked `published: false`, so it has no page yet.

### Share pages

One per release, made by the release workflow.

| Release | URL |
| --- | --- |
| Omasheet 0.1.12 | `/r/v0.1.12/` |

### GitHub

| Link | URL |
| --- | --- |
| Repository | https://github.com/librasteve/omasheet |
| Releases | https://github.com/librasteve/omasheet/releases |
| Latest release | https://github.com/librasteve/omasheet/releases/latest |
| Build from source | https://github.com/librasteve/omasheet#install |
| Agent skill | https://github.com/librasteve/omasheet/blob/main/skill/omasheet/SKILL.md |
| Installer, macOS/Linux | https://raw.githubusercontent.com/librasteve/omasheet/main/install.sh |
| Installer, Windows | https://raw.githubusercontent.com/librasteve/omasheet/main/install.ps1 |

### Elsewhere (linked from the posts)

| Link | URL |
| --- | --- |
| OmaStore (in the posts) | https://github.com/KitsuneSemCalda/OmaStore |
| OmaStore (in the README) | https://github.com/KitsuneForgering/OmaStore (the two differ; pick one) |
| librasteve on YouTube | https://www.youtube.com/@librasteve |
| Flight 15 files | https://github.com/librasteve/omasheet/blob/dev/examples/showcase/flight15.omx (also `.md` and `.html`) |

### Not linked yet

The homepage "Listed in OmaStore" card has no link, and there is no link to the Guide or the posts from the hero.
