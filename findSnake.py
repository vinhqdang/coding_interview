# Given a 2D array of size nXn with values from 1 to n^2 permuted in the 2D array i.e no duplicates. 
# Find the longest snake in the array such that snake can go upward, downward, right, left and each and every adjacent value 
# in the snake should differ by 1. 
# Ex: 
# 2 5 6 
# 3 4 9 
# 1 7 8 
# Answer is 5. [2,3,4,5,6].

# http://www.careercup.com/question?id=5706557272621056

import random

N = 3

#generate array
arr = [i for i in range (N * N)]
visited = [False for i in range (N * N)]

random.shuffle (arr)

arr.append (-2)

def up (index):
	if (index >= N):
		return index - N
	else:
		return N*N

def down (index):
	if (index <= N*N - N - 1):
		return index + N
	else:
		return N*N

def left (index):
	if (index % N > 0):
		return index - 1
	else:
		return N*N

def right (index):
	if (index % N <= N - 1):
		return index + 1
	else:
		return N*N

longest = 0
logest_trace = list()
for i in range (N*N):
	curr_len = 0
	if (visited[i] == False):
		visited[i] = True
		curr_len += 1
		curr_index = i
		curr_list = list()
		curr_list.append (arr[curr_index])
		while (True):
			if (arr[curr_index] == arr[up(curr_index)] + 1):
				curr_len += 1
				curr_index = up(curr_index)
				curr_list.append (arr[curr_index])
				visited [curr_index] = True
				continue
			elif (arr[curr_index] == arr[down(curr_index)] + 1):
				curr_len += 1
				curr_index = down(curr_index)
				curr_list.append (arr[curr_index])
				visited [curr_index] = True
				continue
			elif (arr[curr_index] == arr[right(curr_index)] + 1):
				curr_len += 1
				curr_index = right(curr_index)
				curr_list.append (arr[curr_index])
				visited [curr_index] = True
				continue
			elif (arr[curr_index] == arr[left(curr_index)] + 1):
				curr_len += 1
				curr_index = left(curr_index)
				curr_list.append (arr[curr_index])
				visited [curr_index] = True
				continue
			else:
				break
		if (curr_len > longest):
			longest = curr_len
			logest_trace = curr_list

print arr
print '----'
print logest_trace
print '----'
print longest
