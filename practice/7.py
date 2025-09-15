nums=list(map(int,input("enter number to sort").split()))
temp=0
for i in range(len(nums)-1):
      if nums[i]>nums[i+1]:
         temp=nums[i]
         nums[i]=nums[i+1]
         nums[i+1]=temp
print(nums)