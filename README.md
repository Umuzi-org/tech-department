# Tech department content

This is a Hugo based web site. You can see the site [HERE](https://umuzi-org.github.io/tech-department/syllabuses/)

This repo aims to contain all the info needed to run Umuzi's technical courses. This is very much a work in progress.

## To clone this repo

There is a submodule in here so clone recursively:

```
git clone --recursive git@github.com:Umuzi-org/tech-department.git
```

## running locally

This is a Hugo based application. To get yourself set up on a Debian machine:

```
sudo apt install golang
./install_hugo.sh
```
MAC

Add this in your bash file e.g zshrc

```
# Go development
export GOPATH="${HOME}/.go"
export GOROOT="$(brew --prefix golang)/libexec"
export PATH="$PATH:${GOPATH}/bin:${GOROOT}/bin"
```
Run these installs in your terminal using Homebrew
```
brew install go
brew install hugo -> look for version 0.51
``` 

To run the development server:

```
hugo serve -b "http://localhost:1313/"
```

## syllabus docs

look inside /content. The documentation is composed of a bunch of markdown files with a lil metadata.

## Contributing

Please make sure that your contributions actually work and look good. If you edit some stuff then run the hugo server locally. Look at your changes in the browser.

You can contribute in a few different ways:

### You can add or edit course materials

All our course materials live inside the `content` directory.

Please DO NOT put large binary files into this repo. For example PDFs and Presentations and word documents aren't cool.

#### Adding new materials

Let's say you want to add a self-study introduction to Python Flask. You would do something like this:

1. make a directory. This path would make sense: `content/topics/intro-to-flask`
2. make a markdown file inside your new directory called `_index.md`
3. start your markdown file with the following:

```
---
topic: Introduction to Flask
ready: true
---
```

The `ready:true` part tells hugo that this is not a draft, it is ready for human consumption.

If you add anything inside the `content/projects` directory then it will automatically get rendered with a link to a submission form at the top of the page. If you want to suppress this behavior then use the frontmatter:

```
noform: true
```

Take a look at http://localhost:1313/projects/nodejs/ to see this in action

### you can upgrade the look and feel of this site

For the most part the best place to do this is in the layouts directory.

DO NOT EVER make changes directly in the public directory. If you do this your changes will be destroyed. Everything in public gets generated auto-magically so your stuff will just get over-written.

### Lint

To set up your environment:

```
mkvirtualenv -p $(which python3.7) umuzi-tech-dept
pip install -r requirements.txt
```

Run `python3.7 lint.py` to make sure all your markdown frontmatter is ok.
