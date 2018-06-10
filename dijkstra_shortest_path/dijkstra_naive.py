#data structure {node: [(connecting node, connecting distance), .... .. ]}

graph = {}
with open('dijkstraData.txt') as f:
    i = 0
    
    for line in f:
    '''
    file in format of:
    node1\t node2,dist_to_node2 \t node3,dist_to_node_3..... \n
    node2\t .... 
    '''
        i+=1
        graph[i] = []
        new_item = line.split('\t')[1:] #all items but key
        for item in new_item:
            if item !='\n':
                graph[i].append((int(item.split(',')[0]), int(item.split(',')[1])))
                
n = len(graph)

#m*n implementation
def dijkstra(G,n=n):
    A = {} #visited nodes : shortest distance to node
    B={} # Computed shortest path
    for i in range(1,n+1):
        A[i] = 100000 # set defult shortest dist to 100000
        B[i] =set()
    nodes = set(range(1,n+1)) #unvisited node
    A[1] = 0 
 
    while nodes:
        minNode = None
        for node in nodes:
            if minNode is None:
                minNode = node
            elif A[node] < A[minNode]:
                minNode = node  

            for (next_node, node_distance) in G[minNode]:
                if minNode == 1:
                    dist_to_node = node_distance
                else:
                    dist_to_node = A[minNode]+ node_distance

                if next_node not in A or A[next_node] > dist_to_node:
                    A[next_node] = dist_to_node
                    B[next_node].add(minNode)
        nodes.remove(minNode)                    
       
    return A, B
    
'''
usage:
a,b = dijkstra(graph)
to find shortest distance from node 1 to node x:
a[x]
'''
