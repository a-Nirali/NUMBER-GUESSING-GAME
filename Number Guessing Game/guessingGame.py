import random
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
chances = 0
print("Guess a number(Between 1 and 9):")

while chances < 5:
    guess=int(input("Enter Your Guess:"))
    if guess == number:
        print("Congratulation YOU WON!!!")
        break
    elif guess < number:
        print("Your Guess Was Too Low: Guess a Number Higher Than",guess)
    else:
        print("Your Guess Was Too High: Guess a Number Lower Than",guess)
    chances +=1

    if not chances <5 :
            print("You Lose!!! The Number Is",number)