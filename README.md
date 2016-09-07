# Contents

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Contents](#contents)
- [Administration](#administration)
	- [Steps to get started:](#steps-to-get-started)
	- [Register a 'Superuser' account](#register-a-superuser-account)
- [Umbrella application](#umbrella-application)
- [Node Package Manager (npm)](#node-package-manager-npm)
	- [Adding dependencies to `packages.json`](#adding-dependencies-to-packagesjson)

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

# Node Package Manager (npm)
We'll be using npm to manage packages and dependencies e.g. Bootstrap - hich is what we will use to style our HTML with.
It uses a `packages.json` file to keep track of package versions used, much the same as the `requirements.txt` file that is used by Python to keep track of package versioning to ensure consistency.

To download `npm` on Ubuntu:
```
sudo apt-get install npm
```

Navigate to the `ProjectUmbrella-Code` root directory and run `npm install` and npm will install the dependencies from the `packages.json` file.

## Adding dependencies to `packages.json`
This section to be added (TBA) or alternatively just google it ;)
