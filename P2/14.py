nums=list(map(int,input("Enter a number").split()))
uniquenums=[]
for num in nums:
    if num not in uniquenums:
      uniquenums.append(num)
print(nums)
print(uniquenums)