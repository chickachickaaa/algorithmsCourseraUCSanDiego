# python3
#import sys


def eff_fib(n):
    myfibarray = [0] * (n+1)
    #print(myfibarray)
    #if n == 0 or n == 1:
       # myfibarray[n] == n
    #myfibarray[1] = 1  # we changed this
    #myfibarray[0] = 0 #we changed this

    #print(myfibarray)
    while n < 2:
        return n
    #print(myfibarray)
    for i in range(2, n+1):
        myfibarray[0] = 0
        myfibarray[1] = 1
        myfibarray[i] = myfibarray[i-1] + myfibarray[i-2]
        #print (myfibarray)
    return myfibarray[n]



if __name__ == '__main__':
    input = input()
    n = int(input)
    print(eff_fib(n))

'''def fib(n):
  a = 0
  b = 1
  while b<n:
    print b 
    temp = a
    a = b
    b = temp+b
fib(4)'''

''' Uses python3 Naive
    def calc_fib(n):
        if (n <= 1):
            return n

        return calc_fib(n - 1) + calc_fib(n - 2)

    n = int(input())
    print(calc_fib(n)) '''
