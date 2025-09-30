F=float(input("Enter temperature in Fahrenheit:"))
def Farenheit(F):
    C = (F - 32) * 5/9
    return C
celsius=Farenheit(F)
print(celsius)