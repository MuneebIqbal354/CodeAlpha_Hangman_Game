import random
import stages
import words_list

generate = random.choice(words_list.different_words)
# print (generate)

blanks = []
lives = 6
flag = True
for i in range (len(generate)):
    blanks += '_'
print (blanks)

while flag:
    guess_letter = input("Guess a letter: ")
    for x in range (len(generate)): # x = 0, 1, 2, 3, 4
        if generate[x] == guess_letter:
            blanks[x] = guess_letter
    print(blanks)
    if guess_letter not in generate:
        lives -= 1
        if lives == 0:
            print ("You Lose!!!",":((")
            print (f'The word is "{generate}"')
            flag = False
    if '_' not in blanks:
        print ("You Win",":)")
        flag = False
    print(stages.stages_list[lives])