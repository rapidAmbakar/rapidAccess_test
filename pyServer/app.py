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
        
        tot_imgs = len(request.form) - 2
        print("POST -------------------------------------------------- CALLED\n\n")
        #print("Total Len : ", len(request.form),"\n")
        print()
        print("\n\n")
        try:
            eid = request.form.get("employee_id",888)
            ename = request.form.get("employee_name","EMPTY")
            
            
            for i in range(tot_imgs):
                imgstring = request.form.get('images_'+str(i),'343')
                
                imgstring = imgstring.replace("data:image/jpeg;base64,",'')
                imgdata = base64.decodebytes(imgstring.encode('ascii'))
                
                
                filename = "Employee/"+str(eid)+"_"+str(ename)
                
                if not os.path.exists(filename):
                    os.makedirs(filename)
                
                with open(filename+"/"+str(i)+".jpeg", 'wb') as f:
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
            "employee_id": request.form.get("employee_id",888),
            "employee_name": request.form.get("employee_name","EMPTY")
            }
    
    
api.add_resource(Helloworld, '/',
                 '/Helloword')


api.add_resource(userImages, '/api/images')


if __name__ == '__main__':
    context = ("/home/ad.rapidops.com/pushkar.ambatkar/local_ssl/localhost.pem", "/home/ad.rapidops.com/pushkar.ambatkar/local_ssl/localhost.key")
    app.run(debug=True,
            host="0.0.0.0",
            ssl_context=context)
