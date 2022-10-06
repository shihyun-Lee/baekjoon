import sys
n,k=map(int,input().split())
coin=[]
for i in range(n):
  coin.append(int(sys.stdin.readline().rstrip()))
cnt=0
for i in range(n-1,-1,-1):
  cnt+=k//coin[i] #개수추가
  k=k-k//coin[i]*coin[i] #그만큼 빼주기
  
print(cnt)