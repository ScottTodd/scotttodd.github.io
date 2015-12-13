source 'https://rubygems.org'
gem 'github-pages'
gem 'jekyll-mentions'

require 'rbconfig'
gem 'wdm', '~> 0.1.0' if RbConfig::CONFIG['target_os'] =~ /mswin|mingw/i
gem 'listen', '2.7.6' if RbConfig::CONFIG['target_os'] =~ /mswin|mingw/i

gem 'sass', '~> 3.4.1'
gem 'scss_lint'

gem 'colorize'

# Fix for this error (listen gem requires celluloid >= 0.15.2):
#   Celluloid 0.17.0 is running in BACKPORTED mode. [ http://git.io/vJf3J2 ]
#   jekyll 2.5.3 | Error: wrong number of arguments (2 for 1)
gem 'celluloid', '0.16.0'
