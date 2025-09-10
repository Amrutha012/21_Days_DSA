#ROTATE AN ARRAY K STEPS TO THE RIGHT

arr = list(map(int, input().split()))
k = int(input())

k = k % len(arr) 
arr = arr[-k:] + arr[:-k]

print(arr)
