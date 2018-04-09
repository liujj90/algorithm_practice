from weightedquickunionfind import *
import numpy as np


class Percolation(object):
	def __init__(self,n):
		self.n = n
		self.union_find = WeightedQuickUnionUF(self.n**2)
		self.grid = self.make_grid()
		
		self.num_open =0

	# if vacant: 0, not vacant = 1
	def make_grid(self):
		# initialise with all "not vacant"
	    grid = np.ones((self.n,self.n))
	    # make top and bottom vacant
	    grid[0,:], grid[self.n-1,:] = 0,0
	    for col in range(self.n):
	    	self.connect(0,0,0,col) #connect first row
	    for col in range(self.n):
	    	self.connect(self.n-1, 0, self.n-1, col) # connect last row
	    return grid

	def unrolled_coordinates(self, i,j):
		return i*self.n + j # need to unroll 2d array into 1d so we can work with single indices for weightedquickunionfind

	def connect(self, i1,j1,i2,j2):
		self.union_find.union(self.unrolled_coordinates(i1,j1), self.unrolled_coordinates(i2,j2))

	def make_vacant(self,i,j):
		# union with adjacent vacant sites
		if self.grid[i,j] !=0:
			self.num_open+=1
			self.grid[i,j] = 0
			# check if adjacent are vacant
			for (adjacentx, adjacenty) in [(i-1, j),(i+1,j), (i, j+1), (i, j-1)]:
				if self.grid[adjacentx,adjacenty] == 0:
					self.connect(i,j, adjacentx,adjacenty)

	def randomised_vacancy(self):
		self.make_vacant(np.random.randint(0,self.n-1), np.random.randint(0,self.n-1))
	def percolate(self):
		return self.union_find.connected(0,self.n**2-1) #is top and bottom connected?
# usage
grid1 = Percolation(5) # initialise a 5x5 grid
for i in range(6): # randomly open 6 cells 
	grid1.randomised_vacancy()
	print(grid1.grid, grid1.percolate()) # what the grid looks like, whether it percolates
