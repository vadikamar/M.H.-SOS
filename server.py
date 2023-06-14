import string
from flask import Flask, render_template, request, jsonify
from trycourier import Courier
import sys
import json
from geopy.geocoders import Nominatim
import geocoder
'''from pymongo import MongoClient
from pymongo_get_database import get_database'''

'''def get_database():
   CONNECTION_STRING = "mongodb://localhost:27017/"
   client = MongoClient(CONNECTION_STRING)
   return client['first']'''

jsvalue=""
no=-1
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route("/function_route",methods=["GET","POST"])
def my_function():
  if request.method=="POST":
    jsvalue=request.json['value']
    print(jsvalue)
    return json.dumps({'success':"recevied"}), 200, {'ContentType':'application/json'}

@app.route('/pass_val',methods=['POST'])
def pass_val():
    no=request.args.get('value')
    print('name',no)
    return jsonify({'reply':'success'})

@app.route('/my-link/')
def my_link():
        client = Courier(auth_token="pk_prod_J74J2SJFG64GV1NMD1F2QQXAX5ZG") #or set via COURIER_AUTH_TOKEN env var
        geoLoc = Nominatim(user_agent="GetLoc")
        g = geocoder.ip('me')
        locname = geoLoc.reverse(g.latlng)
        add=locname.address
        resp = client.send_message(
          message={
            'to': {
              'email': 'vadikamar@gmail.com',
              'data': {'name': 'Vadik', 'addr':add}
            },
            'content': {
              'title': 'M.H. SOS Alert',
              'body': 'We are sorry to tell but {{name}} is feeling depressed and he needs your support. His IP ADDRESS:{{addr}} ',
            },
            'routing': {
              'method': 'single',
              'channels': ['email'],
            }
          }
        )
        '''dbname = get_database()'''
        return render_template('thanks.html')




      

if __name__ == '__main__':
  app.run(debug=True)