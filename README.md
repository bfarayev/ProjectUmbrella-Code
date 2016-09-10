# Contents

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Contents](#contents)
- [Administration](#administration)
	- [Steps to get started:](#steps-to-get-started)
	- [Register a 'Superuser' account](#register-a-superuser-account)
- [Umbrella application](#umbrella-application)
	- [Node Package Manager (npm)](#node-package-manager-npm)
		- [Dependencies & `packages.json`](#dependencies-packagesjson)
	- [Bootstrap](#bootstrap)
	- [Postgresql Set up](#postgresql-set-up)
	- [GeoDjango](#geodjango)

<!-- /TOC -->

# Administration
## Steps to get started:
1. Navigate to the `ProjectUmbrella-Code` root directory
2. Run a local server via `python manage.py runserver`
  - Note 1: On Ubuntu you may have to specify python3 explicitly: `python3 manage.py runserver`
  - Note 2: You can tell the server to run on a port different to the default (which is Port 8000) by using: `python manage.py runserver 8080`
3. Current valid directories include:
  - url = `localhost:8000` for the umbrella application
  - url = `localhost:8000/polls` for polls application
  - url = `localhost:8000/admin`  for administration


## Register a 'Superuser' account
You will probably need a superuser account on the django admin panel at some point so:
1. Run `python manage.py createsuperuser` to create super user.
2. Follow the prompts.

# Umbrella application
Currently the Umbrella app points to the root of the webserver e.g. on localhost it is `127.0.0.1:8000`. You should be greeted by the index page (index.html duh).

## Node Package Manager (npm)
We'll be using npm to manage packages and dependencies e.g. Bootstrap - hich is what we will use to style our HTML with.
It uses a `packages.json` file to keep track of package versions used, much the same as the `requirements.txt` file that is used by Python to keep track of package versioning to ensure consistency ([more info here](https://pip.readthedocs.io/en/1.1/requirements.html)).

To download `npm` on Ubuntu:
```
sudo apt-get install npm
```
On Mac: [Visit this article](http://blog.teamtreehouse.com/install-node-js-npm-mac)

Navigate to the `ProjectUmbrella-Code` root directory and run `npm install` and npm will install the dependencies from the `packages.json` file.

### Dependencies & `packages.json`
Not going to re-invent the wheel, here is the npm documentation on [getting started with `package.json`](https://docs.npmjs.com/getting-started/using-a-package.json) and more detailed stuff on specifying dependencies [here](https://docs.npmjs.com/files/package.json)

## Bootstrap
Bootstrap has some really good demos/examples that can be found [here](http://getbootstrap.com/css/)

## Postgresql Set up
Haven't done this yet, been looking here to start off with: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

For MAC, have a look at:http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#create-database

## GeoDjango
Just leaving some GeoDjango links here that might be helpful:
http://invisibleroads.com/tutorials/geodjango-googlemaps-build.html
https://docs.djangoproject.com/en/1.10/ref/contrib/gis/tutorial/

For MAC someone finished the `Postgresql Set up`, download `postgis`
here:http://postgis.net/install/

## Steps for Postgresql
following http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#create-database
1. Once you have the `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD` of Postgresql.
2. root to your virtual-environment, added to `postactivate`, it should be in `your-virtual-environment/bin`:
```
export DATABASE_NAME='Your-data-base-name'
export DATABASE_USER='Your-user-name'
export DATABASE_PASSWORD='Your-user-password'
```
3. reactivate your virtual-environment

## Steps for GeoDjango tutorial
1. Installing `postgis` in http://postgis.net/install/
2. following the suggestion in the postgis install page, run `psql` in terminal, run following code:
```
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
CREATE EXTENSION fuzzystrmatch;
CREATE EXTENSION postgis_tiger_geocoder;
ALTER EXTENSION postgis
 UPDATE TO "2.2.2";
ALTER EXTENSION postgis_topology
 UPDATE TO "2.2.2";
ALTER EXTENSION postgis_tiger_geocoder
 UPDATE TO "2.2.2";
```
3. try to `brew` following
```
$ brew install gdal
$ brew install libgeoip
```
4. It should work then.

## Googlemap view
1. `python3 manage.py runserver`
2. open `localhost:8000`
3. move mouse to `Get Started`, click `View map`, remember to allow it to locate your position. (google map based on javascript, almost dead here)
