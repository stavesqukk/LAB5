#1. Create a class Book with attributes title, author, and price. Write a
#constructor to initialize these values and create an object with sample data.
#● Add a method display_info() to the Book class that prints the book's
#title, author, and price. Call this method using a Book object.
#● Add a method update_price(new_price) to the Book class that updates
#the book's price. Demonstrate how to use it with an object.
class Book:
    def __init__(self, author,title,price):
        self.author =author 
        self.title = title 
        self.price = price 
    def display_info(self):
        print(f"{self.title} is written by {self.author} and its price {self.price}")
    def update_price(self,new_price):
        self.price = new_price
    

a = Book("Santosh","MATHS",1200)
a.display_info()
a.update_price(1300)
a.display_info()
