#Reverse an array without using extra space

arr = list(map(int, input().split()))
n = len(arr)
for i in range(n//2):
  arr[i],arr[n-1-i] = arr[n-1-i],arr[i]

print(arr)