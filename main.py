import time
import datetime
import json

books = []

class Book():
    def __init__(self, name, author, price):
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
        print(f"You rented {chosen_book['Name']}")

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
------------------------""")
        user = int(input("Which Book Would You Like To Buy?\n"))
        chosen_book = books[user - 1]
        print(f"You Bought {chosen_book['Name']}")


class User():
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.history = []

    def register(self):
        pass

    def login(self):
        pass
