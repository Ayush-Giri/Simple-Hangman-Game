import random
from art import stages
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in chosen_word:
    display.append("_")

end_of_game = False
number_of_lives_left = 6
ascii_art_indexing = -2

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    index_values = 0

    for letter in chosen_word:
        if chosen_word[index_values] == guess:
            display[index_values] = guess
            index_values += 1
        else:
            index_values += 1
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

    elif guess not in chosen_word:
        number_of_lives_left -= 1
        print(stages[ascii_art_indexing])
        ascii_art_indexing -= 1
        if number_of_lives_left == 0:
            print("You loose")
            end_of_game = True
