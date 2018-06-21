def insertion_sort(A): #A is the array to be sorted
    for j in range(1, len(A)):
        key = A[j]
        #insert A[j] into sorted array A[1...j-1]
        i = j-1
        while i >= 0 and A[i] > key: # looping to first term while previous entry is more than key
            A[i+1] = A[i] # move previous term to next index
            i = i-1 # loop to front of list - breaks when it is first term 
        A[i+1] = key # assign first term as key if it is smallest
    return A
    
def insertion_sort_dec(A): #A is the array to be sorted
    for j in range(1, len(A)):
        key = A[j]
        #insert A[j] into sorted array A[1...j-1]
        i = j-1
        while i >= 0 and A[i] < key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A
