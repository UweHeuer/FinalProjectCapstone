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
follows the standard scheme https://<AUTH0_DOMAIN>/authorize?audience=<API IDENTIFIER>&response_type=token&client_id=<CLIENT_ID>&redirect_uri=<CALLBACK_URI>.

# Testing
## Test by Automated Test Script
Run the tests for each API and role by (tokens for testing set via `setup.sh` (see above)):
```
python test_app.py
```
## Tests by Postman
There is a Postman export file `capstone.postman_collection.json`. It uses to global variables to be set:
* CAPSTONE_URL
* AUTH_TOKEN

## Manual Tests
There are 3 Auth0 test user - one for each role - to be used for manual tests:
* Casting Assistant ca@uweheuer-capstone.herokuapp.com
* Casting Director cd@uweheuer-capstone.herokuapp.com
* Executive Producer ep@uweheuer-capstone.herokuapp.com

# API Reference
## Error Handling
Errors or missing access rights are returned via a standard JSON object with a standard format e.g.
```
{
    "error": 401,
    "message": "token is invalid",
    "success": false
}
```

Standard errors codes and messages are:
* 400 bad request
* 401 invalid payload
* 401 unauthorized
* 401 invalid token
* 401 token expired
* 401 invalid claims
* 401 invalid header
* 401 wrong_authorization_header_format
* 401 missing_bearer_in_authorization_header
* 401 authorization_header_missing
* 404 resource not found

## Endpoints

### GET '/movies'
* no parameter
* return a list of all movies
* response example
```
{
    "movies": [
        {
            "id": 1,
            "release_date": "22.02.2022",
            "title": "movie title 1"
        },
        ...
    ],
    "success": true
}
```

### POST '/movies'
* requires a JSON body e.g.
```
{
    "title": "movie title 1",
    "release_date": "22.02.2022"
}
```
* creates a new movie
* in case of success returns the id of the new movie e.g.
```
{
    "movie_id": 4,
    "success": true
}
```

### PATCH '/movies/<int:id>'
* requires a JSON body with the attributes to be patched e.g.
```
{
    "title": "patched title from postman",
    "release_date": "patched release_date from postman"
}
```
* updates the movie with 'id'
* in case of success returns the id of the updated movie e.g.
```
{
    "movie_id": 3,
    "success": true
}
```

### DELETE '/movies/<int:id>'
* no parameter
* deletes the movie with 'id'
* in case of success returns the id of the deleted movie e.g.
```
{
    "movie_id": 5,
    "success": true
}
```

### GET '/actors'
* no parameter
* return a list of all actors
* response example
```
{
    "actors": [
        {
            "age": "22",
            "gender": "M",
            "id": 2,
            "name": "name of actor 2"
        },
        {
            "age": "22",
            "gender": "F",
            "id": 4,
            "name": "name of actor 4"
        }
    ],
    "success": true
}
```

### POST '/actors'
* requires a JSON body e.g.
```
{
    "name": "name of actor",
    "gender": "F",
    "age": "22"
}
```
* creates a new actor
* in case of success returns the id of the new movie e.g.
```
{
    "actor_id": 5,
    "success": true
}
```

### PATCH '/actors/<int:id>'
* requires a JSON body with the attributes to be patched e.g.
```
{
    "name": "patched name of actor",
    "gender": "M",
    "age": "25"
}
```
* updates the actor with 'id'
* in case of success returns the id of the updated movie e.g.
```
{
    "actor_id": 3,
    "success": true
}
```
### DELETE '/actors/<int:id>'
* no parameter
* deletes the actor with 'id'
* in case of success returns the id of the deleted actor e.g.
```
{
    "actor_id": 5,
    "success": true
}
```



