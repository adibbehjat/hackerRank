# Enter your code here. Read input from STDIN. Print output to STDOUT

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
		continue
		col_s,col_e = col_e,col_s

	# Transform data into index	
	col_s = col_s - 1
	row = row - 1
	
	# Modify train_map based on the new collected information
	if row not in train_map:
		train_map[row] = {'map':[0]*m}
	train_map[row]['map'][i:col_e] = [1] * (col_e  - col_s)

# Total space available
total = n*m

for row in train_map:
    total -= sum(train_map[row]['map'])
    
print total

"""

NEW METHOD

"""



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