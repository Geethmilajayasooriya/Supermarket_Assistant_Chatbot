from flask import Flask, request, jsonify, send_from_directory
from chatbot import extract_items, find_shelves

app = Flask(__name__)

@app.route("/")
def index():
    # Serve index.html from current folder
    return send_from_directory(".", "index.html")

@app.route("/style.css")
def style():
    # Serve CSS from current folder
    return send_from_directory(".", "style.css")

@app.route("/get_shelves", methods=["POST"])
def get_shelves():
    data = request.get_json()
    user_input = data.get("items", "")
    items = extract_items(user_input)
    shelf_info = find_shelves(items)
    return jsonify(shelf_info)

if __name__ == "__main__":
    app.run(debug=True)
