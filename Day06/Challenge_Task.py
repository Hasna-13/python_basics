def Add(a,b):
    return a+b
def Subtract(a,b):
    return a-b
def Multiply(a,b):
    return a*b
def Divide(a,b):
        if b != 0:
          return a / b
        else:
          return "Error! Division by zero."

print("Choose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

op = int(input("Choose operation: "))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

if op==1:
    print(f"Result:{Add(a,b)}")
elif op==2:    
    print(f"Result:{Subtract(a,b)}")
elif op==3:
    print(f"Result:{Multiply(a,b)}")
elif op==4:
    print(f"Result:{Divide(a,b)}")
else:
    print("Enter valid option")    
