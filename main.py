import time
import datetime
import json

books = []
users = []

def save():
    user_data = []
    for user in users:
        user_data.append({"name": user.name,
                          "phone number": user.phone_number,
                          "balance": user.balance,
                          "history": user.history})
    with open("users.json", "w") as file:
        json.dump(user_data, file)
    
    book_data = []
    for book in books:
        book_data.append({"name": book.name,
                          "author": book.author,
                          "price": book.price})
    with open("books.json", "w") as file:
        json.dump(book_data, file)


def load():
    global books, users
    try:
        with open("users.json", "r") as file:
            user_data = json.load(file)
            
            for i in user_data:
                users.append(i["name"], i["phone number"], i["balance"], i["history"])
    except FileNotFoundError:
        users = []
    except json.JSONDecodeError:
        users = []
    try:
        with open("books.json", "r") as file:
            book_data = json.load(file)
            for i in book_data:
                books.append(i["name"], i["author"], i["price"])
    except FileNotFoundError:
        users = []
    except json.JSONDecodeError:
        users = []


class Book():

    def __init__(self, name="", author="", price=0):
        self.name = name
        self.author = author
        self.price = price

    def rent_book(self, current_account):
        for index, book in enumerate(books, start=1):
            print(f"""
------------------------
{index}. Name : {book.name}
Author : {book.author}
------------------------""")
        user = int(input("Which Book Would You Like To Get On Rent?\n"))
        chosen_book = books[user - 1]
        print(f"You rented {chosen_book.name}")
        current_account.history.append(f"You Rented {chosen_book.name} on {datetime.datetime.now()}")
        time.sleep(1)

    def add_book(self):
        name = input("Name : ")
        author = input("Author : ")
        price = float(input("Price : "))
        new_book = Book(name, author, price)
        books.append(new_book)
        print("Book Successfully Added")
        save()
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
        save()
        time.sleep(1)

    def buy_book(self, current_account):
        for index, book in enumerate(books, start=1):
            print(f"""
------------------------
{index}. Name : {book.name}
Author : {book.author}
Price : {book.price}
------------------------""")
        user = int(input("Which Book Would You Like To Buy?\n"))
        chosen_book = books[user - 1]
        if current_account.balance >= chosen_book.price:
            current_account.balance -= chosen_book.price
            print(f"You Bought {chosen_book.name}")
            current_account.history.append(f"You Bought {chosen_book.name} on {datetime.datetime.now()}")
            time.sleep(1)
        else:
            print("Not enough money")
            time.sleep(1)


class User():
    def __init__(self, name="", phone_number=0, balance=0, history = None):
        self.name = name
        self.phone_number = phone_number
        self.balance = balance
        self.history = [] if history is not None else []

    def register(self):
        self.name = input("Enter your name : ")
        try:
            self.phone_number = int(input("Enter your Phone Number : "))
        except ValueError:
            print("Enter valid phone number")
            time.sleep(1)
            return

        users.append(self)
        print("Successfully Registered")
        save()
        time.sleep(1)

    def login(self):
        name = input("Enter your name : ")
        try:
            phone_number = int(input("Enter your Phone Number : "))
        except ValueError:
            print("Enter valid phone number")
            time.sleep(1)
            return
        
        found = False

        for user in users:
            if name == user.name and phone_number == user.phone_number:
                print("Successfully Logged In")
                found = True
                return user
    
        if not found:
            print("Invalid Login Details")
            time.sleep(1)


def main():
    load()
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
            time.sleep(1)


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
            book.rent_book(current_account)

        elif choice == "2":
            book.buy_book(current_account)
        
        elif choice == "3":
            print("Which feature would you like to use:")
            choice = input("1. Check Balance\n" \
            "2. Add Funds\n")
            if choice == "1":
                print(f"Balance : {current_account.balance}")
                time.sleep(1)
            elif choice == "2":
                try:
                    amount = float(input("Enter amount of money to deposit : "))
                    print(f"Successfully deposited {amount}")
                    current_account.balance += amount
                    current_account.history.append(f"Deposited {amount} on {datetime.datetime.now()}")
                    time.sleep(1)
                except ValueError:
                    print("Enter valid amount")
                    time.sleep(1)
            else:
                print("Invalid Command")
                time.sleep(1)
        
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
            time.sleep(1)
            return

def test():
    book = Book()
    book.add_book()

test()
main()
