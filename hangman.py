import random

# game data
word_list = ['python', 'java', 'kotlin', 'javascript']          # words list
chosen_word = random.choice(word_list)                          # choosing random word
number_of_lives = 8                                             # number of lives, that user have
correct_shot = ''                                               # variable needed for guessing the whole word early
word_set = set(chosen_word)                                     # set containing the letters used in chosen word
user_letters = set()                                            # set for collecting letters used by user
# masking the word
length = len(chosen_word)
masked = '-' * length
letters_list = list(chosen_word)
allowed_characters = 'abcdefghijklmnopqrstuvwxyz'               # chars that may occur in guessed word

# actual game

print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit:')
if input() == 'play':
    while number_of_lives > 0:
        print()
        print(masked)
        user_input = input("Input a letter: ")
        if user_input == chosen_word:                               # checking if user guessed the whole word
            correct_shot = user_input                               # assign correct value to external variable
            break
        if user_input in user_letters:                              # check if user's input is correct
            print('You already typed this letter')
        elif len(user_input) != 1:
            print('You should input a single letter')
        elif user_input not in allowed_characters:
            print('It is not an ASCII lowercase letter')
        else:
            if user_input in word_set:
                letter_position = []                                # temporary list for letter's positions inside word
                for i in range(len(letters_list)):
                    if letters_list[i] == user_input:
                        position = i
                        masked = masked[:position] + user_input + masked[position + 1:]  # inserting those letters
            else:                                                   # action if letter is not inside the word
                print("No such letter in the word")
                number_of_lives -= 1
        if user_input in allowed_characters:                        # add the latest user's input to used letters set
            user_letters.add(user_input)
        if masked == chosen_word:
            break

    # ending the game
    if masked == chosen_word or correct_shot == chosen_word:
        print()
        print(chosen_word)
    if masked == chosen_word or correct_shot == chosen_word:        # winning options
        print('You guessed the word!')
        print('You survived!')
    if number_of_lives == 0:                                        # loosing options
        print('You are hanged!')
