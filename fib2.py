import sys

n = int(sys.argv[1])

def fib(n):
   f1, f2 = 0, 1
   for x in range(n):
      f3 = f1 + f2
      f1 = f2
      f2 = f3
   return f2

print (fib(n))
