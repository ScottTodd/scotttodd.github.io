scotttodd.github.io
===================

This is the source for my [website](http://scotttodd.github.io/).

It uses [GitHub Pages](https://pages.github.com/) for easy hosting, [Jekyll](http://jekyllrb.com/) for static site generation, and [Jekyll Bootstrap](http://jekyllbootstrap.com/) for its many blog features and theming support.

To build a similar site, check out GitHub's [Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages) and Jekyll Bootstrap's [Jekyll Quickstart](http://jekyllbootstrap.com/usage/jekyll-quick-start.html).

Development Instructions
-----

First time build (Windows 10):

1. Install Ruby: [official website](https://www.ruby-lang.org/en/documentation/installation/). Tested on 2.7.4 (see what the GitHub Pages gem uses).
2. Install the Ruby Development Kit from [here](http://rubyinstaller.org/downloads), following the instructions [here](http://github.com/oneclick/rubyinstaller/wiki/Development-Kit).
3. ```gem install bundler```
4. ```bundle update```
5. ```bundle install```

Updating/managing gems:

* ```gem list```
* ```gem dependency```
* ```gem update github-pages```, see GitHub Pages [Dependency versions](https://pages.github.com/versions/)
* ```bundle update```

Standard workflow commands:

* ```rake server``` (supports livereload)
* ```rake test```
* ```rake lint```

Or run directly:

* ```bundle exec jekyll serve --livereload``` (easier to terminate)

Directory Structure
-------------------

I mostly use the basic [Jekyll structure](http://jekyllrb.com/docs/structure/).

The 'custom' theme is forked from the 'twitter' theme.

Here are the main areas that I've worked in:

```
├─── pages (general webpages)
├─── _posts (project webpages)
├─── assets (supporting non-text content)
│   ├─── css
│   ├─── images
│   ├─── js
│   ├─── projects
│   └─── themes
│       └─── custom
└─── _includes (layouts and page templates)
    └─── themes
        └─── custom
```

License
-------

This site is open sourced under the [MIT license](http://opensource.org/licenses/MIT), though the projects showcased may have their own licenses.
