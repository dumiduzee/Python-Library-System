class AdminValidation:
    def __init__(self,adminUsername,admniPassword,con):
        self.__adminUsername = adminUsername
        self.__admniPassword = admniPassword
        self.__con = con

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
            query = f'SELECT username FROM admin WHERE username="{self.__adminUsername}"'

            cursor = self.__con.getCursor()
            cursor.execute(query)
            result = cursor.fetchone()
            if result:
                return True
            else:
                print("Invalid username")
                return False
        except Exception as e:
            print(f"Something went wrong with your username validation: {e}")

    def passwordValidation(self):
        try:
            querry = f'SELECT password FROM admin WHERE password="{self.__admniPassword}"'
            cursor = self.__con.getCursor()
            cursor.execute(querry)
            result = cursor.fetchone()
            if result:
                return True
            else:
                print("Invalida password")
                return False
        except Exception as e:
            print(f"Something went wrong with your password Validation {e}")

