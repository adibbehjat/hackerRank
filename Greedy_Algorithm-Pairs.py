def pairs(a,k):
	
    a.sort()
	
    answer = 0
	
    i,j = 0,1

	while j < len(a):
		
        # Collect difference
        dif = a[j] - a[i]

		# Select path based on dif outcome
		if dif == k:
			answer += 1
			j += 1

		elif dif > k:
			i += 1

		else:
			j += 1
		
	#a contains array of numbers and k is the value of difference
	return answer

# Tail starts here
if __name__ == '__main__':
	a = map(int, raw_input().strip().split(" "))
	_a_size=a[0]
	_k=a[1]
	b = map(int, raw_input().strip().split(" "))
	print pairs(b,_k)


"""
Prompt:

Given N integers, count the number of pairs of integers whose difference is K.

Sample Input:

5 2
1 5 3 4 2

-- Explanation:
5 = size of array (N)
2 = difference (K)
Array = array of N integers



Sample Output:

3

"""