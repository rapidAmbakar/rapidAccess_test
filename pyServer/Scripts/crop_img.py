import os
import path
import face_recognition
import cv2

categories = os.listdir("rapidFaces_interns")
# print (categories)

def crop_face(img_path):
    crop_face_Image = (0,255,0)
    try:
        img = cv2.imread(img_path)
        face_location = face_recognition.api.face_locations(img,model='hog')        
        try:
            xx,xy,yx,yy = face_location[0]
            y1 = xx-50
            x1 = yy-50
            w1 = xy+100
            h1 = yx+100
            crop_face_Image = img[y1:y1+h1,x1:x1+w1]
        except:
            xx,xy,yx,yy = face_location[0]
            y1 = xx-20
            x1 = yy-20
            w1 = xy+40
            h1 = yx+40
            crop_face_Image = img[y1:y1+h1,x1:x1+w1]
            print ('done')
    except Exception as e:
        print (">>>>>",e)
    return crop_face_Image

crop_img = crop_face("MicrosoftTeams-image.png")
