from percolation import Percolation
import numpy as np

class PercolationStats(object):
	def __init__(self, n, T):
		self.n = n
		self.T = T
		self.open_list = np.array([])
		self.PercolationStats()

	def PercolationStats(self):
		for trial in range(self.T):
			grid = Percolation(self.n) # initiatae nxn grid
			percolated = False
			num_open = 0
			while percolated == False: # while not percolating
				grid.randomised_vacancy() # randomly open cell
				num_open = grid.num_open # check how many total open cells
				percolated = grid.percolate() # check if percolated, breaks loop when true
			self.open_list  = np.append(self.open_list, np.float64(num_open)/self.n**2) # update open_list make sure value is a float

	def mean(self): #sample mean of percolation threshold
		return np.mean(self.open_list)
	def stddev(self):
		return np.std(self.open_list)/(self.T-1)
	def confidenceLo(self):
		return (self.mean() - 1.96*self.stddev())
	def confidenceHi(self):
		return (self.mean() + 1.96*self.stddev())


'''
p = PercolationStats(200,100)
print('mean:', p.mean(), 'standard deviation:', p.stddev(), '95% ci',[p.confidenceLo(), p.confidenceHi()])
'''