#Rotate an array(LEFT ROTATION)

arr = list(map(int, input().split()))
k = int(input("Enter the number of steps for left rotation:"))

k = k%len(arr)

left_rotate = []
left_rotate = arr[k:]+arr[:k]

print(left_rotate)