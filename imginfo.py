# Writing to an excel  
# sheet using Python 
import xlwt 
import os
from xlwt import Workbook 
from glob import glob                                                          
import cv2 
jpgs = glob('D:/Users/Abel/Documents/ocv/colorized/jpg10k/*.jpg')
path = 'D:/Users/Abel/Documents/ocv/colorized/valdb'
  
# Workbook is created 
wb = Workbook() 
i=0  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
  
for j in jpgs:
    img = cv2.imread(j)
    print (j[45:-4]) 
    h,w,c = img.shape
    print (h,w)
    info = os.stat(j)
    print(info.st_size/1024)
    img1 = cv2.imread('D:/Users/Abel/Documents/ocv/colorized/valdb/' + j[45:-4] + '.jpeg')
    hr,wr,cr = img1.shape
    print (hr,wr)
    info1 = os.stat('D:/Users/Abel/Documents/ocv/colorized/valdb/' + j[45:-4] + '.jpeg')
    print(info1.st_size/1024)
    sheet1.write(i, 0, j[45:-4]) 
    sheet1.write(i, 1, hr) 
    sheet1.write(i, 2, wr) 
    sheet1.write(i, 3, info1.st_size/1024) 
    sheet1.write(i, 4, h) 
    sheet1.write(i, 5, w) 
    sheet1.write(i, 6, info.st_size/1024) 
    i+=1
    
wb.save('imgcomp.xls') 