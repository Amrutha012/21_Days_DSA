arr = list(map(int, input().split()))
new_arr=[]
arr2 = []

for i in arr:
  if i == 0:
    new_arr.append(i)
  else:
    arr2.append(i)

print(arr2+new_arr)