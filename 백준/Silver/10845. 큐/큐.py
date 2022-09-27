# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 13:57:41 2022

@author: jeeni
"""
import sys
#큐 구현하기-하나의 배열이라고 생각해보자
global que #큐 리스트를 전역변수로 설정
que=[]
#정수 x를 큐에 넣는 함수
def push(x):
    que.append(x)
    return
    
#큐에서 가장 앞에 있는 정수 빼고 그 수 출력 정수 없을 시 -1
def pop():
    a=-1
    for i in range(len(que)):
        if que[i]:
            a=i
            break
    if a==-1:
        print("-1")
    else:
        print(que.pop(a))
    return 

#큐에 들어있는 정수의 개수 출력
def size():
    cnt=0
    for i in range(len(que)):
        if que[i]:
            cnt+=1
    print(cnt)
    return
        
#큐가 비어있는가
def empty():
    if que:
        print("0") #큐가 값이 있으면
    else:
        print("1") #비어있을 때
    return

#큐의 가장 앞에 있는 정수 출력.없으면 -1
def front():
    for i in range(len(que)):
        if que[i]:
            print(que[i])
            return
            
    print("-1") #값없으면 -1출력
    return
    
#큐의 가장 뒤에 있는 정수 출력.없으면 -1
def back():
    if que:
        print(que[len(que)-1])
    else:
        print("-1")
    return
    
n=int(input())
a=[]
for i in range(n):
    a=sys.stdin.readline().split()
    
    if "push" in a[0]:
        push(int(a[1]))
    elif a[0]=="pop":
        pop() #매개 변수 없는 함수 사용시
    elif a[0]=="size":
        size()
    elif a[0]=="empty":
        empty()
    elif a[0]=="front":
        front()
    elif a[0]=="back":
        back()
     