# Uses python3
def edit_distance(s, t): #s is array 1 to n, t is array 1 to m, s[1...n], t[1...m] these are two words like short and ports
    #n is end of first string
    #m is end of second string
    #i is index in first string
    #j is index in second string
    #D array is what?
    m = len(s) + 1
    n = len(t) + 1
    D = {} #makin my first dictionary!
    #D(i, 0) = i  # indexing through short Edit distance. for all i and j
    #D(0, j) = j  # indexing through ports Edit distance
    for i in range(m):  # iterate through ports second string
        D[i,0] = i
    for j in range(n):  # interate through short first string
        D[0,j] = j
    for i in range(1,m):
        for j in range(1,n):
            cost = 0 if s[i-1] == t[j-1] else 1
            D[i,j] = min(D[i, j-1]+1, D[i-1, j]+1, D[i-1, j-1] +cost)
    return D[i,j]



    #return 0  # we want to eventually return an integer that signifies the edit distance, 1 for each insertion, deletion and mismatch

    #write your code here
    #first let's loop through with nested for loops the two strings
    #while doing that we'll compare and see if each index of each array
    # either is equal to eachother
    # is a mismatch
    # or needs to be inserted or deleted
    # if match then add 0 to counter
    # if mismatch then add 1 to counter
    # if insertion add 1 to counter
    # if delete add 1 to counter
    # match = D(i-1, j-1), mismatch = D(i-1, j-1) +1, insertion= D(i,j-1) +1, delete= D(i-1,j)+1,
    #how do you know which one to use at any point in index? AH easy on human eyes how tell a computer?
    #i think according to the game you go through if mismatch you do insertion or deletion (which one) and then mismatch is just last of what's left
    # so loop till match then figure out what insertion deletion needs to happen
'''def edit_distance(A[1 ... n], B[1 ... m])
    D(i,0) = i #indexing through short Edit distance
    D(0,j) = j #indexing through ports Edit distance 
    for j in range (1,m): #iterate through ports second string
        for i in range(1,n): #interate through short first string
            insertion = D(i, j-1) + 1
            deletion = D(i-1, j) + 1
            match = D(i-1, j-1)
            mismatch = D(i-1, j-1) + 1
            if A[i] = B[j]:  #this is s and t array, so what's the D array? D(i,j) it is the edit distance between A[1...i] and B[1...j]
                D(i,j) = min(insertion, deletion, match)
            else:
                D(i,j) = min(insertion, deletion, mismatch)
    return D(n, m)'''


    #return 0 # we want to eventually return an integer that signifies the edit distance, 1 for each insertion, deletion and mismatch

if __name__ == "__main__":
    print(edit_distance(input(), input()))
