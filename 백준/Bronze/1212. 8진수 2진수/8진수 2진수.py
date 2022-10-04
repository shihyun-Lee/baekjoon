#2진수 8진수
n=int(input(),8) #8진수 입력방법

tmp=bin(int(n))
tmp = format(n, 'b')
print(tmp)