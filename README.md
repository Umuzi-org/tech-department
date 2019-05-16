# Tech department content

This is a hugo based web site. You can see the site [HERE](https://master.d3hv5c7o5j7vym.amplifyapp.com)

This repo aims to contain all the info needed to run Umuzi's tecnical courses. This is very much a work in progress.

## To clone this repo

There is a submodule in here so clone recursively:

```
git clone --recursive git@github.com:Umuzi-org/tech-department.git
```

## running locally

This is a hugo based application. To get yourself set up on a debian machine:

```
sudo apt install golang
./install_hugo.sh
```

To run the development server:

```
hugo server
```

## syllabus docs:

look inside /content. The documentation is composed of a bunch of markdown files with a lil metadata.

## Contributing

You can contribute in a few different ways:

### you can add or edit course materials

All our course materials live inside the `content` directory.

Please DO NOT put large binary files into this repo. For example PDFs and Presentations and work documents aren't cool.

#### Adding new materials

Let's say you want to add a self-study introduction to Python Flask. You would do something like this:

1. make a directory. This path would make sense: `content/topics/intro-to-flask`
2. make a markdown file inside your new directory called `_index.md`
3. start your markdow file with the following:

```
---
topic: Introduction to Flask
---
```

### you can upgrade the look and feel of this site

For the most part the best place to do this is in the layouts directory.

DO NOT EVER make changes directly in the public directory. If you do this your changes will be descroyed. Everything in public gets generated automagically so your stuff will just get over-written.
