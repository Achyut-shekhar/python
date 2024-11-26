def factorial(n):
    s=1 
    a=0
    for i in range(1,n+1):
      s=s*i
      a=a+s
    return a

n=int(input("enter the number"))
res=factorial(n)
print(res)