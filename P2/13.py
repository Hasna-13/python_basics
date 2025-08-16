nums=list(map(int,input("enter a list of number").split()))
largest=nums[0]
for num in nums:
    if num>largest:
         largest=num
nums.remove(largest)
largest=nums[0]
for num in nums:
    if num>largest:
         largest=num
print(largest)         
