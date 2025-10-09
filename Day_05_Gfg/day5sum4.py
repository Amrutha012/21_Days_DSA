#print all the sub arrays in the array

arr = list(map(int, input().split()))
for i in range(len(arr)):
  sub_arr=[]
  for j in range(i, len(arr)):
    sub_arr.append(arr[j])
    print(sub_arr)