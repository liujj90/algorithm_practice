# algorithm_practice

This is where I drop my practice scripts with algorithms as they come by. They can be from courses, or just general interests in the web

### Percolation
Based of the Princeton's highly rated algorithms courseara, this implementation in python uses the weighted quick union find algorithm to solve a percolation problem. Basically, by randomly making a cell in an nxn grid vacant, calculate the probability of it reaching percolation (ie. is the path betweem top and bottom open?).

### Counting SCC with Kosaraju's Algorithm
Here is my implementation of counting strongly connected components in a directed graph, an assignment from Stanford's coursera-algorithm course.

Some implementation notes: python is quite picky with the recursion depth, and the only way to work is to manually set a higher recursion depth and stack size within the script.

The current settins worked on my ubuntu (16.04 LTS) virtual box.

