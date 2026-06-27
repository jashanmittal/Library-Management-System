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
{index}. Name : {self.name}
Author : {self.author}
------------------------""")
        user = input("Which Book Would You Like To Get On Rent?\n")
        print(f"You rented the {books(user - 1)}")
            
