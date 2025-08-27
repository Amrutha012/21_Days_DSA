#find the missing number in an unsorted array:
arr = list(map(int, input().split()))
mis_arr=[]
arr.sort()
max_val = arr[0]
min_val = arr[0]
for i in range(len(arr)):
  if arr[i] > max_val:
    max_val = arr[i]

  if arr[i]<min_val:
    min_val = arr[i]

for i in range(min_val, max_val+1):
  if i not in arr:
    mis_arr.append(i)

print(mis_arr)