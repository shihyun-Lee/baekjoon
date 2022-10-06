n=int(input())

for i in range(2,n+1):
  #소인수 분해
  while n%i==0:
    if n%i==0:
      print(i)
      n//=i