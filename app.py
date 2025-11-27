from flask import Flask, jsonify, request

app = Flask(__name__)

# 模拟用户数据
users = {
    1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
    2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
}

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or not data.get("name"):
        return jsonify({"error": "Missing name"}), 400
    new_id = max(users.keys()) + 1
    users[new_id] = {"id": new_id, "name": data["name"], "email": data.get("email", "")}
    return jsonify(users[new_id]), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(port=5000)
