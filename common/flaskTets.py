from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/",methods=['GET'])
def helloWorld():
    data = request.args["aa"]
    print(data)
    return data

@app.route("/index",methods=['POST'])
def index():
    data = request.get_json()
    print(data)
    return data.get("aa")


if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0", 8888)