class Loggable:
    def __init__(self):
        self.__logs = []

    @property
    def logs(self):
        return self.__logs

    def log(self, message):
        if isinstance(message, str):
            self.__logs.append(message)

    def save_logs_to_file(self, filename):
        try:
            with open(filename, "w") as file:
                for line in self.__logs:
                    file.write(line + "\n")
        except FileNotFoundError as file_err:
            print(f"Error: File not found - {str(file_err)}")
        except PermissionError as perm_err:
            print(f"Error: Permission denied - {str(perm_err)}")
        except Exception as e:
            print(f"Error while saving logs to file: {str(e)}")