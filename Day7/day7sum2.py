#Duplicate with k distance in an Array
arr = [10, 5, 3, 4, 3, 5, 6]
k = 3
n = len(arr)

found = False

for i in range(n):
    for c in range(1, k + 1):
        j = i + c
        if j < n and arr[i] == arr[j]:
            found = True
            break 
    if found:
        break

print("Yes" if found else "No")
