string=input("enter a string")
count=0
for char in string:
    if char in "aeiouAEIOU":
         count+=1
print(count)         