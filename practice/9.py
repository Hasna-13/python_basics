string=input("enter string")
m=len(string)
flag=0
for i in range(1,m):
    if string[i]!=string[m-i-1]:
        flag=1
if flag==1:
  print("not")
else:
   print("palindrome")  