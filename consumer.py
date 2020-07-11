from flask import Flask,request,jsonify
from kafka import KafkaConsumer
from kafka import KafkaProducer
import sys
import datetime

app = Flask(__name__)

def errorMessage(iid,topicName):
    bootstrap_servers = ['localhost:9092']
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    emsg = "error occured for id:" + str(iid + ' and Timestamp is: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    producer.send(topicName, emsg.encode())
    # print( "please provide a valid topic name for iid:" + str(iid),flush=True)
    return "please provide a valid topic name for iid:" + str(iid)

def successMessage(iid,topicName):
    bootstrap_servers = ['localhost:9092']
    producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
    smsg = " message is successfuly consumed for iid:" + str(iid + ' and Timestamp is: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
    producer.send(topicName, smsg.encode())
    # print("message is successfuly consumed for iid:" + str(iid), flush=True)
    return "message is successfuly consumed for iid:" + str(iid)


@app.route("/",methods=['GET','POST'])
def consumer():
    payload = request.get_json()
    topicName = payload['topic']
    iid = payload['iid']
    bootstrap_servers = ['localhost:9092']
    topicList = ['Event_Error','Prediction','Processing_completed','change_log_of_query','message','metadata_input','stateful_data_of_query']
    count = [x for x in topicList if str(x) == topicName]
    if len(count) == 0:
        topic = 'Event_Error'
        return jsonify(msg = errorMessage(iid,topic))
        sys.exit()
   
    consumer = KafkaConsumer(topicName, group_id = None,bootstrap_servers = bootstrap_servers,
    auto_offset_reset = 'earliest',consumer_timeout_ms=1000)
    print("consumer is ready for messages to consume",flush=True)
    for msg in consumer:
        print("message is received:",msg.value.decode('utf=8'),flush=True)
       
    return jsonify(msg = successMessage(iid,topicName))
    # return jsonify(msg = "its done")
    

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=6090,debug=True)


