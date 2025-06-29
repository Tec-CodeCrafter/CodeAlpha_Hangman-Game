## Hangman_Game

This is a spooky and Easy terminal-based word guessing game built in Python. The player must guess letters to unveil a hidden word before running out of chances.

## 🧠 What This Project Does

The goal is simple — guess the hidden haunted or Easy word, letter by letter... but you only have 6 chances before the game ends and the ghost gets you 👻. 

Key Python Concepts Used in This Project :

- Loops and conditionals
- String manipulation
- List operations
- Basic game logic
- Adding colors using the colorama library for a better terminal experience

## 💼 How It Works

The program starts by randomly selecting a word from a spooky-themed list like "ghost", "zombie", "nightmare", etc.

1. The selected word is hidden using underscores (_), and the player must guess the letters.
2. For each correct guess:
3. The hidden word updates to reveal the guessed letter in the correct position(s).
4. For each wrong guess:
5. The player loses one of their 6 chances.
6. A creepy message is shown to increase suspense.
7. The game ends when:
8. The player guesses the full word correctly (you win 🎉), or
9. The player runs out of guesses (you lose 💀).

## Features

- 🧠 Random spooky word selection
- 🎨 Colored terminal output using `colorama`
- ✅ Input validation and attempt tracking
- ☠️ Game-over and success endings with styled messages
- 🔁 Tracks wrong attempts and previous guesses
- 🔁 Allow the player to play the game again if they type "yes"

## 🧾 Example Output

💀 Welcome to the Haunted Word Guess 💀
 ...Type a letter... if you dare 👉😈

Word: _ _ _ _ _
Wrong attempts left: 6

🔍 Guess a letter: g
✅ Good guess!

Word: g _ _ _ _       
Wrong attempts left: 6

🔍 Guess a letter: o  
✅ Good guess!

Word: g _ o _ _       
Wrong attempts left: 6

🔍 Guess a letter:  


## 🔧 Requirements

- Python 3.x
- colorama  # colorama module is used to add color to your terminal (console) output

## 🛠️ How to Run

1. Make sure Python is installed on your system.
2. Clone the repository or download the code.
3. Open your terminal or command prompt and navigate to the folder:
   ```bash
   cd path/to/your/project
4. Install requirements:
   ```bash
   pip install -r requirements.txt
   
5. Run the game:
   ```bash
   python Hangman_Game.py
   

## File Structure

- `Hangman_Game.py`: Main game file
- `README.md`: Project documentation
- `requirements.txt`: Required Python packages

## Author

- Prince Kumar
- GitHub: @Tec-CodeCrafter 
- Created for CodeAlpha Internship
- 🔗 [LinkedIn](https://www.linkedin.com/in/prince-kumar-aa5a76329)
- 💻 [GitHub](https://github.com/Tec-CodeCrafter)

