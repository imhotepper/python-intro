import sys

n = int(sys.argv[1])

f1, f2 = 0, 1
#    print (f3, " ")
#    print (f3, " ")

for x in range(n):
   f3 = f1 + f2
#    print (f3, " ")
   f1 = f2
   f2 = f3

print (f2, " ")
