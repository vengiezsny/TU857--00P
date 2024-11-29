# Import the required pythn module
import random

from abc import ABC, abstractmethod

from tenacity import retry_unless_exception_type


class GamePR(ABC): # abstract class for puzzles and riddles
    def __init__(self, name, reward):
        self._name = name # store the game's name
        self._reward = reward # each game grants the user a reward

    @abstractmethod
    def play(self): # implemented in all games
        pass

    @property
    def reward(self): # getter for the reward
        return self._reward

# Riddles
class Riddles(GamePR):
# A class for riddles and inherits from GamePR. The user will be
# given a riddle and has the option to get a hint if needed.

    def __init__(self):
        list_riddles = [
            {
                "question": "I’m tall when I’m young, and I’m short when I’m old.",
                "answer": "candle",
                "hint": "It burns."
            },
            {
                "question": "I follow you all the time and copy your every move, but you can’t touch me or catch me.",
                "answer": "shadow",
                "hint": "I appear in the light, but disappear in the dark."
            },
            {
                "question": "If you’ve got me, you want to share me; if you share me, you haven’t kept me.",
                "answer": "secret",
                "hint": "Something you tell, but wish others wouldn't."
            }

        ]

        super().__init__("Riddles", "diary.")
        self.__riddles = list_riddles # contains all the riddles

    def play(self): # main riddle game logic
        print(f"\nYou will now play the game of {self._name}.")

        remaining_riddles = len(self.__riddles) # number of riddles left to answer
        completed_riddles = 0 # tracks the riddles solved by the user

        # loop through the riddles
        for riddle in self.__riddles:
            print(f"\n{remaining_riddles} riddles left to acquire a clue.")
            print(f"{riddle['question']}")

            tries = 3 # user has 3 tries to answer the riddle

            while tries > 0:
                print(f"You have {tries} tries left.")
                choice = input("Enter your answer (type 'hint' for a hint): ").strip().lower() # .strip() to remove white space
                                                                                               # .lower() to return the string in all lower case

                if choice == "hint":
                    print(f"{riddle['hint']}")
                elif choice == riddle["answer"]:
                    print("You have solved the riddle.")
                    completed_riddles = completed_riddles + 1 # increment each time a riddle is completed
                    remaining_riddles = remaining_riddles - 1 # decrement each time a riddle is completed
                    break
                else:
                    print("Incorrect.")
                    tries = tries - 1

            print(f"You have no more tries. The answer was {riddle['answer']}.")

        # after riddles are completed
        if completed_riddles == len(self.__riddles):
            print("\nCongratulations. You have completed all the riddles and you have been granted your reward.")
            return self._reward
        else:
            print("\nYou failed to complete the riddles.")
            return None # no reward is granted if the riddles are not solved

class Puzzles(GamePR):
    # A class for puzzles containing a hangman game and a number sequence puzzle

    def __init__(self):
        super().__init__("Puzzles", "a box of letters")

    def hangmanGame(self): # hangman game logic
        word_list = ["detective", "mystery", "necklace", "diamond", "secrets", "evidence"]
        word = random.choice(word_list)
        display_word = ['_'] * len(word) # diplays the word to be guessed with blank spaces
        guessed_letters = []
        bodyparts = 6 # represents the 6 body parts of the "man"; head, body, arm, arm, leg, leg

        print("\nYou will now play Hangman.")

        while bodyparts > 0 and '_' in display_word: # while loop runs as long as there are bodyparts and there are
                                                     # still blank spaces
            print(" ".join(display_word)) # print current state of the word to guess
            guess = input(f"Guess a letter, you have {bodyparts} body parts left.").lower()

            if guess in word: # check if guessed letter is in the word
                # if the letter is in the word, loop through the word to update the display_word with the guessed letter
                for i in range(len(word)):
                    if word[i] == guess:
                        display_word[i] = guess
                print("Correct letter guessed.")
            elif guess in guessed_letters:
                print("Letter already guessed.")
            else:
                bodyparts = bodyparts - 1
                print(f"This letter is not in the word. {bodyparts} body parts left.")

            guessed_letters.append(guess) # guessed letter is added to the list of guessed letters

        if '_' not in display_word:  # if there are no blanks in display_word, the word is guessed
            print(f"Congratulations! You've guessed the word: {''.join(display_word)}")
            return True  # return True, as the word has been guessed
        else:
            print(f"Game over! The correct word was: {word}")
            return False  # return False, as the word was not guessed

    def sequencePuzzle(self): # sequence game logic
        sequence = [2, 4, 8, 16, 32]

        print("\nYou will now play the Sequence Puzzle.")
        print("Given the sequence 2, 4, 8, 16, 32, what is the next number?")

        answer = 64 # 32x2 = 64

        attempts = 3 # user has 3 attempts to answer
        while attempts > 0: # loop as long as there is attempts
            user_answer = input(f"You have {attempts} left, enter your answer: ").strip

            if user_answer == answer: # check if the users answer is the answer
                print("Correct. You solved the puzzle and will now be granted an award.")
                return True # user has solved the puzzle
            else:
                attempts = attempts - 1
                print(f"Incorrect. You have {attempts} left.")

        print(f"You failed. The correct answer was {answer}")
        return False # user has failed to solve the puzzle

    def play(self):
        # Play both the sequence game and the hangman game
        print(f"\nYou will now play the game of {self._name}")

        # hangman first
        hangman_result = self.hangmanGame()
        if not hangman_result:
            print("You did not complete Hangman.")
            return None

        # sequence game second
        sequence_result = self.sequencePuzzle()
        if not sequence_result:
            print("You did not complete the Sequence Puzzle")

        # both games completed
        print("\nCongratulations, you have completes the riddles and the puzzles. You have been granted your rewards.")
        return self._reward