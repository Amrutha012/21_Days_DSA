def findUnique(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


arr1 = [2, 3, 5, 4, 5, 3, 4]
print(findUnique(arr1)) 

arr2 = [2, 2, 5, 5, 20, 30, 30]
print(findUnique(arr2))
