import itertools
import math
def L_and_S(arr):
    n = len(arr)
    A = list(arr)

    # base case
    if n == 2: 
        if A[0] > A[1]:
            return (0, 1)
        else:
            return (1, 0)

    # recursive case
    # Let W be new array length n/2 (keeps track of largest elements)
    W = [0 for i in range(0, math.ceil(n/2))]
    # Let M be new array length n/2 (keeps track of swaps)
    M = [0 for i in range(0, math.ceil(n/2))]

    for i in range(0, math.ceil(n/2)):
        # swap larger element into first position of pair
        # set M[i] to 1 if pair was swapped, else 0
        # move larger element into W 
        if A[2*i] < A[2*i + 1]:
            temp = A[2*i]
            A[2*i] = A[2*i + 1]
            A[2*i + 1] = temp
            M[i] = 1
        W[i] = A[2*i]

    # now recurse on W
    (j, k) = L_and_S(W)
    # map back from W to A
    j_swap = M[j]
    k_swap = M[k] 
    j = 2*j
    k = 2*k
    if A[j + 1] > A[k]:
        k = j + 1   
        k_swap = 0 - j_swap
    return (j + j_swap, k + k_swap) # account for the swap

# test cases
arr = [1,2,4,5,7,9,10,19]
correct = 0
total = 0
for perm in itertools.permutations(arr):
    total = total + 1
    (p, l) = L_and_S(perm)
    larg = perm[p]
    sec = perm[l]
    if larg != 19 or sec != 10:
        print(perm)
    else:
        correct = correct + 1
print("correct = {}/{}".format(correct, total))