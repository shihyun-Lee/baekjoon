#골드바흐 파티션-몇개 성립하는지
import sys
lst=[1 for i in range(1000000)]
lst[1]=0
for i in range(2,int((1000000)**0.5)+1):  #홀수 소수의 합이어야함
    if lst[i]!=0:
        for j in range(2*i,1000000,i):
            lst[j]=0

N=int(input())
for i in range(N): 
    n=int(sys.stdin.readline().rstrip())
    cnt=0
    for j in range(2,n//2+1):  #중복처리 안되기 위해서 절반만 반복
        if lst[j]==True and lst[n-j]==True:
            cnt+=1
    print(cnt)
    
