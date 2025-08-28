#Intersection of arrays

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

intersection = []
for i in arr1:
  if i in arr2 and i not in intersection:
    intersection.append(i)

print(intersection)
