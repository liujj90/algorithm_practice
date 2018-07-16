with open('jobs.txt') as f:
    a = [line.split('\n')[0] for line in f][1:]
    b = {'weight':[], 'length':[], 'diff':[], 'div':[]}
    for x in a:
        b['weight'].append(int(x.split(' ')[0]))
        b['length'].append( int(x.split(' ')[1]) )
        b['diff'].append(int(x.split(' ')[0])- int(x.split(' ')[1])) # compute difference weight - length
        b['div'].append(int(x.split(' ')[0])/int(x.split(' ')[1]))# compute ratio weight/length
        
# df datastructure makes sorting easy
import pandas as pd
df = pd.DataFrame(b)
df2 = df.sort_values(['diff','weight'], ascending=[False, False]) # sort by diff and then weight, descending

# calculate completion times from ordered df (by diff)

len_sum = 0
comp_time = 0

for i in range(10000):
    curr_weight = df2['weight'].iloc[i]
    len_sum += df2['length'].iloc[i]
    comp_time += len_sum * curr_weight

# calculate completion times from ordered df (by div)
df3 = df.sort_values(['div','weight'], ascending=[False, False])
len_sum = 0
comp_time = 0

for i in range(10000):
    curr_weight = df3['weight'].iloc[i]
    len_sum += df3['length'].iloc[i]
    comp_time += len_sum * curr_weight
