## Huffman Codes

### Assignement 3 in part 3 of Stanford's Algorithm course
The aim of this exercise is to generate a variable length encoding of items represented as binary Huffman codes. 

The idea is that using information about how frequently an element appears on a given document/file, we can prioritise shorter codes (less bits) to the more frequently occuring (higher probability) elements, while lower priority and longer codes are assigned to lower probability items. 

A min-heap is used to implement fast retrieval of low probability items to build the Huffman tree from the child up.

Note: code does NOT generate the ideal answer, some tweaks have to be made to optimise. I suspect it is something within the tree- constructing step. 
