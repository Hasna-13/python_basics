num=int(input("enter a number"))
b=0
sum=0
while num>0:
    a=num%10
    b=b*10+a
    num=num//10
    sum=sum+a
print(sum)    
