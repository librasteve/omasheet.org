#!/usr/bin/env ruby
# Jekyll's include/include_relative tags always render the included file
# as a Liquid template -- including under the github-pages gem's forced
# safe mode, which rules out a custom plugin to change that behavior.
# Upstream docs (e.g. docs/interop.md) use literal "{{ ... }}" syntax for
# omasheet's own markdown-report templating, which Liquid then tries to
# parse as its own output tags and fails on.
#
# This wraps each given file's entire content in {% raw %}...{% endraw %}
# (both stock, safe-mode-allowed Liquid tags) so that syntax passes
# through as plain text. It runs against the CI's ephemeral submodule
# checkout only, right before the Jekyll build -- never against the
# submodule's own git history, so the upstream repo's docs stay exactly
# as written when read directly on GitHub or anywhere else.
ARGV.each do |path|
  content = File.read(path)
  next if content.start_with?("{% raw %}")

  File.write(path, "{% raw %}\n#{content}\n{% endraw %}\n")
end
