# Motivation for the Project
This project implements the Capstone Project of the Udacity Full Stack Web Developer Nanodegree program. 
It implements the Casting Agency specifications. The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. 

# Technology Stack

The main technologies are:
- Python
- Flask
- SQLAlchemy and Flask Alchemy
- PostGreSQL
- Auth0
- Heroku

The detailed dependencies are listed in `requirement.txt`.

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

# Testing

# API 


