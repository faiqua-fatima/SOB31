import random

def compare_numbers(number, user_guess): #faiqua fatima defined a function to play the game
    cows=0#faiqua fatima set initial conditions
    bulls=0
    for i in range(len(number)):#faiqua fatima added a for loop
        if user_guess[i]==number[i]:#faiqua fatima added if condition
            bulls+=1
        elif user_guess[i] in number:#faiqua fatima added else condition
            cows+=1

    return cows,bulls

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number #faiqua fatima changed 0 to 1000
guesses = 0
print(number) #faiqua fatima added () after print to contain number

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")#faiqua fatima replaced raw input to input
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
