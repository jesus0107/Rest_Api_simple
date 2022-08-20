from flask import Flask, jsonify
from products import products


app = Flask(__name__)


@app.route("/products")
def get_products():
    return jsonify({"products": products, "message": "Products list"})

@app.route("/products/<string:product_name>")
def get_product(product_name):
    print(product_name)
    product_found = [product for product in products if product['name'] == product_name]
    return jsonify({"product": product_found[0]})

if __name__ == "__main__":
    app.run()