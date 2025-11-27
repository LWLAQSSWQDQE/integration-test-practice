from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/users/1/orders")
def user_orders():
    return jsonify([{"order_id": 123, "item": "Book"}])

if __name__ == "__main__":
    app.run(port=5001)
