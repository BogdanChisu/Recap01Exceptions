"""
Exceptions are those events that occur during program execution and interrupt its normal course. In a sense, they are
the objects that represent the given error.

For example, run the following code:
"""
# a = 3
# b = [1, 0, 2]
# for elem in b:
#     result = a / elem
#     print(f"Result is: {result}")
"""
will cause an exception to occur: the ZeroDivisionError.

BUILT-IN EXCEPTIONS

The base exception class is Exception. All other inherit from it.

The most common include:
- Assertion error - This one occurs if the condition given after the keyword assert is false.
"""
# a = 1
# b = 2
# assert a == b
"""
- AttributeError - will occure when we try to reference an attribute or method of an object that does not exist
"""
# x = 10
# x.append(8)
"""
- FileNotFoundError - signals and input/output error and occurs when you try to access a file that does not exist
"""
# f = open('test.txt')
# print(f.read())
"""
- IndexError - occurs when trying to access a list item using index that does not exist
"""
# lst = [1, 2, 3, 4]
# print(lst[6])
"""
- ModuleNotFound - occurs when we try to import a module that is not installed
"""
# import sklearn
"""
- KeyError - occurs when trying to access a dictionary item using a key that does not exist
"""
# people = {
#     'Adam': 109,
#     'Monica': 230,
#     'Gregory': 1550
# }
# print(people['Betty'])
"""
- NameError - will show up when we try to use a variable that has not been initialized
"""
# a = 10
# c = a + b
# print(c)
"""
- ZeroDivisionError - We have seen this one already. It occurs when you try to divide by zero.

-------------------------------------------
HANDLING EXCEPTIONS
-------------------------------------------

The keywords related to exception handling include: try, except, finally, raise.
"""
# a = 3
# b = [1, 0, 2]
# for elem in b:
#     try:
#         result = a / elem
#     except ZeroDivisionError:
#         continue
#     print(f"Result is: {result}")
"""
In this case, the try clause is executed. If no exception occurs, the except clause is skipped and we go straight to
the line with the print function. However, if an exception occurs and its type matches the type defined in the
except part, the code in that block will get executed and the interpreter proceeds to the statement which follows the
try-except block.

MULTIPLE EXCEPTION HANDLING:
"""
# try:
#     # the string of statements where the error may appear
# except ValueError:
#     # handling an exception of ValueError type (when the parameter is of the incorrect data type)
# except (ZeroDivisionError, KeyError)
#     # handling of ZeroException\error and KeyError in the same manner
# except:
#     #handling all other exceptions
"""
It's a good practice to always specify the type of exception expected after the except keyword - this gives you more
control over your own code.

finally
---------------------

The finally clause is executed regardless of whether the exception occured or not.
"""
# try:
#     file = open("temp.txt")
#     file.write("Alice has a cat")
# except IOError:
#     print("An error occured while processing the file.!")
# finally:
#     file.close()
"""
In this case we open the file and write a sentence to it. Thanks to the use of finally , we can be sure that the file
has been closed, regardless of whether there was an error.

-------------------------------------------
RAISING EXCEPTIONS
-------------------------------------------
We also have the ability to raise exceptions in the code when we want to signal that certain behavior is a bug. The
keyword raise is used for this. 
"""
# a = 3
# b = [1, 0, 2]
# for i in b:
#     if i == 0:
#         raise ValueError("The divizor cannot be zero.")
#     result = a / i
#     print(result)

"""
CREATE YOUR OWN EXCEPTIONS

We can also create our own exception classes. For this we need to inherit from the parrent class of all exceptions:
Exception.

1.
"""


class CustomException(Exception):
    pass


a = 3
b = [1, 0, 2]
for elem in b:
    if elem == 0:
        raise CustomException("The divisor cannot be zero.")
    result = a / elem
    print(f"Result is {result}")


# 2.
class CustomException(Exception):
    def _init_(self):
        message = "Divisor cannot be zero."
        super()._init_(message)


a = 3
b = [1, 0, 2]
for elem in b:
    if elem == 0:
        raise CustomException("The divisor cannot be zero.")
    result = a / elem
    print(f"Result is {result}")