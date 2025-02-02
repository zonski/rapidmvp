# RapidMVP

## Setup a new local dev instance

### Install tools needed

* Install Python `brew install python` 
* Install PostgreSQL
* Install IDE of your choice 

### Create a Database Schema 

* Login to pgAdmin
* Create a new login role (aka user) called "rapidmvp" with password "rapidmvp"
* Grant the user the ability to login and give it super user access (for development)
* Create a new database called "rapidmvp" with owner "rapidmvp"

### Create an Auth0 account and setup

* Sign up to Auth0 
* Create a new application of type "Regular Web Application" 
* Set the "Allowed Callback URL" to http://localhost:8080/callback
* Set the "Allowed Logout URL" to http://localhost:8080
* Take note of the "Domain", "Client ID" and "Client Secret"

### Setup the local source code

* Clone the repository locally
* In the project root directory setup a "venv" `python3 venv .venv`
* Activate the venv with `souce .venv/bin/activate`
* Install the project dependencies `pip install -r requirements.txt

### Setup the config parameters

* Copy .env.sample to .env.local
* Check the DB_ settings match what you created in the database setup
* Update the Auth0 settings with the values from your App that you created in the Auth0 setup
* The APP_SECRET is a random string of characters that is used to encrypt the session cookie. You can generate one with `openssl rand -hex 32`

### Run the database migration scripts 

* `./migrate.sh`

### Run the project 

* `./start.sh`
* Open a browser and go to http://localhost:8080 (not 127.0.0.1:8080 or you will need to configure Auth0 to allow that)


## Editing the code

* The code is:
  * written in Python 
  * uses Flask as the web framework - ChatGPT can help a lot with this
  * uses Jinja2 for templating (worth considering using htmlx as a light weight frontend framework https://htmx.org/)
  * uses Bootstrap for styling (quick and easy but probably should move this to tailwind.css)
* The "things" page is a good place to start. 
  * It shows how to use the database and how to render a list of things.
  * The `src/app/routes/things.py` file contains the routes (urls) for the "things" page.
  * HTML Templates are in `src/app/templates/things`
  * Make your own "whatever" router in `src/app/routes/whatever.py` and edit `src/app/routes/__init__.py` to add the new router to the app
  * The database migration scripts are in `src/app/db/migrations/001_create_things_table.sql`
  * You can work with an existing database schema and not use the migration scripts. 
  * Otherwise you can make your own scripts. These are pure SQL, naming convention is to us YYMMDD_NUMBER_name_of_script.sql
  * The migration scripts are run with the `./migrate.sh` script
