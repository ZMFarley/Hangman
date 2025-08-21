import random
from nltk.corpus import words
class HangManEngine:
    MAX_WRONG_GUESSES = 6
    #Initialization and String Section 
    def __init__(self):
        self._rnd_wrd_gn = random.Random()
        self._word_list = self._load_word_list()
        self._word = self._pick_word()
        self._guess_list = []
        self._current_guess = ""
        self._num_guesses_left = 0
        self._num_wrong_guesses = 0
        self._num_right_guesses = 0
        self._num_games_won = 0
        self._num_games_lost = 0
        self._score = 0

    def __str__(self):
        return (f"{self._word}, {self._guess_list}, {self._current_guess}, {self._num_guesses_left}, {self._num_wrong_guesses}," 
               f"{self._num_right_guesses}, {self._num_games_won}, {self._num_games_lost}, {self._score}, {self._rnd_wrd_gn}")
    
    # Getter Section
    @property
    def word(self):
        return self._word
    
    @property
    def guess_list(self):
        return self._guess_list
    
    @property
    def num_guesses_left(self):
        return self._num_guesses_left
    
    @property
    def current_guess(self):
          return self._currrent_guess
    
    @property
    def num_wrong_guesses(self):
        return self._num_wrong_guesses
    
    @property
    def num_right_guesses(self):
        return self._num_right_guesses
    
    @property
    def num_games_won(self):
         return self._num_games_won
         
    @property
    def num_games_lost(self):
         return self._num_games_lost
    
    @property
    def score(self):
         return self._score

    # Game Logic Section 
    def _load_word_list(self):
        return [word.lower() for word in words.words() if 5 <= len(word) <= 10]
    
    def _pick_word(self):
        return self._rnd_wrd_gn.choice(self._word_list)
    
    def __verify_guess(self, pick):
        if not pick.isalpha():
            return "letter"
        elif len(pick) != 1:
            return "length"
        elif pick in self._guess_list:
            return "already"
    
    def guess(self,pick):
        # Check current guess (pick) and add it to the guess list
        err = self.__verify_guess(pick)
        if not err:
            self._current_guess = pick.lower()
            self._guess_list.append(self._current_guess)
        else:
            return err
        
        # Update the guess system: guess (right/wrong) & overall score
        if self._current_guess in self._word:
            self.__update_guess_result(True)
            self.__update_score()
        else:
            self.__update_guess_result(False)
            self.__update_score()
        
        return True 

    def update_game(self):  
         # Update the game system (+game won/game lost)
        if self._num_wrong_guesses == self.MAX_WRONG_GUESSES:
             self.__update_game_result(False)
             return "lost"
        
        elif list(self._word) == self._guess_list:
            self.__update_game_result(True)

            return "won"
        else:
            return "playing"
            
    def start_new_game(self, flag):
        # Reset the game for new round
        if flag: 
              self._word = self._pick_word()
              self._guess_list.clear()
              self._currrent_guess = ""
              self._num_gusses_left = 0
              self._num_wrong_guesses = 0
              self._num_right_guesses = 0
              self._num_games_won = 0
              self._num_games_lost = 0
              self._score = 0
              return True
        
        # Otherwise end it 
        else:
            return False

    def __update_guess_result(self, flag):
        if flag:
            self._num_right_guesses += 1
        else:
            self._num_wrong_guesses += 1

    def __update_game_result(self, flag):
        if flag:
            self._num_games_won += 1
        else:
            self._num_games_lost += 1

    def __update_score(self):
        self._score = self.num_right_guesses/len(self._word)