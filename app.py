
import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
products = [
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 150},
    {"id": 3, "name": "Product 3", "price": 200}
]

# Route to get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Route to get a specific product by its ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((item for item in products if item["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

# Route to create a new product
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    new_product = {"id": len(products) + 1, "name": data["name"], "price": data["price"]}
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
