# creating a python.txt file and take input from user 

import csv

with open("D:\\23BCA309\\sqlite-tools-win-x64-3460000\\csv\\python.txt","w")as txt:
    cur=csv.writer(txt)

op='n'
l=[]
while op!='y':
    sentence=input()
    l.append(sentence)
    op=input("want to end(y/n):")
    
    

cur.writerow(l)
