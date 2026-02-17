gimee = input("Rain the simple mathematical problems ")

x, y, z = gimee.split(" ")
x = float(x)
z = float(z)

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "*":
    print(x*z)
elif y == "/":
    if z == 0:
        print("This calculation is not posssible")
    else:    
        print(x/z)
else: print("Yoo, the Calculation is little complex for me to now!!")            