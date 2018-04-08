## WeightedQuickUnionUF in python
### The purpose of this script is to reverse engineer WeightedQuickUnionUF based on documnentation + lecture slides

'''
From "https://algs4.cs.princeton.edu/code/javadoc/edu/princeton/cs/algs4/WeightedQuickUnionUF.html"
other resources from lecture notes "https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf"

Represents a union-find data type (disjoint-sets datatype). 
Supports 1) union 2) find operations
3) Connected operation for determining whether two sites are in the same component, and
4)count opteration that returns the total number of components

Union-find models connectivity among of n points in a set, {0... n-1}. 
"is-connectec-to" relation must be an equivalence relation:
Reflexive: p is connected to p
symmetric: if p is connected to q, q is connected to p
transitive: if p is connected to q and q is connected to r, p is connected to r

Equivalence relation partitions sites into equivalence clesses or components:
two sites are the same component only if they are connected
Both sites and components are identified with integers between 0 and n-1 <- what does this mean?
Initially, there are n components, 
the "component identifier" of a component (root, set representative, canonical element) is one of the sites 
in the component: two sites have the same "component identifier" only if they are the same component
	union(q, p) adds a connection between sites p and q, if p and q are in different components, 
	then it replaces these two components wiht a new component that is the union of the two

	find(p) returns the component identifier of component containing p

	connected(p,q) returns true if both p and q are in the same component, and false otherwise

	count() returns the number of components

The component identifier of a component can change only when the component itself changes during a union call

Weighted quick union by size (without path compression): 
1) initializes a data structure with n sites in linear time
2) Union, find and connected operations take O(lg(n)) time
Count operation takes constant time
'''

#list of integers between n, n-1 where each integer points to an index in the list to which it is connected
## input: items = [(p,q), (i,j)] 

class WeightedQuickUnionUF(object): 
	def __init__(self,N): # N is the number of objects with connections
		self.id = list(range(N))
		self.tree_size = [1]*N

	def root(self, i):
		while i!= self.id[i]: # if i is not pointing to itself
			self.id[i] = self.id[self.id[i]] # connect to i's root
			i = self.id[i] #assign new root
		return i
	def find(self, p):
		return self.root(p)

	def connected(self, p, q):
		return (self.root(p) == self.root(q)) #true/false
	def count(self):
		return(len(set(self.id))) # use sets to get unique values, count number of unique values

	def union(self, p,q):
		i = self.root(p)
		j = self.root(q)
		if i == j:
			return
		if self.tree_size[i] < self.tree_size[j]: #if value at i < value at j
			self.id[i] = j # j is root
			self.tree_size[j] += self.tree_size[i] # tree size at j grows by tree size of i
		else:
			self.id[j] = self.id[i] # i is root
			self.tree_size[i] += self.tree_size[j]  # tree size of i grows by tree size j 
'''
union_find = WeightedQuickUnionUF(10)
for (p, q) in [(3, 1), (4, 9), (8, 0), (2, 1), (5, 6), (5, 4), (7, 2), (4, 8), (6, 3), (8, 4)]:
	union_find.union(p,q)
print(union_find.id, union_find.connected(0,1),union_find.find(6) , union_find.count())
'''