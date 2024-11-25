# Authors (Members):
# 1. Vengie Legaspi (student ID: C20366171).
# 2. John Hoang (student ID: C22455366).
# 3. Jace Janczak (student ID: C23493156 ).
# 4. Cristian Brillantes (student ID: C23482336).
# Date: November 25, 2024.
#
# Game Expansion Explanation:
#
# Welcome to the thrilling expansion of our mystery game, "The Detective's Enigma!" 
# The Code Wizards group has conjured up a series of exhilarating new features that 
# will elevate your detective experience to new heights. 
#
# **Exciting Mini-Games:**
# - **Word Scramble:** Test your linguistic skills by unscrambling words related to 
#   the mystery. Each correct guess brings you closer to uncovering the truth!
# - **Memory Game:** Sharpen your memory as you memorize sequences of numbers that 
#   hold vital clues. Can you recall them under pressure?
# - **Riddle Challenge:** Engage your mind with thought-provoking riddles that will 
#   challenge your critical thinking and problem-solving abilities. Solve them to 
#   unlock essential information!
#
#
# **Educational Puzzles:** Engage your mind with puzzles inspired by real-world 
# detective work. These challenges are designed to sharpen your critical thinking 
# skills while you unravel the mysteries that lie ahead.
#
# **File Structure:**
# - `game.py`: The heart of the game where your adventure begins.
# - `puzzles.py`: A treasure trove of educational puzzles to challenge your intellect.
#
# **How to Play:**
# - To embark on your journey in "The Detective's Enigma," simply run the 
#   `main.py` file. 
# - Ensure that the `crime_scene.py`, `characters.py`, and `final_mini_games.py` ,'logger.py','main.py','game.py'
#   modules are in the same directory to unlock the full potential of your 
#   detective adventure.
#
# **Get Ready for an Adventure!**
# Prepare yourself for an immersive experience filled with twists, turns, 
# and brain-teasing challenges. Are you ready to don the detective's hat 
# and solve the case? The truth awaits!
#
# Important Note:
# Please keep this header unaltered in all submitted files.
################################################################################


from characters import Suspect, Witness, NPC  # Import character classes for the game: Suspect, Witness, and NPC (Non-Playable Characters)
from logger import Loggable  # Import the Loggable class for logging game events and errors
from crime_scene import CrimeScene  # Import the CrimeScene class to manage the crime scene and clues
from final_mini_games_VL import WordScramble, MemoryGame, RiddleGame  # Import mini-game classes for additional gameplay features

class Game:
    def __init__(self):
        # Initialize loggers for game and error logging
        self.__logger = Loggable()
        self.__error_logger = Loggable()
        self.__running = True  # Flag to control the game loop
        self.__game_started = False  # Flag to check if the game has started
        self.__characters_interacted = False  # Track if characters have been interacted with
        self.__npcs_interacted = False  # Track if NPCs have been interacted with

        # Initialize the crime scene and characters
        self.__crime_scene = CrimeScene("Mansion's Drawing Room")
        self.__suspect = Suspect("Mr. Smith", "I was in the library all evening.", "Confirmed by the butler.")
        self.__witness = Witness("Ms. Parker", "I saw someone near the window at the time of the incident.",
                               "Suspicious figure in dark clothing.")
        self.__doors = ["Front door", "Library door", "Kitchen door"]  # List of doors to choose from
        self.__doors_checker = [False, False, False]  # Track which doors have been checked
        self.__clues = []  # List to store clues found during the game
        
        # Initialize mini-games available in the game
        self.__mini_games = [
            WordScramble(),
            MemoryGame(),
            RiddleGame()
        ]
        self.__games_completed = []  # Track completed mini-games

    @property
    def log(self):
        return self.__logger  # Return the logger for general game logs

    @property
    def error_log(self):
        return self.__error_logger  # Return the logger for error logs

    def run(self):
        self.__logger.log("Game started")  # Log that the game has started
        print("Welcome to 'The Poirot Mystery'")
        print("You are about to embark on a thrilling adventure as a detective.")
        print("Your expertise is needed to solve a complex case and unveil the truth.")

        while self.__running:  # Main game loop
            try:
                self.update()  # Update game state
            except ValueError as ve:
                self.__error_logger.log(f"Error found:\n {ve}.")  # Log value errors
            except Exception as e:
                self.__error_logger.log(f"Unexpected error from run():\n{str(e)}.")  # Log unexpected errors
                print("Unexpected caught error during running of the Game. We continue playing...")
            else:
                self.__logger.log("Successfully updating")  # Log successful updates
            finally:
                self.__logger.log("---")  # Log end of update cycle

    def update(self):
        self.__logger.log("I'm updating")  # Log that the update method is called

        if not self.__game_started:  # Check if the game has started
            player_input = input("Press 'q' to quit or 's' to start: ")  # Get player input
            if player_input.lower() == "q":
                self.__running = False  # Stop the game loop
                log_file = input("Please provide a file name for the logs: \n")  # Get log file name
                self.__logger.save_logs_to_file(log_file)  # Save logs to file
            elif player_input.lower() == "s":
                self.__game_started = True  # Set game started flag
                self.start_game()  # Start the game
            else:
                raise ValueError("Incorrect user entry.")  # Raise error for invalid input
        else:
            # Prompt for game actions
            player_input = input(
                "Press 'q' to quit, 'c' to continue, 'i' to interact, "
                "'e' to examine clues, 'r' to review clues, 'm' to play mini-games, or 'd' to choose a door: ")

            self.__logger.log(f"Player input is {player_input}.")  # Log player input

            if player_input.lower() == "q":
                log_file = input("Please provide a file name for the logs: \n")  # Get log file name
                self.__logger.save_logs_to_file(log_file)  # Save logs to file
                self.__running = False  # Stop the game loop
            elif player_input.lower() == "c":
                self.continue_game()  # Continue the game
            elif player_input.lower() == "i":
                try:
                    self.interact_with_characters()  # Interact with characters
                except ValueError as ve:
                    self.__error_logger.log(f"Error found:\n {ve}.")  # Log value errors
                    print("Invalid character option.")
                except Exception as e:
                    self.__error_logger.log(f"Unexpected exception found for player input to interact with characters:\n{e}")
                    print("Unexpected error found for player input to interact with character. We continue playing...")
            elif player_input.lower() == "e":
                self.examine_clues()  # Examine clues
            elif player_input.lower() == "d":
                try:
                    self.choose_door()  # Choose a door to investigate
                except ValueError as ve:
                    print("This door choice does not exist.")  # Handle invalid door choice
                    self.__error_logger.log(f"Error found:\n{ve}")
                except Exception as e:
                    self.__error_logger.log(f"Unexpected error found for player input:\n{e}")
                    print("Unexpected error from player input. We continue playing...")
            elif player_input.lower() == "r":
                clues = self.__crime_scene.review_clues()  # Review clues
                if clues:
                    print(clues)  # Print found clues
                else:
                    print("You have not found any clues yet.")  # No clues found message
            elif player_input.lower() == "m":
                self.play_mini_games()  # Play mini-games
            else:
                raise ValueError("Incorrect user game option choice made.")  # Raise error for invalid option

    def start_game(self):
        player_name = input("Enter your detective's name: ")  # Get player's name
        print(f"Welcome, Detective {player_name}!")  # Welcome message
        print("You find yourself in the opulent drawing room of a grand mansion.")
        print("As the famous detective, you're here to solve the mysterious case of...")
        print("'The Missing Diamond Necklace'.")
        print("Put your detective skills to the test and unveil the truth!")

    def continue_game(self):
        print("You continue your investigation, determined to solve the mystery...")  # Continue investigation message

    def interact_with_characters(self):
        print("You decide to interact with the characters in the room.")  # Interaction prompt
        character = int(input("If you want to speak to the witness and a suspect, "
                            "choose 1. \nIf you'd like to speak to other people in the "
                            "room, choose 2: "))  # Character interaction choice

        if character == 1:  # Interact with witness and suspect
            if not self.__characters_interacted:
                self.__logger.log("Interacting with suspects and witnesses.")  # Log interaction
                print("You decide to interact with the witness and suspect in the room:")

                clue_suspect = self.__suspect.interact()  # Interact with suspect
                self.__crime_scene.add_clue(clue_suspect)  # Add clue from suspect
                print(clue_suspect)

                suspect_alibi = self.__suspect.provide_alibi()  # Get suspect's alibi
                self.__crime_scene.add_clue(suspect_alibi)  # Add alibi as clue
                print(suspect_alibi)

                print(self.__suspect.perform_action())  # Perform action with suspect

                clue_witness = self.__witness.interact()  # Interact with witness
                self.__crime_scene.add_clue(clue_witness)  # Add clue from witness
                print(clue_witness)

                witness_observation = self.__witness.share_observation()  # Get witness observation
                self.__crime_scene.add_clue(witness_observation)  # Add observation as clue
                print(witness_observation)

                print(self.__witness.perform_action())  # Perform action with witness

                self.__characters_interacted = True  # Set interaction flag
            else:
                print("You have already interacted with the characters. They no longer wish to speak to you.")
        elif character == 2:  # Interact with NPCs
            if not self.__npcs_interacted:
                self.__logger.log("Interacting with people standing about.")  # Log NPC interaction
                print("You decide to speak to other people in the room:")
                indifferent_npc = NPC("Beatrice", "How do you do.")  # Create indifferent NPC
                friendly_npc = NPC("Seamus", "Welcome to our village.")  # Create friendly NPC
                hostile_npc = NPC("Evil Goblin", "Leave this place!")  # Create hostile NPC

                characters = [indifferent_npc, friendly_npc, hostile_npc]  # List of NPCs

                for character in characters:
                    print(character.interact())  # Interact with each NPC
                    print(character.perform_action())  # Perform action with each NPC

                self.__crime_scene.add_clue("Three people are hanging around the scene who have nothing to do with the crime.")  # Add clue about NPCs

                self.__npcs_interacted = True  # Set NPC interaction flag
            else:
                print("People in the room are tired of you. They no longer want to speak to you.")
        else:
            raise ValueError("This is not an option for a character.")  # Raise error for invalid character choice

    def examine_clues(self):
        self.__logger.log("Examination happening")  # Log clue examination
        print("You decide to examine the clues at the crime scene.")
        if not self.__crime_scene.investigated:  # Check if clues have been examined
            print("You find a torn piece of fabric near the window.")  # Clue found
            self.__crime_scene.add_clue("Torn fabric")  # Add clue to crime scene
            self.__crime_scene.investigated = True  # Set investigated flag
        else:
            print("You've already examined the crime scene clues.")  # Already examined message

    def choose_door(self):
        self.__logger.log("Doors are to be chosen")  # Log door choice
        print("You decide to choose a door to investigate:")

        for i, door in enumerate(self.__doors, start=1):  # List available doors
            print(f"{i}. {door}")

        door_choice = int(input("Enter the number of the door you want to investigate: "))  # Get door choice

        self.__logger.log(f"Player chooses to investigate door {door_choice}.")  # Log door choice

        if 0 < door_choice <= len(self.__doors):  # Validate door choice
            if door_choice == 1:  # Front door interaction
                if not self.__doors_checker[0]:
                    print("As you approach the front door, you hear a faint whisper... The plot thickens!")  # Clue found
                    self.__crime_scene.add_clue("faint whisper near kitchen")  # Add clue
                    self.__doors_checker[0] = True  # Mark door as checked
                    self.__logger.log("Front door has been investigated.")  # Log investigation
                else:
                    print("You have looked in the front door already.")  # Already checked message
                    self.__logger.log("Front door had been chosen before. No access.")  # Log access denial
            elif door_choice == 2:  # Library door interaction
                if not self.__doors_checker[1]:
                    print("You open the library door to reveal a hidden passage... What secrets does it hold?")  # Clue found
                    self.__logger.log("The library has been investigated.")  # Log investigation
                    self.__crime_scene.add_clue("hidden passage behind library door")  # Add clue
                    self.__doors_checker[1] = True  # Mark door as checked
                else:
                    print("You've looked in the library already.")  # Already checked message
                    self.__logger.log("The library had been chosen before. No access.")  # Log access denial
            elif door_choice == 3:  # Kitchen door interaction
                if not self.__doors_checker[2]:
                    print("You open the kitchen door. The mansion's chef prepares the evening meal. No clues to the mystery can be unveiled.")  # No clue found
                    self.__logger.log("The kitchen has been investigated.")  # Log investigation
                    self.__doors_checker[2] = True  # Mark door as checked
                else:
                    print("You've looked in the kitchen already.")  # Already checked message
                    self.__logger.log("The kitchen had been chosen before. No access.")  # Log access denial
        else:
            raise ValueError(f"Invalid door choice: {door_choice}")  # Raise error for invalid door choice

    def play_mini_games(self):
        print("\n=== Mini-Games ===")  # Mini-games section header
        available_games = [game for game in self.__mini_games if game not in self.__games_completed]  # Filter available games
        
        if not available_games:
            print("You've completed all mini-games!")  # All games completed message
            return
            
        print("\nAvailable mini-games:")  # List available mini-games
        for i, game in enumerate(available_games, 1):
            print(f"{i}. {game._name}")  # Print game names
            
        try:
            choice = int(input("\nChoose a game (enter number): ")) - 1  # Get game choice
            if 0 <= choice < len(available_games):  # Validate choice
                game = available_games[choice]  # Get selected game
                if game.play():  # Play the selected game
                    self.__games_completed.append(game)  # Add game to completed list
                    self.__crime_scene.add_clue(f"Found {game.reward} from {game._name}")  # Add reward as clue
            else:
                print("Invalid game choice!")  # Invalid choice message
        except ValueError:
            print("Please enter a valid number!")  # Handle non-integer input