# from abc import ABC, abstractmethod
# import openpyxl
# import xlrd
# import xlwt
# from xlrd import open_workbook
# from xlutils.copy import copy
# from openpyxl import load_workbook


# class InvalidOperationError(Exception):
#     pass

# class Point:
#     default_color = "red"


#     def __init__(self, x, y): # instance method
#         self.x = x # attribute for point objects
#         self.y = y #  and attribute in the contructor of Point class.


#     def __str__(self): # string representation --> Defines behavior for when str() is called on an instance of your class.
#         return f"({self.x}), ({self.y})"

#     def __eq__(self, object):
#         return self.x == another.x and self.y == another.y # this expression if true then they are considered equal.

#     def __add__(self, other):
#         return Point(self.x + another.x , self.y + another.y)

#     def __gt__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __lt__(self, other):
#         return self.x == other.x and self.y == other.y


#     @classmethod
#     def zero(cls):
#         return cls(0, 0)


#     def draw(self): # instance method
#         print(f"Point ({self.x}), ({self.y})")


# point = Point(10, 3)
# point = Point.zero()# factory method # a class method referencing to a zero attribute on class level assigning to point variable.
# point.draw()
# print(point)


# another = Point(1, 10)
# another = Point.zero()
# another.draw()
# print(another)
# print(point == another) # because == locates another point in the memory.
# print(point + another)


# class TagCloud:
#     '''__tags --> Are considered as private members '''
#     def __init__(self):
#         self.__tags = {}

#     def add(self, tag):
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.__tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):          # self, key, value
#         return self.__tags[tag.lower()] = count # dict[key]=value

#     def __le__(self, other):
#         return len(self.__tags)

#     def __iter__(self):
#         iter(self.__tags)           # iter(what do you iterate over ?) # buildin iter object


# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("python")
# cloud.add("python")
# cloud.add("Python")
# print(cloud.__tags)


# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative")
#         self.__price = value

# product = Product(10)
# print(product.price)


# class Animal(object):
#     def __init__(self):
#         super().__init__()
#         print("Animal Constructor")
#         self.age = 1


#     def eat(self):
#         print("eat")


# class Mammals(Animal):
#     def __init__(self):
#         super().__init__()           # super() --> helps when there is Method Overriding.
#         print("Mammals Constructor")
#         self.weight = 2

#     def walk(self):
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         print("swim")

# class Bird(Animal):
#     def fly(self):
#         print("fly")

# # class Chicken(Bird):   # Inheritance Abuse -- This is Multilevel inheritance and here
# #     pass               # Chicken class inherites from Bird class but Chicken cannot fly.


# m = Mammals()
# m.eat()
# print(m.age)
# print(m.weight)
# print(isinstance(m, object)) # inheritance from Animals to Mammals to Fish. (True)
# print(issubclass(Mammals, object))


# class Employee:
#     def greet(self):
#         print("Employee Greet")


# class Person:
#     def greet(self):
#         print("Person Greet")

# class Manager(Employee, Person): # This is called Multil-Level Inheritance.
#     pass                         # because Employee class is first output is show Employee Greet
#                                  # Is fine to use multilevel inheritance but things get complicated when we start to use commom func. ie. like def greet.

# manager = Manager()
# manager.greet()


# class Flyer:
#     ''' A good example of Multiple Inheritance '''
#     def fly(self):
#         pass

# class Swimmer:
#     def swim(self):
#         pass

# class FlyingFish(Flyer, Swimmer):
#     pass


# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.

# Class for Dog
# class Dog:

# 	# Class Variable
# 	animal = 'dog'

# 	# The init method or constructor
# 	def __init__(self, breed, color):

# 		# Instance Variable
# 		self.breed = breed
# 		self.color = color

# # Objects of Dog class
# Rodger = Dog("Pug", "brown")
# Buzo = Dog("Bulldog", "black")

# print('Rodger details:')
# print('Rodger is a', Rodger.animal)
# print('Breed: ', Rodger.breed)
# print('Color: ', Rodger.color)

# print('\nBuzo details:')
# print('Buzo is a', Buzo.animal)
# print('Breed: ', Buzo.breed)
# print('Color: ', Buzo.color)

# # Class variables can be accessed using class
# # name also
# print("\nAccessing class variable using class name")
# print(Dog.animal)


# # "A Good Example of Inheritance"

# class Stream(ABC):
#     def __init__(self) -> None:
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened.")
#         self.opened = True


#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed.")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("Reading data from file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from network")

# class MemoryStream(Stream):
#     def read(self):
#         print("Reading from memory")


# # Issues - 1) Stream is created to use into many subclasses for reuse.
# #          2) FileStream and NetworkStream has def read as common. Not Consistant (no way to unforce a common interface in different kind of stream)

# stream = MemoryStream()
# stream.open()


# class UIControl(ABC):

#     @abstractmethod
#     def draw(self):      #  Common Behaviour or Common derivative in children class.
#         print("UIControl under control")

# class TextBox(UIControl):
#     def draw(self):
#         print("TextBox under control")

# class DropDownList(UIControl):
#     def draw(self):
#         print("DropDown under control")

# def draw(controls): # Polymorphism - Many-Forms --> Here, draw() is taking many forms and draw works with all control without knowing in runtime.
#     for control in controls:
#         control.draw() # DuckTyping - python is happy untill it looks for draw().


# ddl = DropDownList()
# textbox = TextBox()
# print(isinstance(ddl, UIControl))
# draw([ddl, textbox])


# class Text(str):
#     def duplicate(self): # self represents the current object which is in this case a instance of a class
#         return self + self # so here we are concatinating a str with itself.

# class TrackableList(list):
#     def append(self, __object) -> None: # how did the append overide ?
#         print("Append called")
#         super().append(__object)


# text = Text("Python")  # Extending Build-in Type
# print(text.duplicate())

# list = TrackableList()
# list.append("1")


# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __eq__(self, object) -> bool:
#         return self.x == object.x and self.y == object.y

# p1 = Point(1, 2)
# p2 = Point(1, 2)
# print(id(p1))
# print(id(p2))
# print(p1 == p2)


# Point.default_color = "yellow"
# point = Point(1, 2)
# print(point.default_color)
# print(Point.default_color) # class attribute
# point.draw()


# another = Point(3, 4) # instance attribute , independent
# print(another.default_color)
# another.draw()


# print(type(Point))
# print(isinstance(point, Point))


# class ExcelOperation(object):
#     def __init__(self):
#         pass


#     # file = open(name, mode)

#     def write_excel(self):
#         lines=["Beautiful is better than ugly.\n",
#         "Explicit is better than implicit.\n", "Simple is better than complex.\n",
#         "Complex is better than complicated.\n"]
#         f = open("pythonio.txt","w")
#         f.writelines(lines)


#         f = open("pythonio.txt","w")
#         f.write("Monty Python's Flying Circus")


#     def read_excel(self):
#         f=open('pythonio.txt','r')


# excel = ExcelOperation()
# print(excel.read_excel())


# class ExcelOperations:
#     def read_path(self):
#         path = "/home/oto/Downloads/sort_eg.xlsx"
#         wb_obj = openpyxl.load_workbook(path)
#         sheet_obj = wb_obj.active
#         cell_obj = sheet_obj.cell(row=6, column=3)
#         print(cell_obj.value)
#         print(sheet_obj.max_column)
#         print(sheet_obj.max_row)

#     def read_excel(self):
#         workbook = xlrd.open_workbook("sort_eg.xlsx")
#         worksheet = workbook.sheet_by_index(0)

#         # Iterate the rows and columns
#         for i in range(0, 5):
#             for j in range(0, 3):
#                 # Print the cell values with tab space
#                 print(worksheet.cell_value(i, j), end='\t')
#             print('')

#     def write_excel(self):
#         wb = xlwt.Workbook()
#         print(wb)
#         sheet1 = wb.add_sheet('Sheet 1')
#         sheet1.write(1, 0, 'ISBT DEHRADUN')
#         sheet1.write(2, 0, 'SHASTRADHARA')
#         sheet1.write(3, 0, 'CLEMEN TOWN')
#         sheet1.write(4, 0, 'RAJPUR ROAD')
#         sheet1.write(5, 0, 'CLOCK TOWER')
#         sheet1.write(0, 1, 'ISBT DEHRADUN')
#         sheet1.write(0, 2, 'SHASTRADHARA')
#         sheet1.write(0, 3, 'CLEMEN TOWN')
#         sheet1.write(0, 4, 'RAJPUR ROAD')
#         sheet1.write(0, 5, 'CLOCK TOWER')

#         wb.save('sort_eg.xlsx')
#         print(wb)

#     def rewrite(self):
#         changes_work = load_workbook(filename="/home/oto/Downloads/sort_eg.xlsx") #load excel file
#         sheet = changes_work.active #open workbook
#         sheet["A1"] = "SHOW ID" #modify the desired cell
#         changes_work.save(filename="/home/oto/Downloads/sort_eg.xlsx") #save the file
#         print(changes_work)

        # workbook = xlwt.Workbook()
        # sheet = workbook.add_sheet("Sheet Name")
        # # Writing on specified sheet
        # sheet.write(0, 0, 'SAMPLE')

    # workbook.save("sort_eg.xlsx")
    # def write_excel(self):
    #     path = "/home/oto/Downloads/sort_eg.xlsx"
    #     wb_obj = openpyxl.load_workbook(path)
    #     ws = wb_obj['Customer']
    #     ws['A1'] = 'A1'
    #     wb_obj.save('sort_eg.xlsx')



# For Adding in Existing Table.
# rb = xlrd.open_workbook("sort_eg.xlsx")
# wb = copy(rb)
# s = wb.get_sheet(0)
# s.write(0,0,'A1')
# wb.save('sort_eg.xlsx')



