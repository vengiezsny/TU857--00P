# Members:
# 1. Vengie Legaspi (student ID: c20366171).
# 2. John Hoang (student ID: bj456).
# 3. Jacey Janczak (student ID: C23493156).
# 4. Cristian Brillantes 
# 5. No one. ඞ
# Date: November 4, 2024.
#
# Game Expansion Explanation:
#
# In this expansion of our mystery game, "The Detective's Enigma," The Code
# Wizards group introduces exciting new features. We've implemented a
# comprehensive system of achievements and leaderboards that tracks players'
# progress and allows them to compete for the top detective spot.
# Additionally, we've incorporated educational elements that enhance the
# gaming experience with puzzles related to real-world detective work,
# helping players develop critical thinking skills.
#
# File Structure:
# - mini_games
# - puzzles.py: Module containing educational puzzle content.
#
# Running the Game:
# - To play "The Detective's Enigma" with our exciting expansions, run the
# "main_game.py" file.
# - Ensure that the "achievements.py," "leaderboards.py," and "puzzles.py"
# modules are in the same directory for full functionality.
#
# Enjoy the game and have fun becoming the ultimate detective!
#
# Important Note:
# Please keep this header unaltered in all submitted files.
################################################################################

from week10_characters import Suspect, Witness, NPC
from week10_logger import Loggable
from week10_crime_scene import CrimeScene

class Game:
    def __init__(self):
        self.__logger = Loggable()

        # A second logger that is specific to any error logs
        self.__error_logger = Loggable()

        # ... from before:
        self.__running = True
        self.__game_started = False
        self.__characters_interacted = False  # no double interactions
        self.__npcs_interacted = False # no double interactions

        self.__crime_scene = CrimeScene("Mansion's Drawing Room")
        self.__suspect = Suspect("Mr. Smith", "I was in the library all "
                                            "evening.", "Confirmed by the butler.")
        self.__witness = Witness("Ms. Parker", "I saw someone near the window "
                                             "at the time of the incident.",
                               "Suspicious figure in dark clothing.")
        self.__doors = ["Front door", "Library door", "Kitchen door"]
        self.__doors_checker = [False, False, False] # avoid using a door again

        self.__clues = []

    @property
    def log(self):
        # to do: think of some appropriate access checks here. For example,
        # only admins are allowed to read out logs.
        return self.__logger

    @property
    def error_log(self):
        return self.__error_logger


    # ---
    # user methods
    # ---

    def run(self):
        # ...
        self.__logger.log("Game started")
        # ...
        print("Welcome to 'The Poirot Mystery'")
        print("You are about to embark on a thrilling adventure as a detective.")
        print("Your expertise is needed to solve a complex case and unveil the truth.")

        while self.__running:
            try:
                self.update()
            except ValueError as ve:
                self.__error_logger.log(f"Error found:\n {ve}.")
            except Exception as e:
                self.__error_logger.log("Unexpected error from run():\n{e}.")
                print("Unexpected caught error during running of the Game. "
                      "We continue playing...")
            else:
                self.__logger.log("Successfully updating")
            finally:
                self.__logger.log("---")

    def update(self):
        # ...
        self.__logger.log("I'm updating")
        # ...

        if not self.__game_started:
            player_input = input("Press 'q' to quit or 's' to start: ")
            if player_input.lower() == "q":
                self.__running = False
                log_file = input("Please provide a file name for the logs: \n")
                self.__logger.save_logs_to_file(log_file)
            elif player_input.lower() == "s":
                self.__game_started = True
                self.start_game()
            else:
                raise ValueError("Incorrect user entry.")
        else:
            player_input = input(
                "Press 'q' to quit, 'c' to continue, 'i' to interact, "
                "'e' to examine clues, 'r' to review clues or 'd' to choose a "
                "door: ")

            # Logging the user input to keep a record of what the player is
            # choosing.
            self.__logger.log(f"Player input is {player_input}.")

            if player_input.lower() == "q":
                log_file = input("Please provide a file name for the logs: \n")
                self.__logger.save_logs_to_file(log_file)
                self.__running = False
            elif player_input.lower() == "c":
                self.continue_game()
            elif player_input.lower() == "i":
                try:
                    self.interact_with_characters()
                except ValueError as ve:
                    self.__error_logger.log(f"Error found:\n {ve}.")
                    print("Invalid character option.")
                except Exception as e:
                    self.__error_logger.log(f"Unexpected exception found for "
                                            f"player input to interact with "
                                            f"characters:\n{e}")
                    print("Unexpected error found for player input to "
                          "interact with character. We continue playing...")
            elif player_input.lower() == "e":
                self.examine_clues()
            elif player_input.lower() == "d":
                try:
                    self.choose_door()
                except ValueError as ve:
                    print("This door choice does not exist.")
                    self.__error_logger.log(f"Error found:\n{ve}")
                except Exception as e:
                    self.__error_logger.log(f"Unexpected error found for "
                                            f"player input:\n{e}")
                    print("Unexpected error from player input. We continue "
                          "playing...")
            elif player_input.lower() == "r":
                clues = self.__crime_scene.review_clues()
                if clues:
                    print(clues)
                else:
                    print("You have not found any clues yet.")
            else:
                raise ValueError("Incorrect user game option choice made.")

    def start_game(self):
        # ...
        self.__logger.log("Game is starting")
        # ...

        # from before...
        player_name = input("Enter your detective's name: ")
        print(f"Welcome, Detective {player_name}!")
        print("You find yourself in the opulent drawing room of a grand mansion.")
        print("As the famous detective, you're here to solve the mysterious case of...")
        print("'The Missing Diamond Necklace'.")
        print("Put your detective skills to the test and unveil the truth!")

    def interact_with_characters(self):
        """The interact_with_characters method within the Game class
        demonstrates the interaction with characters,
        where each character's dialogue and unique actions (e.g., providing
        an alibi, sharing an observation) are displayed. """

        # ...
        self.__logger.log("Interactions happening")
        # ...
        print("You decide to interact with the characters in the room.")
        character = int(input("If you want to speak to the witness and a "
                           "suspect, "
                        "choose 1. \nIf you'd like to speak to other people in "
                        "the "
                        "room, choose 2: "))

        if character == 1:
            if not self.__characters_interacted:
                self.__logger.log("Interacting with suspects and witnesses.")
                print(
                    "You decide to interact with the witness and suspect in "
                    "the room:")

                clue_suspect = self.__suspect.interact()
                self.__crime_scene.add_clue(clue_suspect)
                print(clue_suspect)  # keep the outputs going

                suspect_alibi = self.__suspect.provide_alibi()
                self.__crime_scene.add_clue(suspect_alibi)
                print(suspect_alibi)

                # use the new abstract method
                print(self.__suspect.perform_action())

                clue_witness = self.__witness.interact()
                self.__crime_scene.add_clue(clue_witness)
                print(clue_witness)

                witness_observation = self.__witness.share_observation()
                self.__crime_scene.add_clue(witness_observation)
                print(witness_observation)

                # use the new abstract method
                print(self.__witness.perform_action())

                self.__characters_interacted = True
            else:
                print(
                    "You have already interacted with the characters. They no "
                    "longer wish to speak to you.")
        elif character == 2:
            if not self.__npcs_interacted:
                self.__logger.log("Interating with people standing about.")
                # Creating and interacting with characters
                print("You decide to speak to other people in the room:")
                indifferent_npc = NPC("Beatrice", "How do you do.")
                friendly_npc = NPC("Seamus", "Welcome to our village.")
                hostile_npc = NPC("Evil Goblin", "Leave this place!")

                characters = [indifferent_npc, friendly_npc, hostile_npc]

                for character in characters:
                    print(character.interact())
                    print(character.perform_action())

                self.__crime_scene.add_clue("Three people are hanging around the "
                                          "scene who have nothing to do with the "
                                          "crime.")

                self.__npcs_interacted = True
            else:
                print("People in the room are tied of you. They no longer "
                      "want to speak to you.")
        else:
            raise ValueError("This is not an option for a character.")
            # print("This was not an option.")

    def examine_clues(self):
        # ...
        self.__logger.log("Examination happening")
        # ...
        # from before...
        print("You decide to examine the clues at the crime scene.")
        if not self.__crime_scene.investigated:
            print("You find a torn piece of fabric near the window.")
            self.__crime_scene.add_clue("Torn fabric")
            self.__crime_scene.investigated = True
        else:
            print("You've already examined the crime scene clues.")

    def choose_door(self):
        # ...
        self.__logger.log("Doors are to be chosen")
        # ...

        print("You decide to choose a door to investigate:")

        # nice output to show which door leads to what.
        # human friendly output starts with 1, default would be 0.
        for i, door in enumerate(self.__doors, start=1):
            print(f"{i}. {door}")

        door_choice = int(input("Enter the number of the door you want to "
                             "investigate: "))

        self.__logger.log(f"Player chooses to investigate door {door_choice}.")

        if 0 < door_choice < len(self.__doors)+1: # for valid entry check
            if door_choice == 1:
                if not self.__doors_checker[0]:
                    print("As you approach the front door, you hear a faint "
                          "whisper... The plot thickens!")
                    self.__crime_scene.add_clue("faint whisper near kitchen")
                    self.__doors_checker[0] = True
                    self.__logger.log("Front door has been investigated.")
                else:
                    print("You have looked in the front door already.")
                    self.__logger.log("Front door had been chosen before. No "
                                      "access.")
            elif door_choice == 2:
                if not self.__doors_checker[1]:
                    print("You open the library door to reveal a hidden "
                          "passage... "
                          "What secrets does it hold?")
                    self.__logger.log("The library has been investigated.")
                    self.__crime_scene.add_clue("hidden passage behind "
                                               "library door")
                    self.__doors_checker[1] = True
                else:
                    print("You've looked in the library already.")
                    self.__logger.log("The library had been chosen before. "
                                      "No access.")
            elif door_choice == 3:
                if not self.__doors_checker[2]:
                    print("You open the kitchen door. The mansion's chef "
                          "prepares the evening meal. No clues to the mystery "
                          "can be unveiled.")
                    self.__logger.log("The kitchen has been investigated.")
                    self.__doors_checker[2] = True
                else:
                    print("You've looked in the kitchen already.")
                    self.__logger.log("The kitchen had been chosen before. "
                                      "No access.")
        else:
            raise ValueError(f"Invalid door choice: {door_choice}") # this
            # needs to be
            # caught where we call the door handling.

    def continue_game(self):
        print("You continue your investigation, determined to solve the mystery...")
        # ...
        self.__logger.log("Continuing the game.")
        # ...

