from flask import Flask, request, jsonify
from flask_cors import CORS

from bson import ObjectId
import bcrypt
from model import cart_collection


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


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

if __name__ == '__main__':
    app.run(debug=True, port=8000)