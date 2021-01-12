#final version

import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = word_list[random.randint(0,len(word_list)-1)]
word_length = len(chosen_word)
lives = 6

logo = hangman_art.logo
print(logo)
print(f'The solution is {chosen_word}.\n')

# Create blanks
display = []
display = ["_" for _ in range(word_length)]

while "_" in display and lives > 0:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You have already guessed {guess}. Please try again")

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f'The chosen letter {guess} is not in the word. You lost a life. Try Again!')
    lives = lives - 1
    print(hangman_art.stages[lives]) 
  else:
    print(hangman_art.stages[lives])

  print(" ".join(display))
  print('\n')

if lives == 0:
  print("You Lost the game.")

else:
  print("You WIN")