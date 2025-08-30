#Remove duplicates from the sorted array

arr = list(map(int, input().split()))
arr.sort()
common = []
duplicate = []
for i in arr:
  if i in common:
    duplicate.append(i)
  else:
    common.append(i)

print(common)