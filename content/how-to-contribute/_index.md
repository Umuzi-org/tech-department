---
title: How to Contribute
---

If you want to contribute content to this repo there are a few things you need to know.


## Don't make any changes to the public/ directory

This is really important. It might be tempting to you to write some html, js or css in there. Resist that temptation. This is a hugo based website. This means that the public directory is generated automagically. Any changes you make within the public directory wil be overwritten.

## If you want to make changes to look and feel or basic site functionslity

This gets interesting. Basically, hugo allows the use of themes. The theme we are using is called `hugo-theme-learn` and you can find it inside the `themes` directory in this repo.  So most of the visual elements you see when looking at this website is generated through use of that theme.

If you want to override anything about how the theme behaves (maybe changing a color or layout, or adding a functionality) then DO NOT directly edit the theme files. Your changes might be overwritten because the theme itself is not really a part of this code repository. It is a git submdule. As cool as git submodules are, they're a little out of scope for this discussion.

If you want to change how a theme behaves then you need to override that behavior WITHOUT directly editing the theme.

Take a look at this directory structure:

```
.
├── archetypes
├── config.toml
├── content
├── install_hugo.sh
├── layouts
├── LICENSE.md
├── public
├── README.md
├── resources
├── static
└── themes
    └── hugo-theme-learn
        ├── archetypes
        ├── CHANGELOG.md
        ├── exampleSite
        ├── i18n
        ├── images
        ├── layouts
        ├── LICENSE.md
        ├── netlify.toml
        ├── README.md
        ├── static
        ├── theme.toml
        └── wercker.yml
```

This is a summary of the directory structure of this application. You'll notice that the structure of the plugin is very similar to the structure of the repo as a whole. If you want to override a piece of the theme's functionality then you need to find the file in the theme that defines that functionality, then make a file with an equivalent path in the main repo. This might sound weird but it's pretty easy to get the hang of.

Have an example:

Let's say we want to change what the menu looks like. Ypu would do something like this:

```
cp themes/hugo-theme-learn/layouts/partials/menu.html layouts/partials/menu.html
```

Cool, so now we have two copies of `menu.html`. Make your changes to the new one.

```
...
├── config.toml
├── layouts
|   └── partials
|       └── menu.html  ### EDIT THIS ONE
...
└── themes
    └── hugo-theme-learn
        ├── layouts
            └── partials
                └── menu.html ### NOT THIS ONE
    ...
```

Nice eh?

The other thing to know is that hugo is written in go. So these html files are actually go templates. So that's a topic you can read about on your own. Go templates are used in lots of interesting places.

## If you want to make changes to the course content

If you want to change content (eg: you want to update or create a workshop or topic), then you will need to create a markdown file within the content directory. If you don't put your file in the right place it will not show up on the website. If you don't get your metadata right then things wont work out either.



## The syllabus index page

TODO