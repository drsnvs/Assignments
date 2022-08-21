# 1. What is File function in python? What is keywords to create and write file.

# Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

# Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

# When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

# Hence, in Python, a file operation takes place in the following order:

# File Handling Operations
# Most importantly there are 4 types of operations that can be handled by Python on files:

# * Open
# * Read
# * Write
# * Close

# Other operations include:
# * Rename
# * Delete

# There are keywords to create and write file

# 'x' - create a new file.
# * 'w' - Write Mode: This mode is used when you want to write data into the file or modify it. Remember, write mode overwrites the data present in the file.
# * 'r+' - Read or Write Mode: This mode is used when we want to write or read the data from the same file.