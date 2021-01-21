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
        if drinks:
            for drink in drinks:
                results.append(drink.short())

        return jsonify({
            'success': 200,
            'drinks': results
        }), 200
    except:
        abort(404)


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


@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def post_drinks(jwt):

    try:
        data = request.get_json()

        title = data['title']
        recipe = data['recipe']
        drink = Drink(title=title, recipe=json.dumps(recipe))
        drink.insert()

        return jsonify({
            'success': 200,
            'drinks': drink.long()
        }), 200
    except:
        abort(400)


@app.route('/drinks/<int:drink_id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def post_drink(jwt, drink_id):

    try:
        data = request.get_json()
        
        drink = Drink.query.filter(Drink.id == drink_id).first()

        if not drink:
            abort(404)

        title = ''

        if 'title' in data:
            title = data['title']
        else:
            title = drink.title

        recipe = ''
        if 'recipe' in data:
            recipe = data['recipe']
        else:
            recipe = drink.recipe

        drink.title = title
        drink.recipe = str(recipe)
        drink.update()

        result = []

        result.append(drink.long())

        return jsonify({
            'success': True,
            'drinks': result
        }), 200
    except:
        abort(404)


@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, drink_id):

    try:

        drink = Drink.query.filter(Drink.id == drink_id).first()

        if not drink:
            abort(404)

        drink.delete()

        return jsonify({
            'success': True,
            'delete': drink_id
        }), 200
    except:
        abort(404)

# Error Handling


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):

    return jsonify({
        'success': False,
        'error': 404,
        'message': 'resource not found'
    }), 404


@app.errorhandler(AuthError)
def auth_error(error):

    return jsonify({
        'success': False,
        'error': error.error,
        'message': 'Authentication error'
    }), error.status_code
