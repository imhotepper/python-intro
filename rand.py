from ast import arg
import random 
import sys

if (len(sys.argv) > 1):
    nr =int( sys.argv[1])
else: 
    nr = random.randint(3, 9)

print( nr)

if nr % 2 ==0:
    print( "Even")
else:
    print( "Odd")