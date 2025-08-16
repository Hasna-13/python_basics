nums1=input("enter number")
nums2=input("enter number")
flag=0
if len(nums1)==len(nums2):
    for i in range(len(nums1)):
        for  j in range(len(nums2)):
            if i==j:
              flag=1
            else:
                flag=0  
if(flag==1):
    print("true")