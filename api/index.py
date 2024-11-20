from flask import Flask, request, jsonify
import ollama  # Assuming Ollama provides a Python SDK or you interact with an API.

app = Flask(__name__)

@app.route("/ollama", methods=["POST"])
def ollama_route():
    # Get the input data from the request
    data = request.json
    user_input = data.get("input", "")
    
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    # Interact with Ollama
    try:
        # Example: Call a function from Ollama SDK or an API endpoint
        response = ollama.query(prompt=user_input)  # Adjust b
        return jsonify({"result": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
