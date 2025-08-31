#🧩 Problem: Count Positive, Negative, and Zero Elements in an Array

arr = list(map(int,input().split()))
pos_arr=[]
neg_arr=[]
zero_arr=[]

for i in arr:
  if i>0:
    pos_arr.append(i)
  elif i<0:
    neg_arr.append(i)
  else:
    zero_arr.append(i)

print(len(pos_arr), pos_arr)
print(len(neg_arr), neg_arr)
print(len(zero_arr), zero_arr)