# frozen_string_literal: true

source "https://rubygems.org"

# gem "rails"
gem "jekyll", "~> 4.3.4"
gem "minima", "~> 2.5"
gem 'sass-embedded'

group :jekyll_plugins do
    gem 'jekyll-sitemap'
    gem 'jekyll-feed'
    gem 'jekyll-seo-tag'
end

gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
gem "webrick", ">= 1.8.2"

platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end