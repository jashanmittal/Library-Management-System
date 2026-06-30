import time
import datetime
import json

books = []
users = []

class Book():
    def __init__(self, name="", author="", price=0):
        self.name = name
        self.author = author
        self.price = price

    def rent_book(self):
        for index, book in enumerate(books, start=1):
            print(f"""
------------------------
{index}. Name : {book.name}
Author : {book.author}
------------------------""")
        user = int(input("Which Book Would You Like To Get On Rent?\n"))
        chosen_book = books[user - 1]
        print(f"You rented {chosen_book.name}")

    def add_book(self):
        name = input("Name : ")
        author = input("Author : ")
        price = float(input("Price : "))
        new_book = Book(name, author, price)
        books.append(new_book)
        print("Book Successfully Added")
        time.sleep(1)

    def delete_book(self):
        for index, book in enumerate(books, start=1):
            print(f"""
------------------------
{index}. Name : {book.name}
Author : {book.author}
Price : {book.price}
------------------------""")
        user = int(input("Which Book Would You Delete?\n"))
        books.pop(user - 1)
        print("Successfully Deleted Book From Database")
        time.sleep(1)

    def buy_book(self):
        for index, book in enumerate(books, start=1):
            print(f"""
------------------------
{index}. Name : {book.name}
Author : {book.author}
Price : {book.price}
------------------------""")
        user = int(input("Which Book Would You Like To Buy?\n"))
        chosen_book = books[user - 1]
        acc = User()
        if acc.balance >= book.price:
            print(f"You Bought {chosen_book.name}")
            time.sleep(1)
        else:
            print("Not enough money")
            time.sleep(1)


class User():
    def __init__(self, name="", phone_number=0, balance=0):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.history = []

    def register(self):
        self.name = input("Enter your name : ")
        try:
            self.phone_number = int(input("Enter your Phone Number : "))
        except ValueError:
            print("Enter valid phone number")
            return

        users.append(self)
        print("Successfully Registered")
        time.sleep(1)

    def login(self):
        name = input("Enter your name : ")
        try:
            phone_number = int(input("Enter your Phone Number : "))
        except ValueError:
            print("Enter valid phone number")
            return
        
        found = False

        for user in users:
            if name == user.name and phone_number == user.phone_number:
                print("Successfully Logged In")
                found = True
                return user
    
        if not found:
            print("Invalid Login Details")


def main():
    while True:
        print("Which feature would you like to use:")
        print("1. Register\n" \
        "2. Login\n" \
        "3. Exit")
        choice = input()

        if choice == "1":
            new_acc = User()
            new_acc.register()
            book = Book()
            menu(book, new_acc)

        elif choice == "2":
            login_acc = User()
            logged_in_user = login_acc.login() 
            if logged_in_user:
                book = Book()
                menu(book, logged_in_user)  

        elif choice == "3":
            exit()

        else:
            print("Invalid Command")


def menu(book, current_account):
    while True:
        print("Which feature would you like to use:")
        print("1. Rent Book\n" \
        "2. Buy Book\n" \
        "3. Balance\n" \
        "4. History\n" \
        "5. Logout")
        choice = input()

        if choice == "1":
            book.rent_book()

        elif choice == "2":
            book.buy_book()
        
        elif choice == "3":
            print(f"Balance : {current_account.balance}")
        
        elif choice == "4":
            for i in current_account.history:
                print(f"""
    ---------------------
    {i}
    ---------------------""")
        
        elif choice == "5":
            print("Logging Out....")
            time.sleep(1)
            return

        else:
            print("Invalid Command")
            return

def test():
    book = Book()
    book.add_book()

