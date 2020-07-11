from flask import Flask,request,jsonify
# import requests
from kafka import KafkaConsumer
from kafka import KafkaProducer

import sys

app = Flask(__name__)

def errorMessage(iid):
    # return jsonify(msg = "please provide a valid topic name for iid:" + str(iid))
    print( "please provide a valid topic name for iid:" + str(iid),flush=True)

def successMessage(iid):
    # return jsonify(msg = "message is successfuly consumed for iid:" + str(iid))
    print("message is successfuly consumed for iid:" + str(iid), flush=True)

@app.route("/",methods=['GET','POST'])
def consumer():
    # iid = request.get_json('iid')
    print("inside end point",flush=True)
    payload = request.get_json()
    topicName = payload['topic']
    iid = payload['iid']
    # topicName = topicName.values()
    # topicName = list(topicName.values())[0]
    topicList = ['Event_Error','Prediction','Processing_completed','change_log_of_query','message','metadata_input','stateful_data_of_query']
    count = [x for x in topicList if str(x) == topicName]
    print(len(count),flush=True)
    if len(count) == 0:
        errorMessage(iid)
        sys.exit()

    bootstrap_servers = ['localhost:9092']
    consumer = KafkaConsumer(topicName, group_id = None,bootstrap_servers = bootstrap_servers,
    auto_offset_reset = 'earliest',consumer_timeout_ms=1000)
    print("consumer is ready for messages to consume",flush=True)
    # print("++++++++++++++++++++++++++++++++++",len(consumer), flush=True)
    # print("===================================",type(consumer))

    for msg in consumer:
        print("-----------------------------------------------we are inside for loop",flush=True)
        print("message is received",msg.value.decode('utf=8'),flush=True)
       


    successMessage(iid)
    return jsonify(msg = "its done")
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6090,debug=True)


