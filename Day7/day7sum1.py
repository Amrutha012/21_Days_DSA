# Minimum increment by k operations to make all equal

arr = list(map(int, input().split()))
k = int(input())

max_ele = max(arr)   # directly use max() for simplicity
target = 0
possible = True

for i in range(len(arr)):
    if (max_ele - arr[i]) % k != 0:
        possible = False
        break
    else:
        target += (max_ele - arr[i]) // k

if possible:
    print(target)
else:
    print(-1)
