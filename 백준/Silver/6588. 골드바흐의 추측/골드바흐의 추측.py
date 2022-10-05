#골드바흐의 추측
import sys
lst=[1 for i in range(1000000)]
lst[1]=0
for i in range(2,int((1000000)**0.5)+1):  #홀수 소수의 합이어야함
    if lst[i]!=0:
        for j in range(2*i,1000000,i):
            lst[j]=0


while(True):
    n=int(sys.stdin.readline().rstrip())
    if n==0:
        break
    for j in range(3,n): 
        if lst[j]==True and lst[n-j]==True:
            print(n,'=',j,'+',n-j)
            break
    if j==n-1:
        print("Goldbach's conjecture is wrong.")

    
