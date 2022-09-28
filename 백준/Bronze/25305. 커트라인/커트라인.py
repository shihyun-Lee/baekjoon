
import sys
a,b=map(int,input().split())
lst=[]

lst=list(map(int,sys.stdin.readline().split()))

lst.sort(reverse=True)
print(lst[b-1])
