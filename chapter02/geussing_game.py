#
def main():
    print("im thinking of a number between 1 and 100")

    magic_number = 55

    guess = 0

    while guess != magic_number:


        guess = eval (input)("what is your guess")
        if guess < magic_number:
            print ("your to low")

        elif guess > magic_number:
            print("your to high")

        else:
            print ("you got it!")


        main()
