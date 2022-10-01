#알파벳 개수

alp=[0 for i in range(26)]
word=input()
for i in range(len(word)):
  alp[ord(word[i])-97]+=1
for i in range(len(alp)):
  print(alp[i],end=" ")