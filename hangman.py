import random

words = ["python", "coding", "alpha", "developer", "program"]
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("--- Welcome to Hangman Game ---")

while attempts_left > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word.strip())
    print(f"Attempts left: {attempts_left}")

    if "_" not in display_word:
        print("Congratulations! You guessed the word correctly!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts_left -= 1
        print(f"Wrong guess! '{guess}' is not in the word.")

if attempts_left == 0:
    print(f"\nGame Over! The correct word was: {secret_word}")