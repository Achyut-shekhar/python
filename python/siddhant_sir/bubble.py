def bubble_sort(arr):
  for j in range(len(arr)-1):
    swap=True
    for i in range(len(arr)-1-j):
      if(arr[i]>arr[i+1]):
        swap=False
        arr[i],arr[i+1]=arr[i+1],arr[i]
        if not swap:
          break
  print(arr)

arr=list(map(int,input().split()))

# for i in range 
print(arr)
bubble_sort(arr)
