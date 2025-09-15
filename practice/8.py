string=input("enter string")
rev=""
for char in string:
   rev=char+rev
if(rev==string):
  print("palindrome")
else:
   print("not palindrokme")  
