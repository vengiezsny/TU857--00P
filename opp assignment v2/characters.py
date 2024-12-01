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

    @abstractmethod
    def perform_action(self):
        pass

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

    def perform_action(self):
        return f"Suspect {self._name} nervously shifts and avoids eye contact."

class Witness(Character):
    def __init__(self, name, dialogue, observation):
        super().__init__(name, dialogue)
        self._observation = observation

    def __add__(self, other):
        if isinstance(other, Witness):
            combined_observation = f"{self._observation} and {other._observation}"
            combined_name = f"{self._name} and {other._name}"
            return Witness(combined_name, "Combined observations", combined_observation)

    def share_observation(self):
        return f"{self._name}'s Observation: {self._observation}"

    def perform_action(self):
        return f"Witness {self._name} speaks hurriedly and glances around anxiously."

class NPC(Character):
    def perform_action(self):
        return f"{self._name} decides to hang around and see what will happen."

    def interact(self):
        super().interact()
        return "\nI know nothing!"