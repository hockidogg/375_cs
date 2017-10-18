# this program was created to calculate your score
def main():
    total = 0
    denomanater = 0
    score = input("what is the score ")
    while score !="":
        total = total + eval (score)
        score = input ("whats the next score? ")
        denomanater = denomanater + 1
    print (total / denomanater,"is the average")


main()
