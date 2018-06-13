# algorithm_practice

This is where I drop my practice scripts with algorithms as they come by. They can be from courses, or just general interests in the web

### Percolation
Based of the Princeton's highly rated algorithms courseara, this implementation in python uses the weighted quick union find algorithm to solve a percolation problem. Basically, by randomly making a cell in an nxn grid vacant, calculate the probability of it reaching percolation (ie. is the path betweem top and bottom open?).

### Counting SCC with Kosaraju's Algorithm
Here is my implementation of counting strongly connected components in a directed graph, an assignment from Stanford's coursera-algorithm course.

Some implementation notes: python is quite picky with the recursion depth, and the only way to work is to manually set a higher recursion depth and stack size within the script.

The current settins worked on my ubuntu (16.04 LTS) virtual box.

### Dijkstra shortest path python implementation

This is a naive implementation (m*n time) of Dijkstra's algorithm for finding the shortest path in a weighted, directed graph.\

Default starting node is 1, and default distance is 100000 (scale this to inf for larger graphs).

### Heap implementation for the Median Maintenance

This one was a lot of fun to make: An efficient manner (O(nlgn)) of computing rolling medians from an array using the heap datastructure. 

Essentially by creating two heaps: a min heap containing the n/2 largest values(H_high) and a max heap containing the n/2(ceiling) smallest values. Each time the two half lists get imbalanced, we extract the value from the larger half and inserting to the bottom of the smaller half, maintaining heap invarient for both heaps each time. 

Performance: 0.107s vs 9.32s for the naive implementation in python3. 
