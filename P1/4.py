num=int(input("Enter a number"))
n=num
sum=0
for i in range(1,num):
    if num%i==0:
      sum+=i
     
if n==sum:
      print("perfect")  
else:
    print("not perfect")          