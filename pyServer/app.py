from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_cors import CORS
import base64


import face_recognition
import cv2


import os
import matplotlib.pyplot as plt

app = Flask(__name__)
api = Api(app)
CORS(app)

import functions


cascade_path = "haarcascade_frontalface_default.xml"
casecade = cv2.CascadeClassifier(cascade_path)

parser = reqparse.RequestParser()

#@app.route("/")
#def hello_world():
#    return "<p>Hello, World!</p>"

students = ['Virat','Sachin','Dhoni']

"""
def StringtoImg(imgstring):
    imgstring = imgstring.replace("data:image/jpeg;base64,",'')
    imgdata = base64.decodebytes(imgstring.encode('ascii'))
    return imgdata



def cropFace(img_path):
    crop_face_Image = (0,255,0)
    try:
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = casecade.detectMultiScale(gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(100, 100),
        flags=cv2.CASCADE_SCALE_IMAGE)
        for (x,y,w,h) in faces:
    
            try:
                y1 = y-50
                x1 = x-50
                w1 = w+100
                h1 = h+100
                crop_face_Image = img[y1:y1+h1,x1:x1+w1]
                print ('done')
            
            except:
                y2 = y-20
                x2 = x-20
                w2 = w+40
                h2 = h+40
                crop_face_Image = img[y2:y2+h2,x2:x2+w2]
                print ('done')
                
    except Exception as e:
        print (">>>>>",e)
    #cv2.imwrite("2.jpeg",crop_face_Image)
    return crop_face_Image

"""

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
                imgdata = functions.StringtoImg(imgstring)
                
                
                
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
    
    
    
class predImages(Resource):
    
    def post(self):
        imgstring = request.form.get("pred_img",0)
        imgdata = functions.StringtoImg(imgstring)
        with open("temp/tmp.jpeg", 'wb') as f:
            print("## in save")
            f.write(imgdata)
        #cv2.imwrite("1.jpeg",imgdata)
        imgdata = functions.cropFace("temp/tmp.jpeg")
        cv2.imwrite("temp/tmp_crop.jpeg",imgdata)
        #with open("2.jpeg", 'wb') as f:
        #    print("## in save")
        #    f.write(imgdata)
        
        return {
                "status":"200",
                "model": "GOT IT"
                }
            
    
api.add_resource(Helloworld, '/',
                 '/Helloword')


api.add_resource(userImages, '/api/images')

api.add_resource(predImages, '/api/pred_image')










if __name__ == '__main__':
    context = ("/home/ad.rapidops.com/pushkar.ambatkar/local_ssl/localhost.pem", "/home/ad.rapidops.com/pushkar.ambatkar/local_ssl/localhost.key")
    app.run(debug=True,
            host="0.0.0.0",
            ssl_context=context)
