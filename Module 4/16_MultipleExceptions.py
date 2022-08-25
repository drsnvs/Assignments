# 16. Can one block of except statements handle multiple exception?

# yes, like except TypeError, SyntaxError
# Explanation: Each type of exception can be specified directly. There is no need to put it in a list.

# How do you handle multiple exceptions with a single except clause?
# You can also handle multiple exceptions using a single except clause by passing these exceptions to the clause as a tuple . except (ZeroDivisionError, ValueError, TypeError): print ( "Something has gone wrong.." ) Finally, you can also leave out the name of the exception after the except keyword.