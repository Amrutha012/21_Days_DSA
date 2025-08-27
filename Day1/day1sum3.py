#SECOND LARGEST ELEMENT IN AN ARRAY

arr = list(map(int, input().split()))
arr.sort()

print(arr[-2])