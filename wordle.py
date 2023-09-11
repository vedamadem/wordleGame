import random

print ('''\n Wordle is a word guessing game.
You have 5 attempts.
(✔) means the letter in in the word ad in the correct position.
(X) means the letter is in the word but not in the correct position.
(_) means the letter is not there in the word itself. Best of Luck. ''')

words = ["this", "five", "help", "lake", "pink", "cats","veda","crab", "izzy", "bean", "home", "duck", "luck"]




def check_word(guess, hidden_word):
    if hidden_word == guess:
        print("Congrats!! You did it.")
        return True
    else:
        result = ""
        for i, j in zip(guess, hidden_word):
            if i == j:
                result = result + "(✔)"
            elif i in hidden_word:
                result = result + "(X)"
            else:
                result = result + "(_)"
        print(result)
        return False

def main_loop():
    hidden_word = random.choice(words)
    attempt = 5
    while attempt > 0:
        guess = input("Enter a four letter word: ")
        if check_word(guess, hidden_word):
            break
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempts left.")
main_loop()
