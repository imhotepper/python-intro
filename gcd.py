import sys

n = int( sys.argv[1])
m = int(sys.argv[2])

while n != m:
    if (n > m): 
        n -= m
    else:
        m -= n

print (n)
