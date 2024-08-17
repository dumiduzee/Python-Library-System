class Actions:
    def __init__(self):
        self.__bookList = []
    def addBook(self,bookName,bookIsbn,bookAuthor):
        if bookName and bookIsbn and bookAuthor:
            try:
                self.__bookList.append({"name":bookName,"bookIsbn":bookIsbn,"bookAuthor":bookAuthor})
                return f"{bookName} successfully added to the library!!"
            except Exception as e:
                return f"Something went wrong while adding books to the library!! {e}"
        else:
            return "Fields can't be empty!!"

    def removeBook(self,bookIsbn):
        try:
            if any(bookIsbn in dict.values() for dict in self.__bookList):
                return f"{bookIsbn} removed successfully!!"
            else:
                return f"{bookIsbn} is not exists!! check your isbn again"
        except Exception as e:
            return f"Something went wrong while removing book isbn - {bookIsbn}"

