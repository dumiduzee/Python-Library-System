import mysql.connector


class Con:
    def __init__(self, host, username, password, database):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__database = database

        self.__db = mysql.connector.connect(
            host=self.__host,
            user=self.__username,
            passwd=self.__password,
            database=self.__database
        )

    def getDatabase(self):
        return self.__db

    def getCursor(self):
        return self.getDatabase().cursor()

    def databaseCommit(self):
        return self.getDatabase().commit()

    def cursorCommit(self):
        return self.getCursor().commit()
