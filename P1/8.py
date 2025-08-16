num=int(input("enter a num"))
sum=0
prod=1
for i in range(1,num):
      a=num%10
      sum=sum+a
      prod=prod*a
      num=num/10
if sum==prod:
    print("spy")
else:
     print("not spy")    


