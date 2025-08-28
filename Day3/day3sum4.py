#Remove the commom number from arr1 and print the remaining from the two arrays

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

intersection = []
for i in arr1:
  if i in arr2:
    intersection.append(i)

  if i in arr2 and i in intersection:
    arr1.remove(i)

print(arr1)