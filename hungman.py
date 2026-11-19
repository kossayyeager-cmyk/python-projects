
import random as r

words = [
    "python", "computer", "keyboard", "monitor", "programming",
    "developer", "software", "hardware", "internet", "database",
    "algorithm", "function", "variable", "integer", "boolean",
    "string", "dictionary", "tuple", "module", "package",
    "elephant", "giraffe", "kangaroo", "dolphin", "penguin",
    "butterfly", "crocodile", "turtle", "leopard", "cheetah",
    "mountain", "volcano", "forest", "desert", "ocean",
    "river", "island", "waterfall", "rainbow", "thunder",
    "airplane", "helicopter", "bicycle", "motorcycle", "submarine",
    "spaceship", "train", "rocket", "vehicle", "highway",
    "chocolate", "sandwich", "hamburger", "spaghetti", "pancake",
    "pineapple", "strawberry", "watermelon", "avocado", "blueberry",
    "football", "basketball", "volleyball", "swimming", "baseball",
    "skateboard", "tennis", "badminton", "cycling", "wrestling",
    "adventure", "mystery", "treasure", "kingdom", "castle",
    "dragon", "warrior", "wizard", "monster", "vampire",
    "universe", "galaxy", "planet", "asteroid", "telescope",
    "gravity", "oxygen", "diamond", "crystal", "magnet",
    "hospital", "library", "restaurant", "airport", "museum",
    "calendar", "backpack", "umbrella", "scissors", "puzzle"
]
man={0:("o"),1:("o","|"),2:("o","/|\\")
,3:("o","/|\\","/"),4:("o","/|\\","/\\")}

def chose_word(words):
    return r.choice(words)
def displayman(attempts):
    m=man[attempts]
    for i in m:
        print(i)

def main():
    attempts = 0
    guessedletter = []
    diff={"easy":5,"hard":1,"meduim":3}
    print("*" * 20)
    print("WELCOME TO HANGMAN!")
    diffculty=(input("chose a diffculty (easy -meduim-hard)"))
    while True:
        if diffculty not in diff.keys():
         print("invalid value")
         diffculty=(input("chose a diffculty (easy -meduim-hard)"))
        else:
            break
    word = chose_word(words)

    while True:

   
        if attempts == diff[diffculty]:
            print("No more attempts left!")
            print(f"The correct word was: {word}")
            break

     
        if all(letter in guessedletter for letter in word):
            print(f"\nYou won with {attempts} attempts!")
            break

        
        print("\nWord: ", end="")
        for letter in word:
            if letter in guessedletter:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        
        print(f"Guessed letters: {guessedletter}")

        char = input("Guess a character: ").lower()

    
        if len(char) != 1 or not char.isalpha():
            print("Please enter one letter!")
            continue

        if char in guessedletter:
            print("You already guessed that letter!")
            continue

        guessedletter.append(char)

        
        if char in word:
            print("Correct guess!")
        else:
            
            print("Wrong guess!")
            displayman(attempts)
            attempts += 1
            print(f"attempts remainig are:{diff[diffculty]-attempts}")


if __name__ == '__main__':
    main()
