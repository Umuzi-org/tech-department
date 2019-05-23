#!/bin/sh

hugo
grep -r "contentlink-missing" public
MISSING=$(grep -r "contentlink-missing" public)
# echo $MISSING
