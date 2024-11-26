a=int(input("enter first side"))
b=int(input("enter second side"))
c=int(input("enter third side"))

if a==b and b==c :
  print("eqilateral")
elif a==b or b==c or c==a :
  print("isoceles triangle")
else:
    print("scalene")