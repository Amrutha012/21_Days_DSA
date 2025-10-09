#Move all the zeroes to the end of an array without changing indices of the elements

arr = list(map(int, input().split()))
count=[]
val=[]
for i in range(len(arr)):  #we can also access element directly bu using 'i'
  if arr[i]!= 0:           #here is 'i'
    val.append(arr[i])     #here is 'i'
  else:
    count.append(arr[i])   #here is 'i'

print(val+count)