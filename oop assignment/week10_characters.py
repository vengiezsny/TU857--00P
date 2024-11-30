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


from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, dialogue):
        self._name = name
        self._dialogue = dialogue
        self._interacted = False

    def __str__(self):
        return f"{self.__class__.__name__}: {self._name}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self._name == other._name
        return False

    def __lt__(self, other):
        if isinstance(other, Character):
            return self._name < other._name
        return False

    @abstractmethod  # Declares an abstract method using a decorator.
    def perform_action(self):
        pass  # Abstract methods never contain any actual logic. The
        # transfer statement "pass" allows for this.

    # An abstract class must contain at least one abstract method.
    # However, "normal" methods may also be contained.
    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialogue}"
            self._interacted = True
        else:
            interaction = f"{self._name} is no longer interested in talking."

        return interaction


class Suspect(Character):
    def __init__(self, name, dialogue, alibi):
        super().__init__(name, dialogue)
        self._alibi = alibi

    def __repr__(self):
        return f"Suspect('{self._name}', '{self._dialogue}', '{self._alibi}')"

    def provide_alibi(self):
        return f"{self._name}'s Alibi: {self._alibi}"

    def perform_action(self):  # Implement the abstract method for Suspect
        return (f"Suspect {self._name} nervously shifts and avoids eye "
                f"contact.")


class Witness(Character):
    def __init__(self, name, dialogue, observation):
        super().__init__(name, dialogue)
        self._observation = observation

    def __add__(self, other):
        if isinstance(other, Witness):
            combined_observation = f"{self._observation} and {other._observation}"
            combined_name = f"{self._name} and {other._name}"
            return Witness(combined_name, "Combined observations",
                           combined_observation)

    def share_observation(self):
        return (f"{self._name}'s Observation: {self._observation}")

    def perform_action(self):  # Implement the abstract method for Witness
        return (f"Witness {self._name} speaks hurriedly and glances around "
                f"anxiously.")

class NPC(Character):
    """
    A class that implements the abstract class Character.
    The perform_action method must provide logic.
    The purpose of this class is to provide characters that are not
    essential for the mystery.
    """

    def perform_action(self):
        return f"{self._name} decides to hang around and see what will happen."

    def interact(self):
        super().interact()
        return "\nI know nothing!"

