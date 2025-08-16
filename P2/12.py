string=input("enter a string")
check=input("enter a character to check")
count=0
for char in string:
    if char==check:
        count+=1
print(count)        
