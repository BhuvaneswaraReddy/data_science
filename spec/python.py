import os
from pandas import read_csv
from l_r import linear_regression
# from linear_regression import linear_regression
from sample import printk
# def sel(k):
#     v = input("Select 1 - Regression 2- Classification :")
#     print(v)
#     if v == "1":
#         return(linear_regression(k)
#         )        
#     elif v == "2":
#         p = ("2 selected")
#         return 2
#     else:
#         return 0
# path = r"E:\spec\Boston.csv"
# data = read_csv(path)
# linear_regression(data)

# fileofname = input("enter the file name:")
# fileObject = open(fileofname, 'r')
# for line in fileObject:
#     print(line)
# my_list = [line.rstrip('\n') for line in fileObject]
v = input("Select 1 - Linear Regression 2- Classification :")
if v == "1":
    linear_regression()    
elif(v == "2"):
    p = ("2 selected")
    print("2")
else:
    print("0")

