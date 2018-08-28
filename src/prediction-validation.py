# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 19:01:14 2018

@author: heman
"""
import itertools
#Reading the input files line by line stripping off the newline character
actual = open("./input/actual.txt","r")
actual = [line.rstrip('\n') for line in actual]
predict = open("./input/predicted.txt","r")
predict = [line.rstrip('\n') for line in predict]
window = open("./input/window.txt")
window = int([line.rstrip('\n') for line in window])
file = open('./output/comparison.txt', 'w')
#Creating matrices splitting at pipeline character
for i in range(len(actual)):
    actual[i] = actual[i].split("|")
    
for j in range(len(predict)):
    predict[j] = predict[j].split("|")

'''    
max = int(predict[-1][0])
for k in range(1,max):
    if(k+(window-1)<=max):
        print("{} {}".format(k,k+(window-1)))
'''
'''    
#Parsing through the matrix 
for i in range(len(predict)):
    for j in range(len(actual)):
        if((actual[j][0]==predict[i][0]) and (actual[j][1]==predict[i][1]) and (float(actual[j][0]) in range(1,window+1))):
            avg.append(abs(float(actual[j][2])-float(predict[i][2])))

average_error = round(sum(avg)/float(len(avg)),2)
print("1"+"|"+"2"+"|"+"{}".format(average_error))
'''

#max = int(predict[-1][0])
'''
for k in range(1,max):
    avg = []
    if(k+(window-1)<=max):
        for i in range(len(predict)):
            for j in range(len(actual)):
                if((predict[i][:2] == actual[j][:2]) and (float(actual[j][0]) in (k,k+(window-1)))):
                    avg.append(abs(float(actual[j][2])-float(predict[i][2])))
        print("{}|{}|{}".format(k,k+(window-1),round(sum(avg)/float(len(avg)),2)))

k = 1       
for i in range(len(predict)):
    for j in range(len(actual)):
        if((predict[i][:2] == actual[j][:2]) and (float(actual[j][0]) in range(k,k+window))):
            avg.append(abs(float(actual[j][2])-float(predict[i][2])))
print("{}|{}|{}".format(k,k+(window-1),round(sum(avg)/float(len(avg)),2)))       
'''
max = int(predict[-1][0])
for k in range(1,max):
#    avg = []
    if(k+(window-1)<=max):            
        avg = [(abs(float(actual[j][2])-float(predict[i][2]))) for i,j in itertools.product(range(len(predict)),range(len(actual))) if ((predict[i][:2] == actual[j][:2]) and (float(actual[j][0]) in range(k,k+window)))]     
        file.write("{}|{}|{}\n".format(k,k+(window-1),round(sum(avg)/float(len(avg)),2))) 
file.close()        
