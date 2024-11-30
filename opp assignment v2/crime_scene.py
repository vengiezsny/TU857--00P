class CrimeScene:
    def __init__(self, location):
        self.location = location
        self.__clues = []
        self.__investigated = False

    @property
    def investigated(self):
        return self.__investigated

    @investigated.setter
    def investigated(self, value):
        self.__investigated = value

    def add_clue(self, clue):
        self.__clues.append(clue)

    def review_clues(self):
        return self.__clues

    def print_clues(self):
        for i in range(len(self.__clues)):
            print(f"{i + 1}) {self.__clues[i]}")
