# omasheet.org

Jekyll source for the [omasheet.org](https://omasheet.org) website, built on the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/) remote theme.

Getting Started and the Guide are pulled in at build time from [`librasteve/omasheet`](https://github.com/librasteve/omasheet) (a git submodule at `external/omasheet`, see `.gitmodules`) via `include_relative`, not duplicated here. `.github/workflows/pages.yml` rebuilds and deploys to GitHub Pages on every push to `main`, and once a day on a schedule so upstream README/docs changes show up without a push here.

`include`/`include_relative` always render the included file as a Liquid template, and some of those upstream docs (`docs/interop.md`) use literal `{{ ... }}` syntax for omasheet's own markdown-report templating, which collides with Liquid's own tag syntax. The build workflow runs `scripts/escape_liquid.rb` against the submodule checkout (never committed upstream) to wrap those files in `{% raw %}` before Jekyll sees them. **To preview locally**, run that script against `external/omasheet/` first (see the workflow for the exact file list), and don't commit from inside the submodule afterwards -- it's now wrapped for the build only.

---

## Troubleshooting

If you have a question about using Jekyll, start a discussion on the [Jekyll Forum](https://talk.jekyllrb.com/) or [StackOverflow](https://stackoverflow.com/questions/tagged/jekyll). Other resources:

- [Ruby 101](https://jekyllrb.com/docs/ruby-101/)
- [Setting up a Jekyll site with GitHub Pages](https://jekyllrb.com/docs/github-pages/)
- [Configuring GitHub Metadata](https://github.com/jekyll/github-metadata/blob/master/docs/configuration.md#configuration) to work properly when developing locally and avoid `No GitHub API authentication could be found. Some fields may be missing or have incorrect data.` warnings.
