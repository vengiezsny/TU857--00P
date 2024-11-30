# CMPU 2016 Object-Oriented Programming
# TU857-2
# 2024-25, Semester 1: Python with Sunder Ali Khowaja
# SunderAli.Khowaja@tudublin.ie
#
# Mystery Adventure Game - Week 10 Lab Solution
# File Handling and Modules
#
# Learning objectives lab week 10:
# 1. Understanding File Handling:
#   - Gain an understanding of file handling concepts, including reading and
#   writing data to files.
#   - Learn about different modes for file access (e.g., reading, writing,
#   appending) and their applications.
# 2. Implementing Exception Handling for File Operations:
#   - Learn how to handle potential errors that may arise during file
#   handling operations.
#   - Understand how to use try...except blocks to catch and manage
#   exceptions related to file operations.
# 3. Organizing Code with Modules:
#   - Learn the benefits of organizing code into separate modules for better
#   code organization and reusability.
#   - Understand how to create and use custom modules to modularize your code.
#   - Learn how to handle exceptions related to file handling to create more
#   robust programs.
#   - Apply modularization to improve code reusability and maintainability
#   by breaking down the code into separate modules.


from week10_game import Game

if __name__ == "__main__":
    game = Game()
    game.run()

    # Using the logger
    print("\nGame Logs:")
    for log in game.log.logs:
        print(log)

    print("\nGame Error Logs:")
    for log in game.error_log.logs:
        print(log)