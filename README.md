scotttodd.github.io
===================

This is the source for my [website](http://scotttodd.github.io/).

It uses [GitHub Pages](https://pages.github.com/) for easy hosting, [Jekyll](http://jekyllrb.com/) for static site generation, and [Jekyll Bootstrap](https://github.com/plusjade/jekyll-bootstrap) for its many blog features and theming support.

To build a similar site, check out GitHub's [Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages).

Development Instructions
-----

First time build (Windows 10):

1. Install Ruby: [official website](https://www.ruby-lang.org/en/documentation/installation/). Tested on 3.4.5 (see what the GitHub Pages gem uses).
2. ```gem install bundler```
3. ```bundle update```
4. ```bundle install```

Updating/managing gems:

* ```gem list```
* ```gem dependency```
* ```gem update github-pages```, see GitHub Pages [Dependency versions](https://pages.github.com/versions.json)
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
