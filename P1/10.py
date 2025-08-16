nums=list(map(int,input("enter a list").split()))
large=nums[0]
for num in nums:
   if num>large:
      large=num

print(large)      
