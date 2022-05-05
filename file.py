import sys
from datetime import date


# Open a file
my_file = open("file.txt", "w")
my_file.write(str(date.today()))

# Close my_file
my_file.close()