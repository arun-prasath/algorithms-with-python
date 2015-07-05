from sys import argv

script, x, y = argv

def getABCD(num1, num2):
    #print "Split %d, %d: " %(num1, num2)
    n = len(str(num1))
    a = num1 / (10**(n/2))
    b = num1 % (10**(n/2))
    c = num2 / (10**(n/2))
    d = num2 % (10**(n/2))
    #print "a=%d, b=%d, c=%d, d=%d" %(a, b, c, d)
    return a, b, c, d

def karatsuba(num1, num2):
    n = len(str(num1))
    
    if n % 2 == 1:
        n -= 1
    
    if n > 1:
        a, b, c, d = getABCD(num1, num2)
        #print "Mul a, c: %d * %d" %(a, c)
        ac = karatsuba(a, c)
        #print "Mul b, d: %d * %d" %(b, d)
        bd = karatsuba(b, d)
        #print "Mul a+b, c+d: %d * %d" %(a+b, c+d)
        ab_cd = karatsuba(a+b, c+d)
        ad_bc = ab_cd - ac - bd
        prod = (10**n)*ac + (10**(n/2))*ad_bc + bd
        return prod
    else:
        #print "Final Mul %d * %d" %(num1, num2)
        return num1 * num2


x = int(x)
y = int(y)

prod = karatsuba(x, y)
print prod

