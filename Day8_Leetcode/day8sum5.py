#Make even positions as greater than odd

arr = list(map(int, input().split()))
for i in range(len(arr)):
  if (i+1)%2 == 0:
    if arr[i]<arr[i-1]:
      arr[i],arr[i-1] = arr[i-1],arr[i]
    
print(arr)