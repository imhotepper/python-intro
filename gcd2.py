import sys

n = int( sys.argv[1])
m = int(sys.argv[2])

def gcd(n, m):
    while n != m:
        if (n > m): 
            n -= m
        else:
            m -= n
    return n

print (gcd( n, m))
