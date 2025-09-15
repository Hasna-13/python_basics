a=list(map(int,input("Enter 3 number").split()))
large=a[0]
for num in a:
    if num>large:
        large=num

print(large)        
