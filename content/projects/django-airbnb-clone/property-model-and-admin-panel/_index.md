---
_db_id: 548
available_flavours:
- django
content_type: project
from_repo: projects/django-airbnb-clone/intro
prerequisites:
  hard:
  - projects/django-airbnb-clone/calandar-widget
  - projects/django-airbnb-clone/data-export-script
  - projects/django-airbnb-clone/intro
  - projects/django-airbnb-clone/property-model-and-admin-panel
  - projects/django-airbnb-clone/property-owner-dashboard-apis
  - projects/django-airbnb-clone/property-owner-dashboard-ui
  - projects/django-airbnb-clone/property-search
  - projects/django-airbnb-clone/rest-endpoints
  - projects/django-airbnb-clone/user-registration
  - projects/django-airbnb-clone/users-can-crud-properties
  - projects/django-airbnb-clone/users-can-make-bookings
  soft: []
submission_type: continue_repo
title: CloudBnb - Basic Property model and admin panel
---

## Instructions

### Setup

Make use of Postgres. Postgres should be running in a docker container.

### Your first model

In this part of the project you need to implement a few models. Your first model should be called `Property`. This model would represent something that can be rented out temporarily.

Every Property has the following data associalted with it:

- a description
- pictures (more than one). One picture should be selected as the primary/fvorate image
- city
- suburb
- street address
- maximum number of guests
- price per night for one guest
- price per night per extra guest
- a bunch of Tags (use this: https://django-taggit.readthedocs.io/en/latest/). The tags can say things like "internet", "washing machine", "tv", "dstv", "

### Admin panel

Make sure that you can access this data through the admin panel. Create a few properties and add some tags to be sure.

## Migration files

Make sure you commit your migration files to the repo