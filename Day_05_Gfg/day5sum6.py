#Rotate an array(RIGHT ROTATION)

arr = list(map(int, input().split()))
k = int(input())
k = k % len(arr)

rotate_arr = arr[-k:] + arr[:-k]

print(rotate_arr)