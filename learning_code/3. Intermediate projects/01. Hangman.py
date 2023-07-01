#create list with words that will be chosen randomly
import os
import random


words = ("one", "tree", "sample", "diverse", "alphabet", "different", "element")
rnd_word = random.choice(words)
print(f"Pssst! Chosen word is {rnd_word}.")

#only "_" is displayed, number of _ depends on the chosen word
display = []
for letter in range(len(rnd_word)):
    display += "_"
print(display)

#guess the letter and check if its the right one, update display if yes
game_over = False
life = 3
while not game_over:
    correct_guess = 0
    position = 0
    guess = input("Guess the letter.")
    for letter in rnd_word:
        position += 1
        if letter == guess:
            correct_guess += 1
            display[position-1] = guess
    if correct_guess == 0:
        life -= 1
        print(f"Wrong guess. Life remaining: {life}.")
    print(display)
    if life == 0:
        print("G A M E  O V E R !")
        game_over = True
    if "_" not in display:
        game_over = True
        print("Y O U  W O N !")


