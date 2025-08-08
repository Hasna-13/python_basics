first=float(input("Enter first number"))
operation=input("enter operation")
second=float(input("enter second number"))
match operation:
    case "+":
        result = first + second
        print(result)
    case "-":
         result = first - second
         print(result)
    case "*":
         result = first * second
         print(result)
    case "/":
         result = first / second
         print(result)          
