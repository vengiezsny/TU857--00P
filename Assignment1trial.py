# Members:
# 1. Vengie Legaspi (student ID: c20366171).
# 2. John Hoang (student ID: bj456).
# 3. Jace (student ID: cb789).
# 4. Cristian Brillantes
# 5. 
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
# - main_game.py: The main game script.
# - achievements.py: Module for handling achievements.
# - leaderboards.py: Module for managing player rankings.
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


# CMPU 2016 Object-Oriented Programming
# TU857-2

from abc import ABC, abstractmethod
import pygame  # Import pygame for handling graphics and sound
import os     # Import os for file path handling

class Character(ABC):
    """This is the base class for all characters in the game."""

    def __init__(self, name):
        """Initialize the character with a name."""
        self.name = name

    @abstractmethod
    def perform_action(self):
        """Abstract method to perform character-specific actions.

        This method must be implemented by subclasses.
        """
        pass

    def interact(self):
        """This method will be customized by subclasses to provide unique interactions.

        Calls the perform_action method, which is abstract and must be defined in subclasses.
        """
        self.perform_action()  # Call the abstract method


class Suspect(Character):
    """This class represents a suspect and inherits from the Character class."""

    def __init__(self, name, alibi, body_language):
        """Initialize the suspect with a name, their alibi, and their body language cues."""
        super().__init__(name)  # Initialize the base Character class
        self.alibi = alibi  # Store the suspect's alibi
        self.body_language = body_language  # Store body language cues

    def perform_action(self):
        """Specific action for the suspect.

        Describes the suspect's alibi and body language during interaction.
        """
        print(
            f"Suspect {self.name} nervously claims: '{self.alibi}' and their body language suggests they might be lying.")


class Witness(Character):
    """This class represents a witness and inherits from the Character class."""

    def __init__(self, name, observation, demeanor):
        """Initialize the witness with a name, their observation, and demeanor."""
        super().__init__(name)  # Initialize the base Character class
        self.observation = observation  # Store the witness's observation
        self.demeanor = demeanor  # Store the demeanor of the witness

    def perform_action(self):
        """Specific action for the witness.

        Describes the witness's observation and demeanor during interaction.
        """
        print(f"Witness {self.name} states: '{self.observation}' and appears very anxious.")


class NPC(Character):
    """This class represents a non-playable character (NPC) in the game."""

    def __init__(self, name, demeanor):
        """Initialize the NPC with a name and demeanor."""
        super().__init__(name)  # Initialize the base Character class
        self.demeanor = demeanor  # Store the NPC's demeanor

    def perform_action(self):
        """NPC action based on demeanor.

        Determines what the NPC does based on their demeanor.
        """
        if self.demeanor == "friendly":
            print(f"NPC {self.name} greets you warmly: 'Hello there! How can I help you today?'")
        elif self.demeanor == "hostile":
            print(f"NPC {self.name} glares at you: 'What do you want? I'm not in the mood to talk.'")
        else:  # indifferent
            print(f"NPC {self.name} simply shrugs and says: 'I have nothing to say to you.'")


class CrimeScene:
    """This class represents the crime scene where clues are found."""

    def __init__(self, location):
        """Initialize the crime scene with its location and an empty list of clues."""
        self.location = location  # Set the location of the crime scene
        self.clues = []  # Initialize an empty list for clues

    def add_clue(self, clue):
        """Add a new clue to the list of clues."""
        self.clues.append(clue)  # Append the clue to the clues list

    def review_clues(self):
        """Show all the clues you have found so far."""
        print("Clues found: ", self.clues)  # Print all the clues


class SoundManager:
    """Handles all game sound effects and background music.
    
    This class is responsible for loading, playing, and managing all audio
    elements in the game, including sound effects and background music.
    """
    
    def __init__(self):
        """Initialize pygame mixer and load sound files."""
        pygame.mixer.init()
        
        # Base directory for assets
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Dictionary to store all game sounds
        self.sounds = {}
        
        try:
            # Attempt to load sound files
            sound_files = {
                'door_creak': 'door_creak.wav',
                'footsteps': 'footsteps.wav',
                'clue_found': 'clue_found.wav',
                'success': 'success.wav',
                'background': 'mystery_ambience.mp3'
            }
            
            for key, filename in sound_files.items():
                file_path = os.path.join(self.base_dir, 'assets', 'sounds', filename)
                if os.path.exists(file_path):
                    if key != 'background':
                        self.sounds[key] = pygame.mixer.Sound(file_path)
                    else:
                        self.sounds[key] = file_path
                else:
                    print(f"Warning: Sound file not found: {filename}")
                    
        except Exception as e:
            print(f"Warning: Error loading sound files: {e}")
            
    def play_sound(self, sound_name):
        """Play a specific sound effect."""
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except Exception as e:
                print(f"Warning: Could not play sound {sound_name}: {e}")
                
    def play_background_music(self):
        """Start playing background music on loop."""
        try:
            if 'background' in self.sounds:
                pygame.mixer.music.load(self.sounds['background'])
                pygame.mixer.music.play(-1)
        except Exception as e:
            print(f"Warning: Could not play background music: {e}")

class GraphicsManager:
    """Handles all visual elements of the game.
    
    This class manages the game window, loads and displays images,
    and handles all graphical rendering operations.
    """
    
    def __init__(self):
        """Initialize pygame display and load images."""
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("The Detective's Enigma")
        
        # Base directory for assets
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Dictionary to store all game images
        self.images = {}
        
        try:
            # Attempt to load image files
            image_files = {
                'drawing_room': 'drawing_room.png',
                'kitchen': 'kitchen.png',
                'library': 'library.png',
                'front_door': 'front_door.png',
                'suspect': 'suspect.png',
                'witness': 'witness.png'
            }
            
            for key, filename in image_files.items():
                file_path = os.path.join(self.base_dir, 'assets', 'images', filename)
                if os.path.exists(file_path):
                    self.images[key] = pygame.image.load(file_path)
                else:
                    print(f"Warning: Image file not found: {filename}")
                    # Create a default colored rectangle as placeholder
                    surface = pygame.Surface((self.screen_width, self.screen_height))
                    surface.fill((100, 100, 100))  # Gray color
                    self.images[key] = surface
                    
        except Exception as e:
            print(f"Warning: Error loading image files: {e}")

class Game:
    """This class represents the overall mystery game."""

    def __init__(self):
        """Set up the game, create characters, crime scene, and track which doors were visited."""
        self.running = True  # Keeps the game running while this is True
        self.game_started = False  # Tracks if the game has started
        self.crime_scene = CrimeScene("Drawing Room")  # Set the crime scene location

        # Set up the characters (suspect and witness)
        self.suspect = Suspect("Ms. Forteza", "I was in the library.", "Confirmed by the butler.")
        self.witness = Witness("Mr. Legaspi", "I saw someone near the kitchen window.", "Very anxious")

        # Create NPCs with different demeanors
        self.npcs = [
            NPC("Bob", "friendly"),
            NPC("Alice", "hostile"),
            NPC("Charlie", "indifferent")
        ]

        # Track whether each door has been visited
        self.visited_doors = {
            "front_door": False,
            "library_door": False,
            "kitchen_door": False
        }
        self.kitchen_visited = False  # Track if the kitchen door has been visited

        # Initialize sound and graphics managers
        self.sound_manager = SoundManager()
        self.graphics_manager = GraphicsManager()
        
        # Start the background music when the game begins
        self.sound_manager.play_background_music()

    def start(self):
        """Start the game and handle player input."""
        print("Welcome to 'The Poirot Mystery'")  # Game introduction
        print("You're about to solve a thrilling mystery as a detective.")

        while self.running:
            # Ask the player if they want to start or quit
            choice = input("Press 'q' to quit or 's' to start: ").lower()
            if choice == 's':
                self.game_started = True  # Game starts
                self.play_game()  # Begin the main game logic
            elif choice == 'q':
                self.end_game()  # End the game
            else:
                print("Please enter 's' to start or 'q' to quit.")

    def play_game(self):
        """This is the main part of the game where the player interacts with the world."""
        detective_name = input("Enter your detective's name: ")
        print(f"Welcome, Detective {detective_name}!")
        print("You're in the drawing room of a mansion, solving the case of the missing diamond.")

        # Display the initial game scene
        self.graphics_manager.display_scene('drawing_room')

        while self.running:
            # Give the player choices for what they want to do next
            action = input(
                "Press 'q' to quit, 'c' to continue, 'i' to interact, 'e' to examine clues, 'r' to review your clues, or 'doors' to choose a door: ").lower()
            if action == 'q':
                self.end_game()  # End the game
            elif action == 'c':
                print("You continue your investigation, trying to solve the mystery...")
                print("Please choose a door so you can continue solving the mystery!!")
            elif action == 'i':
                self.interact_with_characters()  # Talk to the characters
            elif action == 'e':
                if not self.crime_scene.clues:
                    print("You examine the clues at the crime scene.")
                    self.crime_scene.add_clue("Torn fabric near the kitchen window.")  # Add a clue
                else:
                    print("You've already examined the crime scene.")
            elif action == 'r':
                self.crime_scene.review_clues()  # Show all the clues
            elif action == 'doors':
                self.choose_door()  # Let the player pick a door to explore
            else:
                print("Invalid choice, please pick a valid option.")

    def interact_with_characters(self):
        """Interact with the suspect, witness, or NPCs."""
        print("Choose whom you want to interact with:")
        print("1. Suspect")
        print("2. Witness")
        print("3. NPCs")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            self.suspect.interact()  # Suspect interaction
        elif choice == "2":
            self.witness.interact()  # Witness interaction
        elif choice == "3":
            # Interact with NPCs using a for loop
            for npc in self.npcs:
                print(f"\nInteracting with {npc.name}:")
                npc.interact()  # Call the interact method for each NPC
                npc.perform_action()  # Call the perform_action method for each NPC
        else:
            print("Invalid choice.")  # Handle invalid input

    def choose_door(self):
        """Let the player pick a door to investigate and gather clues based on their choice."""
        if not self.kitchen_visited:
            # If kitchen hasn't been visited, show all three doors
            print("Choose a door to investigate:")
            print("1. Front door")
            print("2. Library door")
            print("3. Kitchen door")
            door_choice = input("Enter the number of the door you want to investigate: ")

            if door_choice == "1":
                # Front door logic
                if not self.visited_doors["front_door"]:
                    print("You hear a faint whisper at the front door... But something seems off.")
                    self.crime_scene.add_clue("Faint whisper near front door.")  # Add a clue
                    self.visited_doors["front_door"] = True  # Mark the door as visited
                else:
                    print("You've already investigated the front door.")
            elif door_choice == "2":
                # Library door logic
                if not self.visited_doors["library_door"]:
                    print("This is not the right door! You feel the walls closing in on you...")
                    self.crime_scene.add_clue("Books have been moved.")  # Add a clue
                    self.visited_doors["library_door"] = True  # Mark the door as visited
                else:
                    print("You've already investigated the library door.")
            elif door_choice == "3":
                # Kitchen door logic
                print("You enter the kitchen...")
                print("You find clues scattered everywhere.")
                print("The chef seems nervous, but no one is speaking up. Could this be it?")
                print("You're very close to solving the mystery!")
                print("Now, you can only choose between door 1 (Secret Front door) and door 2 (Secret Back door).")
                self.crime_scene.add_clue("Hidden passage is here.")  # Add a clue
                self.kitchen_visited = True  # Mark kitchen as visited
            else:
                print("Invalid choice. Please pick again.")
        else:
            # Restrict choices to front door or back door after visiting kitchen
            print("Choose between door 1 (Secret front door) and door 2 (Secret Back door):")
            print("1. Secret Front door")
            print("2. Secret Back door")
            door_choice = input("Enter the number of the door you want to investigate: ")

            if door_choice == "1":
                # Front door revisit
                print("You've already checked the front door. Something still feels wrong.")
            elif door_choice == "2":
                # Correct choice, player wins
                print("Congratulations! You've chosen the correct door and solved the mystery!")
                self.running = False  # End the game
            else:
                print("Invalid choice. Please pick again.")

    def end_game(self):
        """Ends the game."""
        print("Your journey has concluded. Thank you for playing!")
        self.running = False  # End the game loop

        # Stop all sounds and close pygame
        self.sound_manager.stop_background_music()
        pygame.quit()


# Start the game
game = Game()
game.start()  # Initiate the game start process
