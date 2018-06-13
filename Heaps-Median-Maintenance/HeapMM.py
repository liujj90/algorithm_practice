from math import *

## first define min and max heap data structures
class min_heap(object):
    def __init__(self):
        self.values = []
    def get_parent(self, ind):
        return self.values[floor((ind-1)/2)]
    def get_left(self, ind):
        if len(self.values) <= ind*2+1:
            return None
        else:
            return self.values[ind*2+1]
    def get_right(self, ind):
        if len(self.values) <= ind*2+2:
            return None
        else:
            return self.values[ind*2+2]
    def get_len(self):
        return len(self.values)
        
    def min_heapify(self, ind):
        # min_heap: A[parent] <= A [i]
        l = ind*2+1
        r = ind*2+2      

        if l <= (len(self.values)-1) and self.values[l] < self.values[ind]:
            smallest = l
        else:
            smallest = ind
        
        if r <= (len(self.values)-1) and self.values[r] < self.values[smallest]:
            smallest = r
        
        if smallest != ind:
            self.values[ind], self.values[smallest] = self.values[smallest], self.values[ind]
            self.min_heapify(smallest)
        
    def heap_sort(self):
        self.min_heapify(self.get_len())    
    
    def siftdown(self, start, end):
        i = self.values[end]
        while end>start:
            parent = self.get_parent(end)
            parentpos = floor((end-1)/2)
            if parent > i:
                self.values[end] = parent 
                end = parentpos
                continue
            break
        self.values[end] = i
        
    def insert_val(self, val):
        self.values.append(val) #append
        self.siftdown(0, self.get_len()-1)
        
    def glimpse_min(self):
        return self.values[0]
    
    def extract_min(self):
        size = self.get_len()-1
        self.values[size], self.values[0] = self.values[0], self.values[size]
        # delete from heap
        x = self.values.pop()
        self.min_heapify(0)
        return x


class max_heap(object):
    def __init__(self):
        self.values = []
    def get_parent(self, ind):
        return self.values[floor((ind-1)/2)]
    
    def get_left(self, ind):
        if len(self.values) <= ind*2+1:
            return None
        else:
            return self.values[ind*2+1]
        
    def get_right(self, ind):
        if len(self.values) <= ind*2+2:
            return None
        else:
            return self.values[ind*2+2]
        
    def get_len(self):
        return len(self.values)
    
    def max_heapify(self, ind):
        # max_heap: A[parent] >= A[i]
        l = ind*2+1
        r = ind*2+2      

        if l <= (len(self.values)-1) and self.values[l] > self.values[ind]:
            largest = l
        else:
            largest = ind
        
        if r <= (len(self.values)-1) and self.values[r] > self.values[largest]:
            largest = r
        
        if largest != ind:
            self.values[ind], self.values[largest] = self.values[largest], self.values[ind]
            self.max_heapify(largest)
    def heap_sort(self):
        for i in range(self.get_len(),-1,-1):
            self.max_heapify(i)    
    def siftdown(self, start, end):
        i = self.values[end]
        while end>start:
            parent = self.get_parent(end)
            parentpos = floor((end-1)/2)
            if parent < i:
                self.values[end] = parent 
                end = parentpos
                continue
            break
        self.values[end] = i
        
    def insert_val(self, val):
        self.values.append(val) #append
        self.siftdown(0, self.get_len()-1)   
    def glimpse_max(self):
        return self.values[0]
    
    def extract_max(self):
        size = self.get_len()-1        
        self.values[size], self.values[0] = self.values[0], self.values[size] # swap first and last value
        x = self.values.pop() # delete from heap
        self.max_heapify(0)
        return x


## function for median maintenance 
def get_medians(A):
    '''
    Goes through array A to assign values to:
    H_low, a max heap containing the smaller half of the array values
    H_high, a min heap containing the larger half of the array values
        ie. if value drawn is lower than min value of H_high, add value to H_low
    balances H_low and H_high to equal values if they become unbalanced
        ie. if number of values in H_low is larger than H_high, extract largest value from H_low to add to H_high
    Note: median value defined as the ciel value of odd index (base index 0)
    '''
    medians = []
    H_low = max_heap() #max-heap for lower half of array
    H_high = min_heap() #min-heap for higher half of array


    for i in range(len(A)):
        val = A[i]
        
        if i == 0:
            H_low.insert_val(val)
            medians.append(val) #median is the only value 
    
        elif i == 1:
            if A[1] < A[0]: # if second value is lower than first
                temp = H_low.extract_max() # extract max from min value
                H_high.insert_val(temp) # insert max value into H_high
                H_low.insert_val(val) # insert A[1] in H_low
                
            else:
                H_high.insert_val(val) # if value is larger then just insert into H_high
            medians.append(H_low.glimpse_max())
        
        else:
            # if value < min value from H_high, append to H_low, heap_sort then balance tree
            if val <= H_high.glimpse_min():
                H_low.insert_val(val)
            else:
                H_high.insert_val(val)
                
            if H_high.get_len() > H_low.get_len(): # if size of h_high is larger than h_low
                temp = H_high.extract_min()
                H_low.insert_val(temp)
                
            elif H_low.get_len() > H_high.get_len()+1: # if size of H_low 2 more than H_high
                temp = H_low.extract_max()
                H_high.insert_val(temp)

            medians.append(H_low.glimpse_max())
    return medians

'''
running the script
from time import time

with open('Medians.txt') as f: #creating array from file
    A = [int(line) for line in f]

start = time()
med = get_medians(A)
print(time()-start)

sum(med)

# check for correctness
from math import *
def medians(A):
    n = len(A)
    return sorted(A)[floor((n-1)//2)]

start = time()
ans = []
for i in range(1,len(A)+1):
    ans.append(medians(A[:i]))
print(time()-start)

sum(ans)

for i in range(10000):
    if ans[i] != med[i]:
        print(i)
'''

            

