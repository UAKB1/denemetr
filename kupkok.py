kup=input("Enter a number to find the cube root of:")
if float(kup) < 0:
    print(" The cube root of", kup, "is:", -1*abs(float(kup))**(1/3))
elif float(kup) == 0:
    print("The cube root of", kup, "is: 0")
else:
    print("The cube root of", kup, "is:", float(kup)**(1/3))
