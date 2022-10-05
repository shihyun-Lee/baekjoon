n=int(input())
fac=1

for i in range(n,1,-1):
    fac*=i

fac=str(fac)
cnt=0

for i in range(len(fac)-1,-1,-1):
    if fac[i]=='0':
        cnt+=1
    else:
        print(cnt)
        break
