import pandas as pd #for counting vertices in each SCC (with a unique leader)

import sys ,resource
## increase recursion depth (only works on unix right now.. )
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))


class kosaraju(object):
    def __init__(self, graph, size):
        self.graph = graph # adjacency list
        self.n = size
        self.G, self.Grev = self.makeGraph(self.graph) # graph is an adjacency matrix {V1:[V2,V3....]}
        
        self.explored = {}
        self.leader = {} 
        self.s = None # leaders in second pass
        self.t = 0 # finishing time in first pass
        self.finish_time = {}

    def makeGraph(self, g): #transforms adjacency list into matrix
        graph, graphrev = {},{}
        
        for i in range(1, self.n+1):
            graph[i], graphrev[i] = [],[]
        
        for (key,value) in g:
            graph[key].append(value)
            graphrev[value].append(key)
            
        return graph, graphrev
    
    
    def dfs(self, graph, vertex): # depth first search
        self.explored[vertex] = 1
        self.leader[vertex] = self.s 
        for edge in graph[vertex]:
            if self.explored[edge] == 0:
                self.dfs(graph, edge)
        self.t += 1 # finish time
        self.finish_time[vertex] = self.t # assign finish time to vertex at the end of loop
    
    def dfs_loop(self, graph):
        self.t = 0
        self.s = 0
        for i in range(1, self.n+1):
            self.explored[i] = 0 # set all nodes to unexplored
            
        for vertex in range(self.n, 0, -1): # count down from largest numbered vertex
            if self.explored[vertex] == 0:
                self.s = vertex #potential leader vertex
                self.dfs(graph, vertex)
                
    def count_scc(self): # returns the 5 largest SCCs
    '''
    self.leader is formatted as {vertex(1-n)): leader vertex .... }
    the strategy here is to transform this dict into a pandas Series,
    then perform value_counts(), which counts the number of occurances of each leader vertex in the Series
    which returns the number of members in each SCC (per leader vertex)
    count_scc only displays the top 5 
    '''

        count = pd.Series(self.leader).value_counts()[:5] 
        return count
        
                
    def kosaraju_algo(self):
        #return self.G, self.Grev
        print('first dfs_loop initiated')
        self.dfs_loop(self.Grev)
        print('first dfs_loop completed')
        reordered_graph = {}
        # reorder the graph such that vertices are called in order of finish time
        graph_values = list(self.G.values())
        for i in range(self.n):
            temp = graph_values[i]
            reordered_graph[self.finish_time[i+1]] = [self.finish_time[vertex] for vertex in temp]   
        print("second dfs_loop initiated")
        self.dfs_loop(reordered_graph)
        print("second dfs_loop completed")
        print('Counting ')
        print( self.count_scc())

if __name__=="__main__":
    print('opening file')
    with open('SCC.txt') as f:
        G = [(int(line.split(' ')[0]), int(line.split(' ')[1])) for line in f]

    print('initialising kosaraju class')
    t = kosaraju(G,875714)
    print("performing algorithm")
    t.kosaraju_algo()
