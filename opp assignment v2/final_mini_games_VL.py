# This will import required Python modules
import random   # Used for randomly selecting words, numbers, and riddles
import time     # Used for adding delays (like in the memory game)
from abc import ABC, abstractmethod   # Used for creating abstract base class

# Main template class that all games will build upon
class MiniGame(ABC):
    # Constructor - runs when creating a new game
    def __init__(self, name):
        self._name = name              # Store the game's name
        self._completed = False        # Track if player has won (starts as False)
        self._reward = None            # What player gets for winning (set by each game)

    # This is an abstract method that must be implemented by subclasses
    @abstractmethod
    def play(self):
        pass  # Placeholder for the play method, to be defined in subclasses

    # Getter for the completed status
    @property
    def completed(self):
        return self._completed         # Returns True if game is won, False if not

    # Getter for the reward
    @property
    def reward(self):
        return self._reward            # Returns whatever reward this game gives

# Game 1: Word Scramble Game
class WordScramble(MiniGame):
    # Constructor - sets up the game
    def __init__(self):
        super().__init__("Word Scramble")  # Call the parent class constructor with the game name
        self.word_list = ["detective", "mystery", "evidence", "suspect", "witness"]  # List of words to scramble
        self._reward = "A small key"  # Reward for winning the game

    # Helper method to scramble a word
    def _scramble_word(self, word):
        word_letters = list(word)         # Convert the word into a list of its letters
        random.shuffle(word_letters)      # Randomly shuffle the letters in the list
        return ''.join(word_letters)      # Join the shuffled letters back into a string

    # Main game method - this is where the actual game happens
    def play(self):
        print("\n=== Welcome to the Word Scramble Challenge! ===")  # Display the game title
        print("Unscramble the word to gain a valuable clue!")  # Instructions for the player
        
        original_word = random.choice(self.word_list)  # Pick a random word from the list
        scrambled_word = self._scramble_word(original_word)  # Scramble the chosen word
        
        attempts_left = 3  # Player has 3 attempts to guess the word
        hint = f"The word is related to a crime scene."  # Provide a hint for the player
        print(f"Hint: {hint}")  # Show the hint to the player
        
        while attempts_left > 0:  # Loop until the player runs out of attempts
            print(f"\nScrambled word: {scrambled_word}")  # Show the scrambled word
            print(f"Attempts remaining: {attempts_left}")  # Show how many attempts are left
            player_guess = input("Your guess: ").lower()  # Get the player's guess and convert it to lowercase
            
            if player_guess == original_word:  # Check if the guess is correct
                self._completed = True  # Mark the game as completed
                print(f"\nCongratulations! You found {self._reward}!")  # Notify the player of their win
                return True  # Return True to indicate a win
            else:
                attempts_left -= 1  # Reduce the number of attempts left by 1
                print("Incorrect! Try again.")  # Notify the player that their guess was incorrect
        
        print(f"\nGame Over! The word was: {original_word}")  # Notify the player that the game is over
        return False  # Return False to indicate a loss

# Game 2: Memory Game
class MemoryGame(MiniGame):
    # Constructor - sets up the game
    def __init__(self):
        super().__init__("Memory Game")  # Call the parent constructor with the game name
        self.sequence_length = 4           # How many numbers the player needs to remember
        self._reward = "A mysterious note"  # Reward for winning the game

    # Main game method
    def play(self):
        print("\n=== Welcome to the Memory Challenge! ===")  # Display the game title
        print("Remember the sequence of numbers!")  # Instructions for the player
        
        # Create a random sequence of numbers for the player to memorize
        number_sequence = [random.randint(1, 9) for _ in range(self.sequence_length)]  
        
        print("\nMemorize this sequence:")  # Prompt the player to memorize the sequence
        print(' '.join(map(str, number_sequence)))  # Show the sequence as a space-separated string
        time.sleep(3)  # Pause for 3 seconds to allow the player to memorize
        print("\n" * 50)  # Print 50 blank lines to "clear" the screen
        
        start_time = time.time()  # Start the timer to track how long it takes the player to respond
        player_input = input("Enter the sequence (space-separated numbers): ")  # Get the player's input
        elapsed_time = time.time() - start_time  # Calculate the time taken to respond
        
        player_numbers = player_input.split()  # Split the input into a list of strings
        
        if len(player_numbers) != len(number_sequence):  # Check if the length of input matches the sequence
            print("Incorrect length! Please try again.")  # Notify the player of incorrect length
            return False  # Return False to indicate a loss
        
        try:
            player_numbers = [int(num) for num in player_numbers]  # Convert input strings to integers
            if player_numbers == number_sequence:  # Check if the player's sequence matches the original
                self._completed = True  # Mark the game as completed
                print(f"\nWell done! You found {self._reward}!")  # Notify the player of their win
                print(f"You took {elapsed_time:.2f} seconds to answer.")  # Show the time taken to answer
                return True  # Return True to indicate a win
            else:
                print("\nIncorrect sequence! Better luck next time.")  # Notify the player of an incorrect sequence
                return False  # Return False to indicate a loss
        except ValueError:  # Handle case where input cannot be converted to integers
            print("\nInvalid input! Please enter numbers only.")  # Notify the player of invalid input
            return False  # Return False to indicate a loss

# Game 3: Riddle Game
class RiddleGame(MiniGame):
    # Constructor - sets up the game
    def __init__(self):
        super().__init__("Riddle Challenge")  # Call the parent constructor with the game name
        self.riddle_list = [  # List of riddles with their answers
            ("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?", "echo"),
            ("The more you take, the more you leave behind. What am I?", "footsteps"),
            ("What has keys, but no locks; space, but no room; and you can enter, but not go in?", "keyboard")
        ]
        self._reward = "A hidden map"  # Reward for winning the game

    # Main game method
    def play(self):
        print("\n=== Welcome to the Riddle Challenge! ===")  # Display the game title
        print("Solve the riddle to gain a valuable clue!")  # Instructions for the player
        
        riddle, answer = random.choice(self.riddle_list)  # Pick a random riddle-answer pair from the list
        attempts_left = 3  # Player has 3 attempts to answer
        hint = "Think about something that can reflect sound."  # Provide a hint for the player
        
        print(f"Hint: {hint}")  # Show the hint to the player
        
        while attempts_left > 0:  # Loop until the player runs out of attempts
            print(f"\nRiddle: {riddle}")  # Show the riddle
            print(f"Attempts remaining: {attempts_left}")  # Show how many attempts are left
            player_answer = input("Your answer: ").lower()  # Get the player's answer and convert it to lowercase
            
            if player_answer == answer:  # Check if the answer is correct
                self._completed = True  # Mark the game as completed
                print(f"\nFantastic! You found {self._reward}!")  # Notify the player of their win
                return True  # Return True to indicate a win
            else:
                attempts_left -= 1  # Reduce the number of attempts left by 1
                print("Incorrect! Give it another shot.")  # Notify the player that their answer was incorrect
        
        print(f"\nGame Over! The answer was: {answer}")  # Notify the player that the game is over
        return False  # Return False to indicate a loss
