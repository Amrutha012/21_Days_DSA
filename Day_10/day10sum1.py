#FIND THE SECOND LARGEST ELEMENT IN AN UNSORTED ARRAY 

arr = list(map(int, input().split()))
max_num = arr[0]
second_max = float('-inf')

for i in range(len(arr)):
    if arr[i]>max_num:
        second_max = max_num
        max_num = arr[i]
    elif arr[i]>second_max and arr[i]!=max_num:
        second_max = arr[i]
        
   
print(second_max)
        
'''
2nd method:
arr = list(map(int, input().split()))
arr.sort()
print(arr[-2])
'''

