arr=list(map(int, input().split()))
smaller = arr[1]

for i in range(len(arr)):
  if arr[i]<smaller:
    smaller=arr[i]

print("The samllest element in the arr is:", smaller)