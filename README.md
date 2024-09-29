<h1 align="center">Task No. 1: Hangman Game</h1>

This project implements a **text-based Hangman game** as part of a coding task. The game randomly selects a word from a predefined list, and the player must guess one letter at a time to uncover the word. The game provides a limited number of attempts (lives), and after each incorrect guess, the player's remaining lives decrease. If the player runs out of lives, they lose, and the game reveals the word. Otherwise, if the player successfully guesses all the letters in the word, they win.

### Features

- Random word selection.
- Player guesses one letter at a time.
- Displays the current status of the word with blanks (`_`) for unguessed letters.
- Limits the number of incorrect guesses (starting with 6 lives).
- Visual representation of the hangman stages as the player makes incorrect guesses.
- End game conditions: win (when all letters are guessed) or lose (when lives reach zero).

### Files

- `hungman.py`: Contains the main game logic, handles the word guessing, checks for incorrect guesses, and manages the game loop.
- `stages.py`: Defines the stages of the Hangman figure, progressively revealing more parts of the figure with each incorrect guess.

### How to Run

1. Ensure you have Python installed on your system.
2. Clone the repository.
3. Run the `hungman.py` script in a terminal or command prompt.

```
python hungman.py
```
### Gameplay

![image](https://github.com/user-attachments/assets/0e3bf019-bd87-4714-b182-affbb9780ae1)                       ![Screenshot 2024-09-29 165454](https://github.com/user-attachments/assets/c719554a-21fb-45a4-9b95-3f56a603d64f)

