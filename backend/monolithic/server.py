# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

from pymongo import MongoClient
from bson import ObjectId
import bcrypt

from dotenv import load_dotenv
import os

load_dotenv()  
URL = os.getenv('URL')

uri = URL

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


client = MongoClient(uri)
db = client['monolithic_db']  # Change 'your_database_name' to your actual database name
user_collection = db['user']
cart_collection = db['cart']
order_collection = db['order']

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = user_collection.find_one({'email': email})

    if user:
        # Verify password
        if bcrypt.checkpw(password.encode('utf-8'), user['password']):
            return jsonify({'message': 'Login successful :)', 'userID': str(user['_id'])})  # Include user's _id in the response
        else:
            return jsonify({'message': 'Invalid email or password'}), 401
    else:
        return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    email = data.get('email')
    password = data.get('password')
    ph = data.get('ph')
    address = data.get('address')


    # Hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Check if email already exists
    if user_collection.find_one({'email': email}):
        return jsonify({'message': 'Email already exists'}), 400

    # Insert new user
    user_id = user_collection.insert_one({'name': name, 'age' : age ,'email': email, 'password': hashed_password, 'ph.no': ph, 'address': address}).inserted_id

    return jsonify({'message': 'Signup successful', 'user_id': str(user_id)}), 201

@app.route('/cartadd', methods=['POST'])
def add_to_cart():
    data = request.get_json()  # Get data sent in the request
    cart_collection.insert_one(data)  # Insert the data into the cart collection
    return jsonify({"message": "Item added to cart"}), 200

@app.route('/cartrem', methods=['DELETE'])
def remove_from_cart():
    data = request.get_json()  # Get data sent in the request
    userId = data.get('userId')
    id = data.get('productId')

    # Remove the item from the cart collection
    result = cart_collection.delete_one({'userId': userId, 'id': id})

    if result.deleted_count == 0:
        return jsonify({"message": "No item found to delete"}), 404

    return jsonify({"message": "Item removed from cart"}), 200


@app.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    cart_items = data['cartItems']
    user_id = data['userId']

    order = {
        'userId': ObjectId(user_id),
        'cartItems': cart_items
    }

    print("WHAT IS GOING TO ORDER",order)

    result = order_collection.insert_one(order)

    if result.acknowledged:
        return jsonify({
            'status': 'success',
            'message': 'Order created successfully',
            'orderId': str(result.inserted_id)
        }), 201

    return jsonify({
        'status': 'error',
        'message': 'An error occurred while creating the order'
    }), 500

if __name__ == '__main__':
    app.run(debug=True)
