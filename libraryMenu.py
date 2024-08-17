from actions import Actions
class LibraryMenu:
    def __init__(self):
        self.__activity = Actions()
        self.__flag = True
    def Librarymenu(self):
        while self.__flag:
            print("<==========🙌LIBRARY SYSTEM🙌==========>")
            print("✨[A] Add a book to the library")
            print("✨[B] Remove book from library")
            print("✨[C] Update book details")
            print("✨[D] Show all books")
            print("✨[X] Exit")
            print("<==========🙌LIBRARY SYSTEM🙌==========>")
            try:
                mainUserChoice = input("==> ").upper()
            except Exception as e:
                print(f"Check your inputs and try again!!! {e}")

            # CHECK USER INPUTS
            match mainUserChoice:
                case "A":
                    bookName = input("Enter book name : ").lower()
                    bookIsbn = input("Enter isbn number : ").lower()
                    bookAuthor = input("Enter book author: ").lower()
                    print(self.__activity.addBook(bookName,bookIsbn,bookAuthor))
                case "B":
                    bookIsbn = input("Enter isbn number : ")
                    print(self.__activity.removeBook(bookIsbn))
                case "C":
                    pass
                case "D":
                    pass
                case "X":
                    print("✨Programmed exited!!✨")
                    self.__flag = False

