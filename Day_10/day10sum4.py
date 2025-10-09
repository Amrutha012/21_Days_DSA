# Check if an arr is sorted in decreasing order

arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:  
        print("No")
        break
else:
    print("Yes")
