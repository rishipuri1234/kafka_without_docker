from flask import Flask,jsonify,request
app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def hello_world():
    payload = request.get_json()
    message = payload['message']
    print("+++++++++++++++++", message, flush=True)
    return jsonify(msg="Hello World!'")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5040,debug=True)
