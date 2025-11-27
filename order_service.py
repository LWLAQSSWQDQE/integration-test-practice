from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/orders/123/payment")
def order_payment():
    return jsonify({"order_id": 123, "status": "Paid"})

if __name__ == "__main__":
    app.run(port=5002)
