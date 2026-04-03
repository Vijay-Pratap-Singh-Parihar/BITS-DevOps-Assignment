import json

from flask import Flask, jsonify, request

app = Flask(__name__)

members: list = []


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)


@app.route("/members", methods=["POST"])
def add_member():
    raw = request.get_data()
    if not raw or not raw.strip():
        return jsonify({"error": "Request body is required"}), 400

    try:
        data = json.loads(raw.decode())
    except (json.JSONDecodeError, UnicodeDecodeError):
        return jsonify({"error": "Invalid JSON"}), 400

    members.append(data)
    return jsonify({"message": "Member added"}), 201


if __name__ == "__main__":
    # Bind 0.0.0.0 so the app is reachable from Docker port mappings and local clients.
    app.run(host="0.0.0.0", port=5000, debug=True)
