## Greedy algorithms
Week one programming assignment for Stanford's Algorithms MOOC

### Greedy algorithm for calculating completion times
The task here is to compare 2 different methods for prioritizing queues using sum(weight * length) as a measure

1: Queue in descending order: weight-length
2: Queue in descending order: weight/length

Within each group, priotize by descending weight

### Prim's algorithm for calculating minimum spanning tree
I implemented an O(m+n) version here: improvements to be made by integrating a heap data structure for returning minimum edge weights.
