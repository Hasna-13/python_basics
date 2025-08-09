import random
secret_number=random.randint(1,10)
attempts=0
while True:
    guess=int(input("guess number b/w 1to 10"))
    attempts+=1

    if guess<secret_number:
       print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Correct! You won in {attempts} tries.")
        break 
