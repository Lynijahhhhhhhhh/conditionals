# author:
# date:

# --------------- # Section 3 # --------------- #
# ---------- # Part 1 # ---------- #

print('----- Section 3 -----'.center(25))
print('--- Part 1 ---'.center(25))

# Guessing Game - Warm Cold
#
# This is a spin on the number guessing game where the user must guess the correct number between 1 and 100. The
#   unknown number is random. The twist --> Instead of saying 'Too High' or 'Too Low', instead you will tell the user
#   if they are getting 'Warmer' or 'Colder'
#
# A user is getting 'Warmer' if the guess they just made has less of a difference than the previous guess.
# A user is getting 'Colder' if the guess they just made has a greater difference than the previous guess.
# On the first guess, simply inform the user if they are incorrect or correct.
#
# The user should have 10 tries to guess the number.
#
# HINT: You will not only need to keep track of the user's current guess, but also the last guess they made.
#   BE SURE TO UPDATE THE PREVIOUS GUESS TO THE NEW ONE AT SOME POINT IN THE LOOP, probably after you've determined
#   and informed the user if they are warmer or colder.
#
# WRITE CODE BELOW #
from random import randint

print("The secret number is somewhere between 0 and 100. You have 10 guesses.")

user_input = int(input('Make a guess: '))

random = randint(0,100)

count = 0
 
while user_input is not random and count < 9:
    count = count + 1

    how_close_to_answer = random - user_input

    if 5 < how_close_to_answer.__abs__() <20:
        user_input = int(input(f'Warm. Remaining guesses {10 - count}: '))

    elif how_close_to_answer.__abs__() >= 20:
        user_input = int(input(f'Cold. Remaining guesses {10 - count}:  '))

    else:
        user_input = int(input(f'Hot. Remaining guesses {10 - count}: '))


if user_input==random:
    print('You Win!')
    print(f"It took you {count + 1} guesses to get this correct.")
    

else:
   print('You Lose! The number was', random) 


# ---------- # Part 2 # ---------- #
print('\n' + ('--- Part 2 ---'.center(25)) + '\n')
# Calculate the Hamming Distance between two DNA strands.
#
# Your body is made up of cells that contain DNA. Those cells regularly wear out and need replacing, which they
#   achieve by dividing into daughter cells. In fact, the average human body experiences about 10 quadrillion
#   cell divisions in a lifetime!
#
# When cells divide, their DNA replicates too. Sometimes during this process mistakes happen and single pieces of
#   DNA get encoded with the incorrect information. If we compare two strands of DNA and count the differences
#   between them we can see how many mistakes occurred. This is known as the "Hamming Distance".
#
# We read DNA using the letters C,A,G and T. Two strands might look like this:
#
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# ^ ^ ^  ^ ^    ^^
#
# They have 7 differences, and therefore the Hamming Distance is 7.
#
# The Hamming Distance is useful for lots of things in science, not just biology, so it's a nice phrase to
#   be familiar with :)
#
# Instructions
#   1. Prompt input from the user in the form of a DNA strand (as a String) and save it to a variable.
#       Do this twice.
#
#   2. Define a function called hamming() which accepts two parameters:
#       dna_strand1 | string | The first dna strand.
#       dna_strand1 | string | The second dna strand.
#
#       a. Using a loop inside the function, compare the two DNA strands to calculate the hamming distance.
#       b. Return the distance and print it out to the user.
#
#   HINT: It may be helpful to keep track of the distance using a variable. Think about what value it should have at
#       the beginning.
#
# WRITE CODE BELOW #

def hammingD(str1, str2):
    i = 0
    count = 0
 
    while(len(str1) == len(str2)):
        if(str1[i] != str2[i]):
            count += 1
        i += 1
    return count
 
# input
str1 = input("Enter the string>> ")
str2 = input("Enter the other string>> ")

#variable
distance=hammingD(str1, str2)
# function call
print("They have",distance, "differences, and therefore the Hamming Distance is",distance ,".")