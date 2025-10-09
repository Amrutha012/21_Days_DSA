#reverse an array

arr = list(map(int, input().split()))

l = 0
r = len(arr)-1

while l<r:
  arr[l],arr[r] = arr[r],arr[l]
  l = l+1
  r = r-1

print(arr)