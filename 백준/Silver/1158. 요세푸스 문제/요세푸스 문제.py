from collections import deque
 
que=deque()
lst=[]
a,b=map(int,input().split())

for i in range(a):
  que.append(i+1)

for i in range(a):
  que.rotate(-(b-1))
  lst.append(que.popleft())
print("<",end="")
for i in range(a-1):
  print(lst[i],end=", ")
print(lst[-1],end=">")