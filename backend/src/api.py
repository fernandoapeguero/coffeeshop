from operator import truediv
import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

#  only the line below uncomment on first run to create db and re comment for data not to get erase every time

# db_drop_and_create_all()

# ROUTES


@app.route('/drinks')
def get_drinks():
    try:

        drinks = Drink.query.all()

        results = []

        for drink in drinks:
            results.append(drink.short())
        
        return jsonify({
            'success': 200,
            'drinks': results
        }), 200
    except:
        abort(404)

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drink_details(jwt):

    try:
        drinks = Drink.query.all()

        results = []
        for drink in drinks:
            results.append(drink.long())

        return jsonify({
            'success': True,
            'drinks': results
        }), 200
    except:
        abort(404)

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(jwt):

    try:
        data = request.get_json()

        title = data['title']
        recipe = data['recipe']
        drink = Drink(title=title , recipe=json.dumps(recipe))
        drink.insert()
        
        return jsonify({
            'success': 200,
            'drink': drink.long()
        }), 200
    except:
        abort(400)

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def post_drink(jwt, drink_id):

    try:
        print(drink_id)
        # drink = Drink.query.filter(Drink.id == drink_id).all()

        # if len(drink) == 0:
        #     abort(404)

        return jsonify({
            'success': True,
            'drinks': []
        }), 200
    except:
        abort(404)


'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks/<int:drink_id>' , methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, drink_id):

    try:

        drink = Drink.query.filter(Drink.id == drink_id).first()
    
        # if not drink:
        #     abort(404)
        
        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200
    except:
        abort(404)
# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404
'''


@app.errorhandler(404)
def not_found(error):

    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''


@app.errorhandler(AuthError)
def auth_error(error):

    return jsonify({
        'success': False,
        'error': error.error,
        'message': 'Authentication error'
    }), error.status_code
