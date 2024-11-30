import pickle

class Data:
    def __init__(self):
        self.__data = {}
        self.__save_slot = 0

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def save(self):
        dir = "saves/" + str(self.__save_slot) + ".txt"
        with open(dir, 'wb') as file:
            pickle.dump(self.__data, file)

    def load(self):
        dir = "saves/" + str(self.__save_slot) + ".txt"
        with open(dir, 'rb') as file:
            self.__data = pickle.load(file)

    def return_data(self):
        return self.__data

