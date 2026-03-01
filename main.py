import os

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    num1 = data.get("num1", 0)
    num2 = data.get("num2", 0)
    result = num1 + num2
    return jsonify({"result": result})

def main():
  # app.run(port=int(os.environ.get('PORT', 80)))
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
