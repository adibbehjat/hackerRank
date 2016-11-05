# Collect rows, columns and tracks
n,m,k = [int(x) for x in raw_input().strip().split()]

# Train map will contain a 2-Dimensional map
# e.g. a 2x2 map will be represented as:
# {1:{map:[a,b],spots:Int},2:{map:[c,d],spots:Int}}
train_map = {}

# To process the map, we will use 0 to represent available
# post for lamppost, and 1 to represent occupied track

# Examine the tracks from input
for tracks in xrange(k):
	# Identify the row, starting column, and ending column 
	row,col_s,col_e = [int(x) for x in raw_input().strip().split()]
	
	# Switch index where necessary
	if col_e < col_s:
		col_s,col_e = col_e,col_s

	# Transform data into index	
	i = col_s - 1
	row = row - 1
	
	# Modify train_map based on the new collected information
	if row not in train_map:
		train_map[row] = {'map':[0]*m,'spots':0}
	train_map[row]['map'][i:col_e] = [1] * (col_e  - i)
	train_map[row]['spots'] = sum(train_map[row]['map'])

print n*m - sum([train_map[x]['spots'] for x in train_map])

"""
Prompt: https://www.hackerrank.com/challenges/gridland-metro

Note: A train track may (or may not) overlap other train tracks within the same row.

Sample Input

4 4 3
2 2 3
3 1 4
4 4 4

Sample output:
9
"""