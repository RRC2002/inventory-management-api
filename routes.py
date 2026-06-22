from flask import jsonify, request
from models import Product, db

def register_routes(app):

    @app.route("/")
    def home():
        return "Inventory API is running!"

    @app.route("/products", methods=["GET"])
    def get_products():
        products = Product.query.all()

        result = []

        for p in products:
            result.append({
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "quantity": p.quantity
            })

        return jsonify(result)

    @app.route("/products", methods=["POST"])
    def add_product():
        data = request.get_json()

        if not data.get("name") or data["price"] < 0 or data["quantity"] < 0:
            return jsonify({"message": "Invalid product data"}), 400

        new_product = Product(
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"]
        )

        db.session.add(new_product)
        db.session.commit()

        return jsonify({"message": "Product added successfully!"})

    @app.route("/products/<int:id>", methods=["GET"])
    def get_product(id):
        product = Product.query.get(id)

        if not product:
            return jsonify({"message": "Product not found"})

        return jsonify({
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity
        })

    @app.route("/products/<int:id>", methods=["PUT"])
    def update_product(id):
        product = Product.query.get(id)

        if not product:
            return jsonify({"message": "Product not found"})

        data = request.get_json()

        product.name = data["name"]
        product.price = data["price"]
        product.quantity = data["quantity"]

        db.session.commit()

        return jsonify({"message": "Product updated successfully!"})

    @app.route("/products/<int:id>", methods=["DELETE"])
    def delete_product(id):
        product = Product.query.get(id)

        if not product:
            return jsonify({"message": "Product not found"})

        db.session.delete(product)
        db.session.commit()

        return jsonify({"message": "Product deleted successfully!"})

    @app.route("/products/summary", methods=["GET"])
    def product_summary():
        products = Product.query.all()

        total_products = len(products)
        total_quantity = sum(p.quantity for p in products)
        total_value = sum(p.price * p.quantity for p in products)

        return jsonify({
            "total_products": total_products,
            "total_quantity": total_quantity,
            "total_inventory_value": total_value
        })