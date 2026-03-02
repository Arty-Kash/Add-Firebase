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
  # Firebase上では、下記コード（ポート80）で動く
  # app.run(port=int(os.environ.get('PORT', 80)))

  # ローカルPCではポート80は禁止されているので、Firebaseから出して
  # ローカルPC上で実行するためには、下記コードに変更する必要がある。
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
