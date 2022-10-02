#최대공약수,최소공배수
a,b=map(int,input().split())
maxi=1
min=a*b
if a<b:
    tmp=a
    multi=b
else:
    tmp=b
    multi=a
for i in range(2,tmp+1):
    if a%i==0 and b%i==0:
        maxi=i
for i in range(multi,a*b):
    if i%a==0 and i%b==0:
        min=i
        break
        
print(maxi)
print(min)
