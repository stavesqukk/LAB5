#2. Create a class Student with attributes name and marks. Create three objects
#of the class and display their details using a method show_details().
class Student: 
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks 
    def show_details(self):
        print (f"{self.name} has scored {self.marks}")

a = Student("Muskan",80)
b = Student("Shankar", 70)
c = Student("Simone", 88)
a.show_details()
b.show_details()
c.show_details()
