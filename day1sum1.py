arr=list(map(int, input().split()))
lar = arr[1]

for i in range(len(arr)):
  if arr[i]>lar:
    lar=arr[i]

print("The largest element in the arr is:", lar)