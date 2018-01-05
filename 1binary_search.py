# Uses python3
import sys

def binary_search(a, x):
    #left, right = 0, len(a)
    # write your code here
    #element = x #i believe #2
    #print(x)
    #for k in x: #or range(len(x)) HOW IS THIS NOT A LIST IF IT HAS MORE THAN ONE INTEGERRRR
        #element = x[k]
    element = x
    #print(element)
    first = 0
    last = (len(a)) #maybe dont need -1?
    #guess = 0 #don't reallyneed this i think but it helpsme
    #min = left
    #max = right #6
    #array = a #a = [1,2,3,4,5,6]
    #for i in range(first,last):
    while first < last: #so this will loop through array a to account for array x I need a loop somehwer before I think saying for j index of array x, x[j] = target then do binary search
        mid = first + (last - first)//2 #3 #get middle guess #index #maybe last - first thing is weird from stack...irst + (last - first)//2 is weird thing from stack
        if a[mid] == element:
            return mid
        else:
            if a[mid] < element:
                first = mid + 1

            elif a[mid] > element:
                last = mid - 1
                #first = a[0] doesn't change so redundant

    #a = [9,4,3,1,6,7]
    return -1

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')


'''Here's a pseudocode description of binary search:
Let min = 1 min=1m, i, n, equals, 1 and max = nmax=nm, a, x, equals, n.
Guess the average of maxmaxm, a, x and minminm, i, n, rounded down so that it is an integer.
If you guessed the number, stop. You found it!
If the guess was too low, set minminm, i, n to be one larger than the guess.
If the guess was too high, set maxmaxm, a, x to be one smaller than the guess.
Go back to step two.'''