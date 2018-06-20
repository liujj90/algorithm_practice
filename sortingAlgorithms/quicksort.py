# Partition types: start
def partition_start(A,l, end):
    pivot = A[l]
    i = l+1
    
    for j in range(l+1, end):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i-1], A[l] = A[l], A[i-1]
    return i-1

# Partition type: end
def partition_end(A,l, end):
    A[l], A[end-1] = A[end-1], A[l]
    pivot = A[l]
    i = l+1
    
    for j in range(1, end):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i-1], A[l] = A[l], A[i-1]

    return i-1


# Partition type, taking the median of 3 values
import math

def get_median(A):
    # returns the index of the median value
    n = len(A)
    temp = [A[0], A[math.floor((n-1)/2)], A[n-1]]
    median = 0
    for index, item in enumerate(temp):
        #print(index, item)
        if item != min(temp) and item != max(temp):
            median = index
    if median == 0:
        return 0
    elif median == 1:
        return math.floor((n-1)/2)
    else:
        return n-1


def partition(A,p, l, end):
    if p != l:
        A[l], A[p] = A[p], A[l]
    pivot = A[l]
    i = l+1
    
    for j in range(1, end):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i-1], A[l] = A[l], A[i-1]
    #print(A)

    return i-1


# quicksort median
def qsm(A):
    global count
    n = len(A)
    if n <= 1:
        return A
    count+= n-1
    p = get_median(A)
    p_ind = partition(A, p, 0, n)
    qsm(A[:p_ind])
    qsm(A[p_ind+1:])
    
    
# quicksort with either start or end partitions
count = 0
def qs(A):
    global count
    n = len(A)
    if n <= 1:
        return A
    else:
        count += n-1
        ind = partition_end(A,0, len(A))
        qs(A[:ind])
        qs(A[ind +1:])


'''
usage:

with open('quicksort.txt') as f:
    array = [int(line.split('\n')[0]) for line in f]
    
A = array[0:1000] 

count = 0
qs(A)

print(count)

count = 0
qsm(array)

print(count)
'''

