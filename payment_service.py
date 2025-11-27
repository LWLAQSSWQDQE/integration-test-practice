from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/pay/123")
def pay_order():
    return jsonify({"order_id": 123, "status": "Success"})

if __name__ == "__main__":
    app.run(port=5003)
