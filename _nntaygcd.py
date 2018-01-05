# Uses python2
'''import sys

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
    
    #efficient alg
def gcd_eff(a,b):
    #until r = 0:
#if r = 0 else do all of it
    #how to declare r variable?
     while (r !=0):
       r = a%b;
       a = b;
       b = r;
        #if r = 0
        #break;
        #else:
         # a = b;
          #b = r;
return b
'''

#second shot at efficient
import sys
def gcd_eff2(a, b):
    r = a % b
    #print(r)
    while r > 0:
        #print(r)
        a = b
        #print(a)
        b = r
        #print(b)
        r = a % b
        #print(b)
    else:
        return b


if __name__ == '__main__':
    input = raw_input()
    a, b  = map(int, input.split())
    print(gcd_eff2(a, b))
