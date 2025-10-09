#Contains duplicates
arr = list(map(int, input().split()))
dup=[]

for i in arr:
  if i in dup:
    print("Found")
    break
  dup.append(i)
else:
    print("Not Found")