## graph data structure = {node: [(conn_node, conn_cost)...]....}

graph = {}
for i in range(1,501):
    graph[i] = []
# open and load file    
with open('edges.txt') as f:
    for line in f:
        
        new_edge =  line.split(' ')
        if len(new_edge) >2:            
            new_edge = list(map(int, new_edge))
            graph[new_edge[0]].append((new_edge[1], new_edge[2]))
            graph[new_edge[1]].append((new_edge[0], new_edge[2])) #undirected graph

# prims mst algo
def prims_algo(graph):
    cost = 0
    unseen = set(range(2,501)) # start from first node
    nodes = set([1])
    while unseen:
        edges = []
        for node in nodes:
            # get all crossing cuts from graph
            curr_edges = [(conn_node, conn_cost) for (conn_node, conn_cost) in graph[node] if conn_node not in nodes]
            edges.extend(curr_edges) 
        edges.sort(key = lambda x: x[1]) #sort by conn_cost
        cost+= edges[0][1]
        nodes.add(edges[0][0])
        unseen.remove(edges[0][0])

    return cost
    
'''
prims_algo(graph)
'''
