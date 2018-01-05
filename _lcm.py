# Uses Python2
import sys
'''
def lcm_naive(a, b):
    if a > b:
        a, b = b, a
    for x in range(b, a*b+1, b):
        if x % a == 0:
            return x

if __name__ == '__main__':
    input = raw_input()
    a, b = map(int, input.split())
    print(lcm_naive(a, b)) '''



def lcm_eff(a, b):
    def gcd(a, b):
        r = a % b
        # print(r)
        while r > 0:
            # print(r)
            a = b
            # print(a)
            b = r
            # print(b)
            r = a % b
            # print(b)
        else:
            return b
    l = (a * b) // gcd(a, b)
    return l


if __name__ == '__main__':
    input = raw_input()
    a, b = map(int, input.split())
    print(lcm_eff(a, b))






