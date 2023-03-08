
Aysuarex
/
alx-higher_level_programming
Public
Code
Issues
Pull requests
Actions
Projects
Security
Insights
alx-higher_level_programming/0x08-python-more_classes/tests/4-main.py
@Aysuarex
Aysuarex ALX main Test file file for task 4
 1 contributor
27 lines (23 sloc)  575 Bytes
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
