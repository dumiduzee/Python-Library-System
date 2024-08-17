from connection import Con
from adminValidation import AdminValidation
from libraryMenu import LibraryMenu
connection = Con("localhost","root","4878","logger")
print(connection.getDatabase())


# Admin Validation
while True:
    print("<==========🙌ADMIN LOGIN🙌==========>")
    adminUsername = input("Enter username : ").lower()
    adminPassword = input("Enter password : ").lower()
    try:
        if adminPassword and adminPassword:
            validation = AdminValidation(adminUsername,adminPassword)
            if validation.userAndPasswordValidator():
                LibraryMenu().Librarymenu()
                break
        else:
            print("Invalida username or password")
    except Exception as e:
        print(f"Something  error with your inputs {e}")

#