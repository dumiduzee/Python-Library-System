from connection import Con


class Actions:
    def __init__(self):
        self.__bookList = []
        self.__con = Con("localhost","root","4878","librarydb")
    def addBook(self,bookName,bookIsbn,bookAuthor):
        if bookName and bookIsbn and bookAuthor:
            try:
                queery = 'INSERT INTO library (name,isbn,author) VALUES (%s,%s,%s)'
                self.__con.getCursor().execute(queery,(bookName,bookIsbn,bookAuthor))
                self.__con.databaseCommit()
                return f"{bookName} successfully added to the library!!"
            except Exception as e:
                return f"Something went wrong while adding books to the library!! {e}"
        else:
            return "Fields can't be empty!!"

    def removeBook(self, bookIsbn):
        try:
            selectIsbn = f'SELECT * FROM library WHERE isbn="{bookIsbn}"'
            cursor = self.__con.getCursor()
            cursor.execute(selectIsbn)
            result = cursor.fetchone()

            if result:
                querry2 = f'DELETE FROM library WHERE isbn="{bookIsbn}"'
                print(querry2)
                cursor.execute(querry2)
                self.__con.databaseCommit()
                return f"{bookIsbn} deleted successfully!!!"
            else:
                return f"{bookIsbn} does not exist! Please check your ISBN again."

        except Exception as e:
            return f"Something went wrong while removing book ISBN - {e}"


