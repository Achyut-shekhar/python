# 2^3+4^5+6^7
n=int(input("enter series number"))
sum=0

for i in range (2,n+2,2):
        sum=sum+i**(i+1)
print(sum)