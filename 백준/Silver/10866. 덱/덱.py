from collections import deque
import sys
deq=deque()
n=int(input())

a=[]
for i in range(n):
  a=sys.stdin.readline().split()
  if a[0]=="push_front":
    deq.appendleft(a[1]) #왼쪽에 요소추가
  elif a[0]=="push_back":
    deq.append(a[1])
  elif a[0]=="pop_front":
    if deq:
      print(deq.popleft())  #왼쪽요소 삭제
    else:
      print("-1")
  elif a[0]=="pop_back":
    if deq:
      print(deq.pop()) #오른쪽 요소 삭제
    else:
      print("-1")
  elif a[0]=="size":
    print(len(deq))
  elif a[0]=="empty":
    if len(deq)==0:
      print("1")
    else:
      print("0")
  elif a[0]=="front":
    if len(deq)==0:
      print("-1")
    else:
      print(deq[0 ])
  elif a[0]=="back":
    if len(deq)==0:
      print("-1")
    else:
      print(deq[len(deq)-1])