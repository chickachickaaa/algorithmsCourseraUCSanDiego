# Uses python3
import sys
import random

#In 3 Way QuickSort, an array arr[l..r] is divided in 3 parts:
#a) arr[l..i] elements less than pivot.
#b) arr[i+1..j-1] elements equal to pivot.
#c) arr[j..r] elements greater than pivot.
#pivot is m, x = A[l]
#pivot3 has two pivots but they're equal. so m1, x = A[l], m2 is x = A[l]
# k is random number between l and r
# l is start
# r is end
# A is array
def partition3(a, l, r):
    x = a[l] #pivot = m
    j = l;
    t = r;
    i = j
    #for i in range(l,t): now with putting i = j it is declared so we can do while
    while i <= t:
        if a[i] < x:
            #l <= k <= m1 - 1
            a[j],a[i] = a[i], a[j]
            j += 1
        elif a[i] > x:
            # m1 + 1 <= k <= r
            #a[i] = a[r-1] no but would maybe work? replacing with the stack overflow stuff
            a[t], a[i] = a[i], a[t]
            t -= 1
            i-= 1
        i += 1 #so we're swapping end notes first and last instead of j or in middle this allows you to not worry about equals
    return j, t #why do we return j and t? t I get because it's being replaced and pushed closer to the middle so it's m2, but j since
            #since it's adding one and started at the way left. j is switching to the other side of pivot soo maybe it's m2
            # m1 <= k <= m2
    #return k, #j m1 and m2 is the pivot? but they are equal
    #write your code here
    #writing psuedo stuff, understand it a bit better.
    #for all l<=k<=m1-1:
     #   A[k] < x
    #for all m1 <= k <=m2:
    #    A[k] = x
    #for all m1+1 <= k <= r:
    #    A[k] > x
    #pass
def partition2(a, l, r): #take in three parameters one an array, one to mark beginning and one for end
    x = a[l] #start point of array is a of l which is equalling x. pivot = m
    j = l;  # j is a new variable and it equals the first l, signifying this l is going to move
    for i in range(l + 1, r + 1):  # for i in range first plus 1 to last plus 1
        if a[i] <= x: #if index i of array a is less than or equal to x which is the pivot
            j += 1 #add one to the j group segment... how does that look exactly? it's not an array...
            a[i], a[j] = a[j], a[i]  # then a of index i switches with a of index j, to add to right segment
    a[l], a[j] = a[j], a[l] #and now that'll keep going then we switch out first with pivot ... when do we sort oh in next
    return j
def randomized_quick_sort(a, l, r):
    if l >= r: #if l is more than or equal to r. so first more than last then return
        return
    k = random.randint(l, r) #make k a random point between first and last (l and r)
    a[l], a[k] = a[k], a[l] #a at index l and a at index k switch so start is at random middle
    #use partition3 THIS IS WHERE YOU USE YOUR CODE I think this goes here m1, m2 = partition3(a,l,r)
    m1, m2 = partition3(a, l, r) #make variable m equal to j from partition2
    randomized_quick_sort(a, l, m1 - 1); #sort through array from l to j from partition2 minus 1
    randomized_quick_sort(a, m2 + 1, r); #sort through array from j from partition2 plus 1 to r at the end

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split())) #input is one integer showing number of numbers in array to sort, a is array of numbers
    randomized_quick_sort(a, 0, n - 1) #what is this 0 and n-1 doing?
    for x in a: #for x (which is number?) in array print x
        print(x, end=' ')
