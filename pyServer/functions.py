import base64


import face_recognition
import cv2

import os


cascade_path = "haarcascade_frontalface_default.xml"
casecade = cv2.CascadeClassifier(cascade_path)


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