n=input()
length=len(n)
n=int(n)
temp=int(n)
result=0
while temp>0:
  result=result+(temp%10)**length
  temp=temp//10
if result==n:
  print("armstrong")
else:
  print("not armstrong")