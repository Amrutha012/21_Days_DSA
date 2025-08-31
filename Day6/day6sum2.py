#Problem: Find the Index of the First Occurrence of an Element

arr = list(map(int, input().split()))
val = int(input())
for i in range(len(arr)):
  if arr[i] == val:
    print(i)
    break
else:
  print("-1")
