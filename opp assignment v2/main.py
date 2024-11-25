from game import Game  # Import the Game class from the game module, which contains the main game logic

if __name__ == "__main__":  # Check if this script is being run directly (not imported as a module)
    game = Game()  # Create an instance of the Game class to start the game
    game.run()  # Call the run method on the game instance to begin the game loop and player interactions

    # After the game has finished running, display the game logs for the player
    print("\nGame Logs:")  # Print a header for the game logs section
    for log in game.log.logs:  # Iterate through each log entry in the game's log
        print(log)  # Print each log entry to provide insight into the player's actions during the game

    # Display any error logs encountered during the game
    print("\nGame Error Logs:")  # Print a header for the game error logs section
    for log in game.error_log.logs:  # Iterate through each error log entry in the game's error log
        print(log)  # Print each error log entry to help players understand any issues faced during gameplay