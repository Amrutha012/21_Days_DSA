#Check if the arr is sorted or not

arr = list(map(int,input().split()))
arr1 = arr.copy()
arr1.sort()

if arr == arr1:
  print("Array is sorted")
else:
  print("Array is not sorted")