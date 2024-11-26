def rev(n):
    reverse=0
    while(n!=0):
        rem=n%10
        reverse=reverse*10+rem
        n=n//10
    return reverse

n=int(input("enter number"))
res=rev(n)
print(res)