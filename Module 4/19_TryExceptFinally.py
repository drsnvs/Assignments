# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.

# In Python, exceptions can be handled using a try statement. The critical operation which can raise an exception is placed inside the try clause. The code that handles the exceptions is written in the except clause. We can thus choose what operations to perform once we have caught the exception.

try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass

# Example 1:

fruits = ['apple','banana','mango',10,20,30]
try:
    for i in fruits:
        print(i)
        print(i+1)
except Exception as ex:
    print("Error Generate:",ex)
finally:
    print("It Always Run")