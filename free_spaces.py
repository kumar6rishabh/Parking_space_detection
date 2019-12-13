import cv2
import numpy as np
import multiprocessing
from multiprocessing import Process , Queue

import smtplib

sender_email = "rishabh.kumar2017@vitstudent.ac.in"
sender_pass = "40194965"
receiver_email = input("Enter the receiver mail address: ")
receiver_email = receiver_email
subject = "Free Parking spaces are: "
#content = input("Enter the content of the mail: ")
mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(sender_email,sender_pass)
#message = "Subject: {}\n\n{}".format(subject, content)
#mail.sendmail(sender_email, receiver_email, message)


'''nm = input("Enter the name of the image: ")
nm += '.png'
img = cv2.imread(r"./parking_photos/"+nm)'''

up_mask = np.ones((300 , 200 , 3) , np.uint8)
up_mask *= 255
cv2.line(up_mask , (0 , 0) , (0 , 300) ,(0 , 0 , 0) , 20)
cv2.line(up_mask , (200 , 0) , (200 , 300) ,(0 , 0 , 0) , 20)
cv2.line(up_mask , (0 , 300) , (200 , 300) ,(0 , 0 , 0) , 20)
cv2.circle(up_mask , (100 , 150) , 30 , (0 , 0 , 0) , -1)

down_mask = np.ones((300 , 200 , 3) , np.uint8)
down_mask *= 255
cv2.line(down_mask , (0 , 0) , (0 , 300) ,(0 , 0 , 0) , 20)
cv2.line(down_mask , (200 , 0) , (200 , 300) ,(0 , 0 , 0) , 20)
cv2.line(down_mask , (0 , 0) , (200 , 0) ,(0 , 0 , 0) , 20)
cv2.circle(down_mask , (100 , 150) , 30 , (0 , 0 , 0) , -1)
#cv2.imshow('down_mask' , down_mask)
#cv2.waitKey(0)

'''im1 = img[0:300 , 0:200]
im2 = img[0:300 , 200:400]
im3 = img[0:300 , 400:600]
im4 = img[0:300 , 600:800]
im5 = img[0:300 , 800:1000]
im6 = img[0:300 , 1000:1200]

im7 = img[300:600 , 1000:1200]
im8 = img[300:600 , 800:1000]
im9 = img[300:600 , 600:800]
im10 = img[300:600 , 400:600]
im11 = img[300:600 , 200:400]
im12 = img[300:600 , 0:200]'''

def find_spaces(images , q):
    for i , image in images:
        pic_no = i
        im = image
        lis = []
        #print(image)
        img = cv2.imread(im)
        #pic_no = int(im[-1])
        #print(pic_no)
        im1 = img[0:300 , 0:200]
        im2 = img[0:300 , 200:400]
        im3 = img[0:300 , 400:600]
        im4 = img[0:300 , 600:800]
        im5 = img[0:300 , 800:1000]
        im6 = img[0:300 , 1000:1200]

        im7 = img[300:600 , 1000:1200]
        im8 = img[300:600 , 800:1000]
        im9 = img[300:600 , 600:800]
        im10 = img[300:600 , 400:600]
        im11 = img[300:600 , 200:400]
        im12 = img[300:600 , 0:200]

        temp1 = cv2.subtract(up_mask , im1)
        if(((temp1.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(1)
        temp2 = cv2.subtract(up_mask , im2)
        if(((temp2.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(2)
        temp3 = cv2.subtract(up_mask , im3)
        if(((temp3.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(3)
        temp4 = cv2.subtract(up_mask , im4)
        if(((temp4.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(4)
        temp5 = cv2.subtract(up_mask , im5)
        if(((temp5.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(5)
        temp6 = cv2.subtract(up_mask , im6)
        if(((temp6.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(6)
        temp7 = cv2.subtract(down_mask , im7)
        if(((temp7.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(7)
        temp8 = cv2.subtract(down_mask , im8)
        if(((temp8.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(8)
        temp9 = cv2.subtract(down_mask , im9)
        if(((temp9.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(9)
        temp10 = cv2.subtract(down_mask , im10)
        if(((temp10.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(10)
        temp11 = cv2.subtract(down_mask , im11)
        if(((temp11.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(11)
        temp12 = cv2.subtract(down_mask , im12)
        if(((temp12.sum(axis = 1)).sum(axis = 0)).sum(axis = 0) > 0):
            lis.append(12)
        here = []
        st = ""
        ar = list(range(1 , 13))
        for em in ar:
            if em not in lis:
                st += str(em)+" , "
        #print(st)
        #message = "Subject: {}\n\n{}".format(subject, st)
        #mail.sendmail(sender_email, receiver_email, message)
        print("lis is " , lis)
        here.append(pic_no)
        here.append(lis)
        #print(lis)
        q.put(here)
        #print(q.get())
def print_empty(q):
    #print("here")
    while not q.empty():
        print("het")
        t = q.get()
        lane_no = t[0]
        for no in t[1]:
            print("lis is " , no)

q = multiprocessing.Queue()
img1 = './photos/0(0).png'
img2 = './photos/1(1).png'
img3 = './photos/1(6).png'
img4 = './photos/1(9).png'
img5 = './photos/2(19).png'
img6 = './photos/3(169).png'
images = []
images.append([1 , img1])
images.append([2 , img2])
images.append([3 , img3])
images.append([4 , img4])
images.append([5 , img5])
images.append([6 , img6])
#print(images)
p1 = multiprocessing.Process(target = find_spaces , args = (images , q))
p2 = multiprocessing.Process(target = print_empty , args = (q,))

p1.start()
p2.start()

p1.join()
p2.join()

