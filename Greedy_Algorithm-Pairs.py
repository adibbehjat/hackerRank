
def pairs(a,k):
	a.sort()
	answer = 0
	i,j = 0,1
	while i < len(a) - 1:
		
		# Match the correct answer
		if a[j] - a[i] == k:
			answer += 1

		elif a[j] - a[i] > k:
			i += 1
			j = i
		
		j += 1
			
		if j > len(a) - 1:
			i += 1
			j = i + 1
		
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