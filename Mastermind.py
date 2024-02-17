import random # Allowing python to generate random things
guessesTaken = 0 # Setting variable to 0
numberscorrect = 0 # Setting variable to 0

print("Welcome to Mastermind") # Telling the player "Welcome to Mastermind"

number1 = random.randint(1, 9) # Generating random digits
number2 = random.randint(1, 9)
number3 = random.randint(1, 9)
number4 = random.randint(1, 9)

print("In this game you have to guess a 4 digit number") # Explaining the rules of the game
print("You will be asked to enter your number 1 digit at a time in the order (1,2,3,4)")
print(" ") # Creating a blank line so the reader can read the writing easier

while numberscorrect < 4: # Start of loop
    numberscorrect = 0 # Setting variable to 0 so when the loop repeats it doesn`t keep adding
    print("Please enter your first digit") # Telling the player what to do
    guess1 = int(input()) # Allowing the player to input a number and setting the guess variable to their input
    if guess1 == number1: # Processing if the number is correct
        numberscorrect = numberscorrect + 1 # Saying that if the number is correct to add on a point to be told later
    
    print("Please enter your second digit") # Repeat of above code
    guess2 = int(input())
    if guess2 == number2:
        numberscorrect = numberscorrect + 1

    print("Please enter your third digit")
    guess3 = int(input())
    if guess3 == number3:
        numberscorrect = numberscorrect + 1
    
    print("Please enter your forth digit")
    guess4 = int(input())
    if guess4 == number4:
        numberscorrect = numberscorrect + 1

    print(" ")
    print("Here is how many numbers you guessed correctly:") # Telling the player how many numbers they got correct
    print(numberscorrect)
    if numberscorrect < 4: # If they didn`t get all 4 digits correct the loop repeats until they are all correct
        print("Try again") # Telling the player the code is letting them try again
    else:
       break # End of loop
print("Well done!  You guessed correctly!") # Telling the player that they were successful and the game is now over






