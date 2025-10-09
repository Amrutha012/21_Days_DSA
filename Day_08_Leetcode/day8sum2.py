nums = list(map(int, input().split()))
nums.sort()

if nums[0] != 0:
    print(0)
else:
    found = False
    for i in range(len(nums)-1):
        if nums[i+1] - nums[i] > 1:
            print(nums[i] + 1)
            found = True
            break
    if not found:
        print(len(nums))
