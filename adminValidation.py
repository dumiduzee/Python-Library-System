class AdminValidation:
    def __init__(self,adminUsername,admniPassword):
        self.__adminUsername = adminUsername
        self.__admniPassword = admniPassword

    def userAndPasswordValidator(self):
        try:
            if self.userNameValidation() and self.passwordValidation():
                return True
            else:
                return False
        except Exception as e:
            print(f"Something wrong with username and password validator {e}")


    def userNameValidation(self):
        try:
            if self.__adminUsername == "dumidu":
                return True
            else:
                print("Invalida username")
                return False
        except Exception as e:
            print(f"Something went wrong with your username Validation {e}")

    def passwordValidation(self):
        try:
            if self.__admniPassword == "dumidu":
                return True
            else:
                print("Invalida password")
                return False
        except Exception as e:
            print(f"Something went wrong with your password Validation {e}")

