import qrcode   
import time
from datetime import datetime
import random
import string
import cv2
from fileinput import filename
import os
import smtplib
import imghdr
from email.message import EmailMessage
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

student_list =[]
adminEmail = "k.bezuayeho22@bosco.org"
time_list = []
location_list = []
file_list = []

now = datetime.now()
current_time = now.strftime("%H%M")
time = int(current_time)
endTime= time + 5

def scan():
    x=0
    timer = time + 1
    myData=" "
    while time < timer:
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode("utf-8")
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
            extract(myData)
        cv2.waitKey(1)
        x = x + 1
    x = 0

def extract(qr):
    n = 0
    new = ""
    for x in qr:
        if qr[n] != "-":
            new = new + qr[n]
            n = n+1
    if new not in student_list:
        student_list.append(new)
        location_list.append("321")
        time_list.append(now.strftime("%H:%M"))
        print(student_list)
        print(location_list)
        print(time_list)



while time != 1325:
    user = input("What would you like to do?\nexpand, find student, scan, email codes, or end\n")
    if user == "scan":
        scan()
    
    

