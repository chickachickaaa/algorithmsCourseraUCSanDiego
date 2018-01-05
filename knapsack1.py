# Uses python3
import sys
#each value can be used only once!
# optimal W either contains wn or doens't
# ith item is either used or not so you can compare max of using it and having value or not.
def optimal_weight(W, w): #big W is total weight or capacity of bag, little w is weight per bar, n is number of bars
    # write your code here


    dictValue = {}
    if w is in dictValue:
        return result # ?

    #initialize value!
    #they gave me this
    result = 0  # final max weight equals 0
    for i in n:
        for x in w:  #for gold bar x in all gold bars
            if result + x <= W: #if weight of that one gold bar plus the current total max weight is less than capacity
                result = result + x #add the gold ba weight to result
    dictValue[x] = n     #add current gold bar weight to hash with key w
    return result # result should be max weight of gold that fits, no fractions allowed! # and return the result




if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))




'''#weightsUsed = {}
    # if hashWeights contains w
    # return value(w)
    # other wise, value(w) = 0
    # for i in range(n):
        #if w(i) < w:
        #val = knapsack(w - wi) + vi
        #if val > value(w):
            #value(w) = val
    # insert value(w) into hashWeights with key w
    # return value(w)

    value = []
    if w in value.values():
        return value[w]
    else:
        value[w] = 0
    for i in range(n):
        #initialize here?
        value[0, j] = 0
        value[w, 0] = 0
        for w in range(W):
            value[w, i] = value[w, i-1]
            if w[i] <= w:
                val = value[w-w[i], i-1] + v[i]
                if value[w, i] < val:
                    value[w, i] = val

    return value[W, n]'''


