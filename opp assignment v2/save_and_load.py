import os
import pickle

class SaveData:
    def __init__(self):
        self.data = {}
        self.save_dir = "saves"
        self.save_slot = "jan Alasa"

        if not os.path.exists(self.save_dir):
            os.mkdir(self.save_dir)

    # @property
    # def ddata(self):
    #     return self.data

    # @ddata.setter
    # def data(self, value):
    #     self.save_slot = value

    def save(self):
        dir = self.save_dir + "/" + self.save_slot
        with open(dir, 'wb') as file:
            pickle.dump(self.data, file)

    def load(self):
        dir = self.save_dir + "/" + self.save_slot
        if os.path.exists(dir):
            with open(dir, 'rb') as file:
                self.data = pickle.load(file)

    def return_data(self):
        return self.data

    def print_save_dir(self):
        print("List of save files (re-type to continue game):")

        saves_text = ""
        for i in os.listdir(self.save_dir):
            saves_text += i
            saves_text += ", "
        if len(saves_text) > 0:
            saves_text = saves_text[:len(saves_text) - 2] + "."

        print(saves_text)
        print("")
