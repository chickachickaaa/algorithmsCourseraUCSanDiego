# Uses python3
import sys

#def optimal_sequence(n):
#this was my bit before stack didn't work for 1
#import sys
#sys.setrecursionlimit(20000) #adding this to take care of #3 too much recurision. will problably have to apply  memoization. RecursionError: maximum recursion depth exceeded in comparison

d = {}

def f(n):
    if n == 1:
        return 0, -1
    if d.get(n) is not None:
        return d[n]
    ans = (f(n - 1)[0] + 1, n - 1)

    if n % 2 == 0:
        ret = f(n // 2)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 2)

    if n % 3 == 0:
        ret = f(n // 3)
        if ans[0] > ret[0]:
            ans = (ret[0] + 1, n // 3)

    d[n] = ans
    return ans

#solve(n)
def print_solution(n):
    ans = []
    while f(n)[1] != -1:
        ans.append(n)
        n = f(n)[1]
    ans.append(1)
    ans.reverse()
    for x in ans:
        print(x, end=' ')

def solve(n):
    k = 0 #added a loop because that's what stack said but honestly when i return k or print k is doesn't help.
    for i in range(1, n): #also we knew something was needed because the actual steps wasn't printing
        k = k + f(i)[0] #it worked. but totally not sure why. what does the k do?
    print(f(n)[0])
    print_solution(n)
    print('')



'''A(x) {
  if x<0 return 0;
  return something(x) + A(x-1)
}
Can be translated into:

A(x) {
  temp = 0;
  for i in 0..x {
    temp = temp + something(i);
  }
  return temp;
}'''


'''def print_solution(n):
    if f(n)[1] != -1:
        print_solution(f(n)[1])
    print(n, end='')

def solve(n):
    print(f(n)[0])
    print_solution(n)
    print(' ')
'''

n = int(input())
solve(n)


