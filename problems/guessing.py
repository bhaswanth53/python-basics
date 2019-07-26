import random

num = random.randint(1, 9)

choice = []

have = True

while have :
    guess = int(input("Guess the number:\n"))
    if(guess == num) :
        print "Well done, you won the game"
        choice.append(guess)
        have = False
    elif(guess == 00) :
        print "LOL, you exit the game. The answer is ", num
        have = False
    else :
        print "Wrong choice, try again"
        choice.append(guess)
        have = True

print "The choices you made is\n",choice