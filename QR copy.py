import qrcode   
import time
import datetime
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
random_number = []
email_list = []
time_list = []
location_list = []
file_list = []

def qrMake():
    q = 0
    for x in random_number:
        img = qrcode.make(x)
        k = str(random.randint(1,100000000))
        imgName = student_list[q]+ k +".jpeg"
        file_list.append(imgName)
        img.save(imgName)
        q = q + 1

def email():
    q = 0
    tday = datetime.date.today()
    for x in email_list:
        msg = EmailMessage()
        msg['Subject'] = 'QR code for the day'
        msg['From'] = "projectwhereabouts2022@gmail.com"
        msg['To'] = x
        msg.set_content("Dear "+student_list[q]+', this is your QR code for the day. Please scan at QR code station located near teacher\'s desk. This QR code is only viable for the date '+str(tday))
        with open(file_list[q], "rb") as f:
            file_data = f.read()
            file_type = imghdr.what(f.name)
            file_name = f.name
        msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=f.name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("projectwhereabouts2022@gmail.com", "e2W!+7@Z")
            smtp.send_message(msg)
        q=q+1

def expand():
    name = input("What is the student's name?(Firstname Lastname)\n")
    email = input("What is student's email?\n")
    num = random.randint(1000,10000)
    r = str(num)
    email_list.append(email)
    student_list.append(name)
    random_number.append(r)
    time_list.append("_")
    location_list.append("_")


    img = qrcode.make(r)
    k = str(random.randint(1,100000000))
    imgName = name + k +".jpeg"
    file_list.append(imgName)
    img.save(imgName)


def scan():
    x=0
    myData=" "
    while x != 300:
        success, img = cap.read()
        for barcode in decode(img):
            myData = barcode.data.decode("utf-8")
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(255,0,255),5)
            compare(myData)
        cv2.waitKey(1)
        time.sleep(1)
        x = x + 1
    x = 0

def compare(qr):
    n = 0
    for x in random_number:
        if random_number[n] == qr:
            print(student_list[n])
        n=n+1

x = 1
while True:
    user = input("What would you like to do?\nexpand, find student, scan, email codes, or end\n")
    if user == "expand":
        expand()
    elif user == "end":
        x = 1
    elif user == "scan":
        scan()
    elif user == "email":
        email()
    elif user == "print":
        print(random_number)
        print(student_list)
        print(email_list)
        print(file_list)
