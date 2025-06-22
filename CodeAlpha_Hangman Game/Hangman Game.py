import random
from colorama import Fore, Style, init

init(autoreset=True)

# List of spooky words
words = ["ghost", "haunt", "silent", "zombie", "umbrella", "nightmare", "shadow", "widow",  "darkness",  "widow", "blackout"]

# Rabdomly choose one
word_to_guess = random.choice(words)
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

# Function to display word with underscores
hidden_word = ["_"] * len(word_to_guess)

# Intro
print(Fore.MAGENTA + Style.BRIGHT + "\n💀 Welcome to the Haunted Word Guess 💀")
print(Fore.CYAN +" " + "...Type a letter... if you dare 👉😈")

while wrong_attempts < max_attempts and "_" in hidden_word:
    print(Fore.YELLOW + f"\nWord: {' '.join(hidden_word)}")
    print(Style.BRIGHT + f"Wrong attempts left: {max_attempts - wrong_attempts}")
    guess = input(Fore.LIGHTWHITE_EX + "\n🔍 Guess a letter: ").lower()
    
    
    # input validation
    if not guess.isalpha() or len(guess) != 1:
        print(Fore.RED + "⛔ Only single alphabetic characters allowed!")
        continue

    if guess in guessed_letters:
        print(Fore.YELLOW + "😬 You've already guessed that letter.")

    # Check if the guessed letter is in the word
    
    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                hidden_word[i] = guess
        print(Fore.GREEN + "✅ Good guess!")
    else:
        guessed_letters.append(guess)
        wrong_attempts += 1
        print(Fore.RED + f"❌ Wrong! You feel the cold breath of the undead... ({wrong_attempts}/{max_attempts})")
    

# Game over condition
if "_" not in hidden_word:
    print(Fore.GREEN + f"\nBINGO!!🎉 You survived the horror and guessed it right!")
    print(Fore.WHITE + "The Word was: " + "#### " + Fore.LIGHTGREEN_EX + word_to_guess.upper() + Fore.WHITE + " ####")

else:
    print(Fore.RED + f"\n☠️ Game Over! The correct word was:" + Fore.WHITE + " " +"#### " + Fore.LIGHTGREEN_EX + word_to_guess.upper() + Fore.WHITE + " ####")
    print("👻 Better luck next time...")