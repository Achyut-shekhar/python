# count frequency of each element in the array
arr=list(map(int,input().split()))
print(arr)
m={}

for i in range(len(arr)):
  if arr[i] not in m:
    m[arr[i]]=0
  m[arr[i]]+=1
  
print(m)