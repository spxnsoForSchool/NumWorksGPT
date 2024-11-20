from flask import Flask, request, jsonify
import ollama  # Ensure the Ollama Python library is installed

app = Flask(__name__)

@app.route("/ollama", methods=["POST"])
def ollama_route():
    # Get the input data from the request
    data = request.json
    user_input = data.get("input", "")

    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Interact with Ollama using the chat method
        response = ollama.chat(
            model="mistral",  # Specify the model to use
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ]
        )

        # Extract the response content
        mesg = print(response['message']['content'])
        return jsonify({"result": mesg})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
