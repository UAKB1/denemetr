a = 5
area = 3**0.5/4*a**2
print(area)
s = "Aho54yuBEKIR42z.89tur"
print("my name is", f"{s[11:6:-1]}")
x = float(input("what x to find the cube root of"))
g = float(input("what guess to start with"))
next_guess = (g -(g**3 -x)/(3*g**2))
print("next guess", next_guess)