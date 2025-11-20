from flask import Flask, request, jsonify, send_from_directory
import os
import logging
from resources_store import ResourceStore
from translations import translate_to_spanish_simplified, extract_key_actions

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# Initialize the resource store
resource_store = ResourceStore("assets/resources.json")  # path inside container

# ------------------------
# API Endpoints
# ------------------------

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/resources")
def get_resources():
    zipcode = request.args.get("zipcode")
    category = request.args.get("category")
    results = resource_store.find_by_zip(zipcode)
    return jsonify(results)

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data.get("text", "")
    spanish_text = translate_to_spanish_simplified(text)
    actions = extract_key_actions(text)
    return jsonify({
        "original": text,
        "spanish": spanish_text,
        "actions": actions
    })

# ------------------------
# HTML Frontend
# ------------------------

@app.route("/")
def index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), "static"), "index.html")

# ------------------------
# Run the app
# ------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # default to 5000
    app.run(host="0.0.0.0", port=port)