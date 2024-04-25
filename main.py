import random
from hangman_words import word_list
from hangman_art import stages, logo
import os



display = []
chosen_word = random.choice(word_list)
guess_length = len(chosen_word)
end_of_game = False
player_lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

for character in range(guess_length):
    display += "_"
# print(display)

print(logo)

while not end_of_game:
    letter_guess = input("\nGuess a letter: ").lower()

    os.system('cls||clear')

    if letter_guess in display:
        print(f"You've already guessed the letter '{letter_guess}'!")

    for pos in range(guess_length):
        letter = chosen_word[pos]
        if letter_guess == letter:
            display[pos] = letter

    if letter_guess not in chosen_word:
        print(f"The word does not contain the letter '{letter_guess}'! You lose a life.")
        player_lives -= 1
        if player_lives == 0:
            end_of_game = True
            print(f"\nDefeat! The word was '{chosen_word}'!\n")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}\n")

    if "_" not in display:
        end_of_game = True
        print("\nVictory!\n")
        print(f"LIVES LEFT = {player_lives}")
    
    print(stages[player_lives])