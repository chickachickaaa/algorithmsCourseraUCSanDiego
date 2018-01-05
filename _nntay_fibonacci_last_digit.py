# Uses python3
'''import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))'''



#efficient
import sys
def get_fibonacci_last_digit_efficient(n):
    myfibarray = [0] * (n + 1)
    #print(myfibarray)
    myfibarray[0] = 0
    myfibarray[1] = 1

    for i in range(2, n+1):

        myfibarray[i] = (myfibarray[i-1] + myfibarray[i-2])%10

    return myfibarray[n]


if __name__ == '__main__':
    input = input()
    n = int(input)
    print(get_fibonacci_last_digit_efficient(n))



