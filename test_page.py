from core.hangman_engine import HangManEngine
# Function section
def intro():
    print("Welcome to the Hangman Game")
    print("This game will give you a random word")
    print("and play the game of hangman with you")
    print("would you like to play?")
    
def start(guideMessage):
    play = ""
    while (play.lower() != "yes") and (play.lower() != "no"): 
        play = input("Enter yes or no: ")
        if (play.lower() != "yes") and (play.lower() != "no"):
            ErrorMessage("Answer must be yes or no!")
    if (play.lower() == "no"):
        return False 
    else:
        return True
            
def mask_guess(game):
    correct_guesses = ["_"] * len(game.word)

    for i, guess in enumerate(game.guess_list, start = 0):
        for j, letter in enumerate(game.word, start = 0):
            if guess == game.word[j]:
                correct_guesses[j] = guess
    print(correct_guesses)

def makeGuess():
    guess = input("Please guess a letter: ")
    return guess

def checkGuess(list, guess):
    return guess in list

def ErrorMessage(err):
    print(err)

def main():
    go = start(intro())
    while (go == True):
        game = HangManEngine()
        done = "playing"
        catch = True
        while (done == "playing"):
            catch = game.guess(makeGuess())
            if catch == True:
                done = game.update_game()
                print("Score is: ", game.score, "% right ")
                mask_guess(game)
            elif catch == "letter":
                ErrorMessage("Guess must be a letter or hypothen")
            elif catch == "length":
                print("Length of guess must be one letter!")
            else: 
                ErrorMessage("Guess must not have already been made!")
        if done == "won":
            print("You won!")
            print("The word was:", game.word)

        else:
            print("You lost!")
            print("The word was:", game.word)
        
        go = game.start_new_game(start(print("Would you like to play again?")))
    
if __name__ == "__main__":
    main()