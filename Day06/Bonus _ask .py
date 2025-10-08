import random
length=int(input("enter length of passsword"))
N=input("Include number?(y/n):")
S=input("Include symbol?(y/n):")

letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!@#$%^&*()_+:?"


new_password=""
for i in range(0,length):
    new_password+=random.choice(letters)
    if N=='y':
     new_password+=random.choice(numbers)
    if S=='y':
      new_password+=random.choice(symbols)
    if len(new_password)==length:
      break
    
print(new_password)    
