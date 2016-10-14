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
	- [Integrating Postgresql](#integrating-postgresql)
		- [Cleaning up your Postgresql DB](#cleaning-up-your-postgresql-db)
	- [PostGIS installation](#postgis-installation)
		- [Mac instructions](#mac-instructions)
		- [Ubuntu instructions](#ubuntu-instructions)
	- [GeoDjango Tutorials](#geodjango-tutorials)
	- [Git Team Workflow](#git-team-workflow)
		- [Reviewing a PR](#reviewing-a-pr)
- [Deployment!](#deployment)
	- [postgres](#postgres)
		- [So... guides?](#so-guides)
	- [uwsgi+nginx](#uwsginginx)
		- [Foreword: Caution!](#foreword-caution)
		- [uwsgi docs](#uwsgi-docs)
		- [nginx docs](#nginx-docs)
	- [How are we set up?](#how-are-we-set-up)
		- [django](#django)
		- [uwsgi](#uwsgi)
		- [nginx](#nginx)
		- [sock??](#sock)

<!-- /TOC -->

# Administration
## Steps to get started:
1. Navigate to the `ProjectUmbrella-Code` root directory
2. Run a local server via `python manage.py runserver`
  - Note 1: On Ubuntu you may have to specify python3 explicitly: `python3 manage.py runserver`
  - Note 2: You can tell the server to run on a port different to the default (which is Port 8000) by using: `python manage.py runserver 8080`
3. If you get errors, make sure your Postgresql database has been set up correctly as per [here](#postgresql-set-up)
4. Current valid views include:
  - `localhost:8000/`
	- `localhost:8000/admin/`
  - `localhost:8000/googlemaps/` - has a locate current location feature
  - `localhost:8000/signin/`

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



## Integrating Postgresql
Please have a look at this before you start:

* [Tutorial for Mac Users](http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django#create-database)
* [Tutorial for Ubuntu Users](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)

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

6. You will most likely have gotten an error in step 5, if the stack trace mentions `postgis` then complete the next section and then retry step 5. Remember if you need help, ask for it.

### Cleaning up your Postgresql DB
Sometimes you might run into database errors, e.g. when a certain column in a table doesn't exist and `python3 manage.py migrate` doesn't seem to fix it.

What you can try is to drop your database:
```
sudo -u postgres psql
drop database <your_database_name>;
create database <your_database_name> with owner <user_you_use_in_django>;
\q
```
and run `python3 manage.py migrate` & `python3 manage.py runserver` again.

## PostGIS installation
### Mac instructions
1. Install `postgis v2.2` in following the instructions in [this link](http://postgis.net/install/)

2. Following the suggestion in the postgis install page, run `psql` as psql superuser in terminal, run following code:
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
3. Try to `brew` following
```
$ brew install gdal
$ brew install libgeoip
```
4. Done

### Ubuntu instructions
1. Install `postgis` via: `sudo apt-get install postgresql-9.5-postgis-2.2`
2. Run `sudo -u postgres psql` and copy the following:
```
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
CREATE EXTENSION fuzzystrmatch;
CREATE EXTENSION postgis_tiger_geocoder;
```
3. Done

## GeoDjango Tutorials

Some GeoDjango links here that might be helpful:

* [Tutorial 1](http://invisibleroads.com/tutorials/geodjango-googlemaps-build.html)
* [Tutorial 2](https://docs.djangoproject.com/en/1.10/ref/contrib/gis/tutorial/)

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

It should look like `git fetch origin branch-name:branch-name` & `git checkout branch-name`

# Deployment!

Here are a bunch of notes about how our EC2 instance is configured, and the docs I used while setting it up. If anyone has any questions or wants me to go through anything with them, let me know! It was lots of fun, and I'd be happy to talk about it.

## postgres

Postgres databases are stored on clusters: these are the structure which postgres uses to write the data to disk, and once they're set up you can basically forget they exist. On umbrellabox, we are using a database cluster I created in `/db/pgsql/data`, and the original default cluster which postgres created has been destroyed.

`/db` is the mount point I used for the EBS volume which I set up to separate the database from the system. Setting up an EBS volume was pretty easy... you just ask the AWS console for a new one, then partition and mount it in the OS like you would any other disk.

If I were doing this again, I would **not** use an EBS volume for the database, but rather an RDS instance. Setting up a postgres cluster was a pain, in the sense that it requires some understanding of how postgres is working behind the scenes. Avoid if you can!

### So... guides?

There weren't any guides for this kind of thing. I basically muddled through with the official docs for postgres, and figured it out as I went along. I made a royal mess of it the first time, which was why I started the second instance of the server... I think this was probably a unavoidable part of the learning process. :P

## uwsgi+nginx
### Foreword: Caution!

The first lesson I learnt in setting this all up was *USE THE OFFICIAL DOCS!*

### uwsgi docs

This was generally the best source I found for getting everything running together. That said, I had a few problems setting this up by directly following the guide — in those cases, I found the best thing to do was to look up what all of the values in the config were doing.

[uwsgi-docs: Django and nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

[uwsgi-docs: nginx](https://uwsgi-docs.readthedocs.io/en/latest/Nginx.html)

I read the following to check what was good practice for configuring uwsgi once it was working, but most of it didn't apply for our purposes:

[uwsgi-docs: things to know](https://uwsgi-docs.readthedocs.io/en/latest/ThingsToKnow.html)

Regarding the number of worker threads: this is currently defaulting to one — I don't see any reason to have it any higher for our purposes, but it's very easy to do.

### nginx docs

This is the official nginx guide for setting it up with uwsgi. Generally the guide in the uwsgi docs was better for being slightly more comprehensive, but this made for a good introduction to nginx:

[nginx: using nginx with uwsgi and django](https://www.nginx.com/resources/admin-guide/gateway-uwsgi-django/)

This is the list of nginx directives used in .conf files — it got me out of a couple of binds!

[nginx: index of directives](https://nginx.org/en/docs/dirindex.html)

## How are we set up?

### django

Okay, so the django server is running as you would normally, with one difference: we are bundling all static files into one big directory in `$HOME/staticroot`. This is so that nginx can find them all in one place and not bother anyone else about it. Django does this for us — to find out how, read: [djangoproject: static files - deployment](https://docs.djangoproject.com/en/1.10/howto/static-files/#deployment)

Note that in the `deployment` branch, there are a few other changes to `settings.py`. Debug mode is set to false, so that django doesn't generate stack traces etc. when things go wrong. Also, once debug mode is disabled, django defaults to only respond to hosts specified in `allowed_hosts` — this is a whitelist, that can be used to allow only particular subnets and therefore enforce the use of load balancers and what-have-you. Currently we have this set to allow `'*'` — a wildcard, allowing any hosts to connect.

### uwsgi

uwsgi is a python package, so you install it with pip. It basically loads the virtual environment and runs the django project, but can spawn bazillions of worker processes which it then uses to serve the site. On umbrellabox, uwsgi is running from within the virtual environment in a tmux session. This is not necessary — I could just as easily have set up uwsgi in the global pip. This way I get to have nice screens of logs which I can easily start and stop.

Currently we have uwsgi set up to have only a single worker thread, but we could very easily scale this up in the config file if we wanted to run a more powerful instance.

### nginx

All nginx does is takes the incoming traffic on port 80 (http) and redirects it either to nginx for non-static routes, or directly to the file (in `$HOME/staticroot`) for any images/css/what-have-you. It just does this really, really quickly and efficiently, while slow old python has bigger things on its mind.

Access and error logs for nginx are kept at `/var/log/nginx/` by default, but this can be modified in the config file.

In the `deployment` branch, we have two config files for nginx: one for http, and one for https. We are symlinking to these files from the `/etc/nginx/sites-enabled/` directory, where nginx goes to look for site config files, so that we can keep them in one place under version control. We are currently linking to the http config file while we wait for ssl to be set up.

### sock??

`umbrella.sock` is the unix socket which nginx is using to connect to uwsgi. This was not necessary — it worked just as well routing traffic to `localhost:8080`, which I originally had uwsgi running on.