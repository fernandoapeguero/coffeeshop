# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

# Coffee Shop Api Endpoints

## Authentication 
auth0 - Authentification with roles access 

Roles:
```
Barista - Can only get drinks 
Manager - Can do everything
```

Permissions:
```
  get:drinks-detail - Return drinks detail in long form 
  post:drinks - Inserts new recipe into the database 
  patch:drinks - Updates a drinks recipe
  delete:drinks - delete a drink in the database
```

## Base Url 

the base url return the recipes in the database.

    https://localhost:5000/drinks


###  Sample Response From Base Url
 
 ```bash
 {
  "drinks": [
    {
      "id": 1, 
      "recipe": [
        {
          "color": "blue", 
          "parts": 1
        }, 
        {
          "color": "brown", 
          "parts": 1
        }
      ], 
      "title": "chocolate"
    }
  ], 
  "success": 200
}
 ```
  
 ## Error Handling 
 
 Type of error the api handles

   * 400 Bad Request
   * 404 Not Found
   * 405 Method Not Allowed
   * 422 Unproccesable Entity
   * 500 Server Error 
   
Error Handling Response Sample

```bash
{
  'success': False,
  'error':  400,
  'message': 'Bad request'
}

```

responses with come back in a json object format 

<br>

# Endpoint Library 

Here you will find all the endpoint you need to work with the api 

The Structure of the EndPoint library is simple since you will deploy the backend localy for this app we know the domain will be http://127.0.0.1:5000
and you will only need the path for example /trivia_api/questions in this library we will prefix the path with the method needed for the call. 

## Heroku 

currently this backend is deploy in heroku and is very simple to substitute the domain in the local uri to the heroku provided one if you are using the deploy version 
<heroku deploy uri>/<end point> and it will work without no problem.

Example: POST/drinks

---

## GET Endpoints

<br>

### GET/drinks

returns the recipes in short form from the database

Reponse

```bash
{
  "drinks": [
    {
      "id": 1, 
      "recipe": [
        {
          "color": "blue", 
          "parts": 1
        }, 
        {
          "color": "brown", 
          "parts": 1
        }
      ], 
      "title": "chocolate"
    }, 
    {
      "id": 2, 
      "recipe": [
        {
          "color": "Yellow", 
          "parts": 1
        }, 
        {
          "color": "pink", 
          "parts": 1
        }
      ], 
      "title": "Flower Candy"
    }, 
    {
      "id": 3, 
      "recipe": [
        {
          "color": "white", 
          "parts": 1
        }
      ], 
      "title": "panera"
    }, 
    {
      "id": 4, 
      "recipe": [
        {
          "color": "brown", 
          "parts": 1
        }
      ], 
      "title": "splicer"
    }
  ], 
  "success": 200
}
```

<br>

### GET/drinks-detail

returns drinks in long form 

Reponse

```bash
{
    "drinks": [
        {
            "id": 1,
            "recipe": [
                {
                    "color": "blue",
                    "name": "chocolate ",
                    "parts": 1
                },
                {
                    "color": "brown",
                    "name": "canela",
                    "parts": 1
                }
            ],
            "title": "chocolate"
        },
        {
            "id": 2,
            "recipe": [
                {
                    "color": "Yellow",
                    "name": "Flower",
                    "parts": 1
                },
                {
                    "color": "pink",
                    "name": "candy",
                    "parts": 1
                }
            ],
            "title": "Flower Candy"
        },
        {
            "id": 3,
            "recipe": [
                {
                    "color": "white",
                    "name": "diet",
                    "parts": 1
                }
            ],
            "title": "panera"
        },
        {
            "id": 4,
            "recipe": [
                {
                    "color": "brown",
                    "name": "lala",
                    "parts": 1
                }
            ],
            "title": "splicer"
        }
    ],
    "success": true
}
```

<br>

---

## POST Endpoints

<br>

### POST/drinks

post a recipe to the database

you can post a recipe and it will be save to the database if you have the proper permission and 
it will persist and show in the site after submission.

JSON body 

```bash
{
    "title": "Milk Rice",
    "recipe": {
        "name": "Milk Rice",
        "color": "white",
        "parts": 1
    }
}
```

returns json object 
```bash

Response
 return jsonify({
            'success': 200,
            'drinks': drink.long()
        }), 200
```

<br>

### PATCH/drinks/<drink_id>

The api endpoint for PATCH expect a id for the drinks recipe you witch to modify.
It return a json object with the modify drink and a success field.


Response
```bash
return jsonify({
            'success': True,
            'drinks': drink.long()
        }), 200

```

<br>

## DELETE Endpoint

<br>

### DELETE/drinks/<drink_id>

this end point will delete a question from the database base on the id given to the endpoint. The endpoint will return a json object with a success boolean and the deleted id of the drink recipe that was deleted 

Reponse 

```bash
{
    "delete": 1,
    "success": true
}
```
