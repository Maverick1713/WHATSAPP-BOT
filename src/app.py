# from flask_mysqldb import MySQL
# from helper.openai_api import text_complition
from helper.twilio_api import send_message
from helper.bard_api import text_generate
import os
# from data.data import log
import pymysql
from flask import Flask, request
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
db = pymysql.connect(host='localhost',port=3306,user='root', passwd='sonu@5185', db='chatbot',autocommit=True)

@app.route('/')
def home():
    return 'All is well...'


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        # Extract incomng parameters from Twilio
        message = request.form['Body']
        print(message)
        sender_id = request.form['From']
        # log(sender_id,message)
        # Get response from Openai
        # result = text_complition(message)
        result = text_generate(message)
        # if result['status'] == 1:
        #     print(result['response'])
        #     send_message(sender_id, result['response'])
        x = len(result)
        l = 0
        while x!=0:
            k = 1599 if x>1599 else x
            send_message(sender_id, result[l:l+k])
            l+=k
            x-=k
        print("Done")
        cur = db.cursor()
        cur.execute("INSERT INTO data (whatsapp,info) VALUES (%s,%s)",(sender_id,message))
        cur.close()
        print("Success")
        
    except:
        pass
    return 'OK', 200
