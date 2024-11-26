flag=0
n=int(input("enter the number"))
for i in range(2,int(n**0.5)):  
 # n**0.5==n^0.5 and this is square root of the number
  if(n%i==0):
    flag=1
    break
if(flag):
  print("not prime")
else:
  print("prime")
  # every prime number is +1 or -1 of 6 multiple