from flask import Flask, request, jsonify
from flask_cors import CORS

from bson import ObjectId
import bcrypt
from model import order_collection


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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
    app.run(debug=True, port=7000)