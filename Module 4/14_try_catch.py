# 14. How many except statements can a try-except block have? Name Some built-in exception classes:

# Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

# For example, let us consider a program where we have a function A that calls function B, which in turn calls function C. If an exception occurs in function C but is not handled in C, the exception passes to B and then to A.

# If never handled, an error message is displayed and our program comes to a sudden unexpected halt.

# Some built-in exception classes:

# IndentationError	: Raised when indendation is not correct
# KeyError	        : Raised when a key does not exist in a dictionary
# NameError	        : Raised when a variable does not exist
# SyntaxError	    : Raised when a syntax error occurs
# TypeError	        : Raised when two different types are combined