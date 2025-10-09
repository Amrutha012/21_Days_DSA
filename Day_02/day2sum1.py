#unique elements

arr = list(map(int, input().split()))
uni_arr=[]

for val in arr:
  if val not in uni_arr:
    uni_arr.append(val)
print(uni_arr)
