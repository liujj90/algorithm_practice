## Heap implementation for the Median Maintenance

This one was a lot of fun to make: An efficient manner (O(nlgn)) of computing rolling medians from an array using the heap datastructure. 

Essentially by creating two heaps: a min heap containing the n/2 largest values(H_high) and a max heap containing the n/2(cieling) smallest values. Each time the two half lists get imbalanced, we extract the value from the larger half and inserting to the bottom of the smaller half, maintaining heap invarient for both heaps each time. 

Performance: 0.107s vs 9.32s for the naive implementation in python3. 
