# Jekyll's built-in include_relative tag renders the included file as a
# Liquid template, so literal "{{ ... }}" syntax inside it -- e.g. the
# Markdown-report placeholder syntax shown in docs/interop.md, such as
# "{{ Sales.Revenue.sum() }}" -- gets parsed as real Liquid and breaks
# the build (method-call syntax isn't valid inside a Liquid output tag).
# This tag inlines the file's raw bytes with no Liquid pass at all, so
# upstream docs can use whatever syntax they want without the website
# build needing to know about it.
module Jekyll
  class IncludeRelativeRawTag < Liquid::Tag
    def initialize(tag_name, text, tokens)
      super
      @relative_path = text.strip
    end

    def render(context)
      site = context.registers[:site]
      File.read(File.join(site.source, @relative_path))
    end
  end
end

Liquid::Template.register_tag('include_relative_raw', Jekyll::IncludeRelativeRawTag)
