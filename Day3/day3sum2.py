#Union of two arrays

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr3 = arr1+ arr2
unionArr = []

for i in arr3:
  if i not in unionArr:
    unionArr.append(i)

print(unionArr)

