#leaders in an array
arr = list(map(int, input().split()))
max_num = arr[-1]
leaders = []
for i in range(len(arr)-1,-1,-1):
  if arr[i]>=max_num:
    leaders.append(arr[i])
    max_num=arr[i]

leaders.reverse()
print(leaders)
