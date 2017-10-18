# This program converts meters per second into mph
def main():
    mps = eval(input("What is the speed in meters per second? "))
    if mps < 0:
        print("Invalid input!")
    else:
        mph = mps * 2.23694
        print("The speed is", mph, "mph")

main()
