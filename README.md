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
	- [Git Team Workflow](#git-team-workflow)
		- [Reviewing a PR](#reviewing-a-pr)

<!-- /TOC -->

# Administration
## Steps to get started:
1. Navigate to the `ProjectUmbrella-Code` root directory
2. Run a local server via `python manage.py runserver`
  - Note 1: On Ubuntu you may have to specify python3 explicitly: `python3 manage.py runserver`
  - Note 2: You can tell the server to run on a port different to the default (which is Port 8000) by using: `python manage.py runserver 8080`
3. Current valid views include:
  - `localhost:8000/`
  - `localhost:8000/googlemaps.html`
  - `localhost:8000/signin.html`
  - `localhost:8000/admin`


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
Make sure you installed Bootstap at this stage. In root folder run `npm install` if you haven't done it already. B

ootstrap has some really good demos/examples that can be found [in this link](http://getbootstrap.com/css/)

## Postgresql Set up
Haven't done this yet, been looking here to start off with: https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04

For MAC, have a look at:http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#create-database

## GeoDjango Tutorials

Some GeoDjango links here that might be helpful:

* [Tutorial 1](http://invisibleroads.com/tutorials/geodjango-googlemaps-build.html)
* [Tutorial 2](https://docs.djangoproject.com/en/1.10/ref/contrib/gis/tutorial/)

## Integrating Postgresql

Please have a look at this before you start: 

* [Tutorial for Mac Users](http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#create-database)
* [Tutorial for Linux Users](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

Summary of what steps explained above (for Mac Users): 

1. Create a Postgres database in PgAdmin3. We need three fields for the next step: `database-name`, `username`, `password` of Postgresql. `username` is the _owner_ and `password` is the _owner_'s passowrd. You may want to keep it simple and use `postgres/ postgres` for that.
2. In your root folder, do `$ vi $VIRTUAL_ENV/bin/postactivate` and add this:

```
export DATABASE_NAME='database-name'
export DATABASE_USER='username'
export DATABASE_PASSWORD='password'
```

3. Now do `$ vi $VIRTUAL_ENV/bin/predeactivate ` and add:

```
unset DATABASE_NAME
unset DATABASE_USER
unset DATABASE_PASSWORD
```

4. Restart (reactivate) your virtual env by `deactivate` and `workon` commands.  

5. To see the Postgres integration, do:

`python3 manage.py check` and then
`python3 manage.py migrate`

6. If 5 worked without errors then you have Postgres integrated successfully! If not, don't waste time and flag it on Slack!


## Steps for GeoDjango tutorial

1. Install `postgis` in following the instructions in [this link](http://postgis.net/install/)
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
4. Done

## Googlemap view
1. `python3 manage.py runserver`
2. open `localhost:8000`
3. move mouse to `Get Started`, click `View map`, remember to allow it to locate your position. (google map based on javascript, almost dead here)

## Git Team Workflow
When working as a team, following a common workflow is essential. [Feature-branch-workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow/) is a very powerful method where team members work on their feature branches, create pull requests and let others review their code before it's pushed to production.

Rules of thumb:

- Merge often. Take small feature to work on. It's not easy to review 1000 lines of code.
- Choose informative branch names like `feature/PostGIS-Integration`,`fix/Database-Error`, `fix/Unit-Tests` etc.
- Don't merge your own PR (Pull Request). Let others review yours.
- Add useful descriptions to your PRs. Make others work easy by doing this. Time is important. If you find something, add it to your PR description.
- `develop` branch is our default base branch.

Simple example on how this workflow should look like in practice:

- Bob wants to integrate PostGIS.
- He does `git checkout -b {branch_name}` which is the same as
 	- `git branch {branch_name}` - Creates new branch called "branch_name"
	- `git checkout {branch_name}` - Checkout branch named "branch_name"
- He does his work, and thinks it’s in a good shape to push to remote and create a PR and let others review it. So, `git push origin {branch_name}`
- Then he opens GitHub -> Clicks `New pull request` -> (Base should be and will be `develop` by default. Compare should be your `{branch_name}`) -> Adds some description and submits it.
- Now all team members can review and merge his code.

### Reviewing a PR

Sometimes you might want to fix something in someone else's branch. You should use `git fetch` command to copy the remote branch to your local and work on it.

It should look like `git fetch origin branch-name:branch-name` & `git checkout branch-name