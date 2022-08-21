
from flask import Flask, jsonify, request
from products import products


app = Flask(__name__)


@app.route("/products")
def get_products():
    return jsonify({"products": products, "message": "Products list"})


@app.route("/products/<string:product_name>")
def get_product(product_name):
    print(product_name)
    product_found = [product for product in products if product['name'] == product_name]
    if len(product_found) > 0:
        return jsonify({"product": product_found[0]})
    return jsonify({"message": "Product not found"})


@app.route("/products/create", methods=['POST'])
def add_product():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"message": "Product added succesfully", "products":products})


@app.route("/products/<string:product_name>", methods=['PUT'])
def edit_product(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    product_found = product_found[0]
    if len(product_found) > 0:
        product_found['name'] = request.json['name']
        product_found['price'] = request.json['price']
        product_found['quantity'] = request.json['quantity']
        return jsonify({
            "Message": "Product update",
            "product": product_found
        })
    return jsonify({"message": "Product not found"})


@app.route("/products/<string:product_name>", methods=['DELETE'])
def delete_product(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    product_found = product_found[0]
    if len(product_found) > 0:
        products.remove(product_found)
        return jsonify({
            "message": "Removed product",
            "products": products
        })
    return jsonify({"message": "Product not found"})
    

if __name__ == "__main__":
    app.run()