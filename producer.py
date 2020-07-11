from flask import Flask,request,jsonify
# import requests
from kafka import KafkaProducer

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def producer():
    inpt = request.get_json()
    iid = inpt['iid']
    # identifierId = inpt['identifierId']
    bootstrap_servers = ['localhost:9092']
    topicName = 'message'

    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    producer.send(topicName, iid.encode())
    return jsonify(msg = "iid is written to topic-message")  

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6010,debug=True)


