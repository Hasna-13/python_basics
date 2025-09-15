string=input("enter a string")
count=0
count2=0
for char in string:
    if char in "aeiouAEIOU":
      count+=1
    else:
       count2+=1  
print(f"number of vowels:{count}")
print(f"number of consonent:{count2}")