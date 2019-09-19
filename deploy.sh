#!/bin/sh

rm -r docs
hugo
mv public docs
cd docs
git add .
git commit -m "deploy"
git push