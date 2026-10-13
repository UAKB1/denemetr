sayi = int(input("Enter a number: "))
i=1
if sayi < 0:
    print("negative number")
while i**2 <= sayi:
    i+=1
    if i**2 == sayi:
        print("u found it")
        break
    elif i**2 > sayi:
        print("not found")
    