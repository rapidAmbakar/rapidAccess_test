from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_cors import CORS
import base64

import os
import matplotlib.pyplot as plt

app = Flask(__name__)
api = Api(app)
CORS(app)


parser = reqparse.RequestParser()

#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"

students = ['Virat','Sachin','Dhoni']

class Helloworld(Resource):

    def post(self):
        #args = parser.parse_args()
        return {
			"Status": 200,
            "students": request.form.get("ss",45)
		}
    
    def get(self):              

        return {
			"Status": 200,
            "students": students
		}



class userImages(Resource):
    
    def post(self):
        print("POST -------------------------------------------------- CALLED\n\n")
        print("Total Len : ", len(request.form),"\n")
        print(list(request.form))
        print("\n\n")
        try:
            eid = request.form.get("employee_id",888)
            ename = request.form.get("employee_id","EMPTY")
            imgstring = request.form.get('images_0','343')
            print(imgstring[:10],"\n\n")
            imgstring = imgstring.replace("data:image/jpeg;base64,",'')
            imgdata = base64.decodebytes(imgstring.encode('ascii'))

            filename = 'Imgs/',eid,'_',ename,'/1.jpeg'  # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                print("## in save")
                f.write(imgdata)
    
            #with open("imageFlask.jpeg",'wb') as f:
            #    f.write(file)
            #print(file)
            #plt.imshow(file)
            print("IMAGE DONE    -")
        except Exception as e:
            print('Error in Writing file ',e)
        return {
            "status":"200",
            "employee_id": eid,
            "employee_name": ename
            }
    
    
api.add_resource(Helloworld, '/',
                 '/Helloword')


api.add_resource(userImages, '/api/images')




app.run(debug=True,
        host="192.168.1.140")