from connection import Con
from tabulate import tabulate
import pandas as pd

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

    def ShowAllBooks(self):
        # Query to get all books from the library
        query = 'SELECT * FROM library'

        # Get cursor and execute the query
        cursor = self.__con.getCursor()
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            # Define headers for the DataFrame
            headers = ["ID", "NAME", "ISBN", "AUTHOR"]

            # Convert result to DataFrame
            df = pd.DataFrame(result, columns=headers)

            # Save DataFrame to Excel file
            excel_filename = 'library_books.xlsx'
            df.to_excel(excel_filename, index=False, engine='openpyxl')

            return f"Data has been successfully saved to {excel_filename}"
        else:
            return "No result found!!"

    def updateBook(self,bookIsbn):
        if bookIsbn:
            bookName = input("Enter book name : ")
            autho = input(f"Enter author of book {bookIsbn} : ")
            try:
                if (bookName and autho):
                    querry = f'UPDATE library SET name="{bookName}" , author="{autho}" WHERE isbn="{bookIsbn}"'
                    print(querry)
                    cursor = self.__con.getCursor()
                    cursor.execute(querry)
                    return f"{bookName} Updated successfully!!"
                else:
                    return "Fields cant be empty!!"
            except Exception as e:
                return f"Something went wrong while adding book!! {e}"


