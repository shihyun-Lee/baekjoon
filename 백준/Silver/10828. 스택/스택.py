# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 00:04:07 2022

@author: jeeni
"""
import sys
#스택
stack=[]
a=[]

n=int(input())

for i in range(n): 
    a=sys.stdin.readline().split()
    if a[0]=="push":
        stack.append(a[1])
    elif a[0]=="pop":
        if len(stack)!=0:
            print(stack.pop()) #맨 마지막 값 제거
        else:
            print("-1")
            
    elif a[0]=="size":
        print(len(stack))
        
    elif a[0]=="empty":
        if len(stack)!=0:
            print("0") #값이 참이면 0출력
        else:
            print("1")
            
    elif a[0]=="top":
        if (stack):
            print(stack[len(stack)-1])
        else:
            print("-1")
