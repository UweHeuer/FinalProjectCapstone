# Motivation for the Project
This project implements the Capstone Project of the Udacity Full Stack Web Developer Nanodegree program. 
It implements the Casting Agency specifications. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. The specifications are:

* Models:
  * Movies with attributes title and release date
  * Actors with attributes name, age and gender
* Endpoints:
  * GET /actors and /movies
  * DELETE /actors/ and /movies/
  * POST /actors and /movies and
  * PATCH /actors/ and /movies/
* Roles:
  * Casting Assistant
    * Can view actors and movies
  * Casting Director
    * All permissions a Casting Assistant has and…
    * Add or delete an actor from the database
    * Modify actors or movies
  * Executive Producer
    * All permissions a Casting Director has and…
    * Add or delete a movie from the database

# Technology Stack

The main technologies are:
- Python
- Flask
- SQLAlchemy and Flask Alchemy
- PostGreSQL
- Auth0
- Heroku

The detailed technical dependencies are listed in `requirement.txt`.

# Getting Started
It is recommended to use a virtual environment to avoid conflicts with existing installations (the listed commands are for a Linux environment).


Setup the environment by
```
python -m venv venv
source ./venv/bin/activate
```

Install the dependencies by
```
pip install -r requirements.txt
```

The needed environment variables (including the token for the automated test script) are set by
```
source ./setup.sh
```

Start the application by
```
flask run --reload
```

# Hosting at Heroku
There is a running application on the Heroku platform which can be accessed by https://uweheuer-capstone.herokuapp.com/. The `Procfile` defines the web dyno.

# Role Base Access Control
The roles from the specifications have been implemented via Auth0. The roles and permissions are:
* Casting Assistant
  * get:actors
  * get:movies
* Casting Director
  * get:actors
  * get:movies
  * patch:actors
  * patch:movies
  * post:actors
  * delete:actors
* Executive Producer
  * get:actors
  * get:movies
  * patch:actors
  * patch:movies
  * post:actors
  * post:movies 
  * delete:actors
  * delete:movies

The authorization code flow for the Heroku hosted app is https://uweheuer.eu.auth0.com/authorize?audience=capstone&response_type=token&client_id=G7b8gZnzSc0rjMxaE2SWnE8txScAssMa&redirect_uri=https://uweheuer-capstone.herokuapp.com/login and 
follows the standard scheme https://Template:YOUR DOMAIN/authorize?audience=Template:API IDENTIFIER&response_type=token&client_id=Template:YOUR CLIENT ID&redirect_uri=Template:YOUR CALLBACK URI.

# Testing

# API 


