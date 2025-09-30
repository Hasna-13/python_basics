print("Rectangle Calculator")
def perimeter(L,W):
   return 2 * (L + W)
def area(L,W):
   return L*W
L=int(input("Length:"))
W=int(input("Width:"))
P=perimeter(L,W)
A=area(L,W)
print(f"Perimeter:{P}")
print(f"Area:{A}")