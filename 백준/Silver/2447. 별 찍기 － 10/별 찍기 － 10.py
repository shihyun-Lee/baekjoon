#별 찍기-리스트 이용
global list
def triple(list,n):

  if n==1:
    return 0
  triple(list,n//3)
  for i in range(1,len(list)):
    if i%n>=n//3 and i%n<n/3*2:
      for j in range(1,len(list)):
        if j%n>=n//3 and j%n<n/3*2:   # 여기서 홀수번째일시 구명
          list[i][j]=0

  return 0


n=int(input())
list=[[1 for i in range(n)] for i in range(n)]
triple(list,n)
for i in range(n):
  for j in range(n):
    if list[i][j]==0:
      print(" ",end="")
    else:
      print("*",end="")
  print()