#Find both union and intersection of two arrays

#Union of two arrays

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

intersection = []
for i in arr1:
  if i in arr2 and i not in intersection:
    intersection.append(i)

arr3 = arr1+ arr2
unionArr = []

for i in arr3:
  if i not in unionArr:
    unionArr.append(i)

print(intersection)
print(unionArr)

