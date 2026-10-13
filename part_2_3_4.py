from secret_number import secret_number
guess = int(input("guess the secret number between 1 and 100: "))
for i in range(1, 5):
    if guess != secret_number:
        guess = int(input("guess the secret number between 1 and 100: "))
        if guess == secret_number:
            print("W")
        elif guess < secret_number:
            print("too low")
    else:
        print("too high")
        i = i +1
        if i > 5:
            print("you have used all your guesses")
while True:
                print("gg")#
