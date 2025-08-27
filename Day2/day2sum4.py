#find the pair of numbers equal to given target:

arr = list(map(int, input().split()))
target = 10 

arr.sort()
l = 0
r = len(arr)-1

found = False
while l<r:
  current_sum = arr[l] + arr[r]
  if current_sum == target:
    print("Yes we found", arr[l], arr[r])
    found = True
    l+=1
    r-=1
    
  elif current_sum < target:
    l += 1
  elif current_sum>target:
    r-=1
if not found:
  print("no elements found")