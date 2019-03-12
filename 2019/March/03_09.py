# This problem was asked by Google.
#
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each
# subarray of length k.
#
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:
#
# 10 = max(10, 5, 2)
# 7 = max(5, 2, 7)
# 8 = max(2, 7, 8)
# 8 = max(7, 8, 7)
# Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the
# results. You can simply print them out as you compute them.


from collections import deque


# My solution
def max_value_subarray(k, array):
	highest_num_per_subarray = []
	counter = 0
	highest_num = []
	for i in range(len(array)):
		for j in range(i, k):
			if j < k:
				counter += 1
				highest_num.append(array[j])
			else:
				counter = 0
				highest_num_per_subarray.append(max(highest_num))


# DailyCoding Solution
def max_of_subarrays_1(lst, k):
	for i in range(len(lst) - k + 1):
		print(max(lst[i:i + k]))


def max_of_subarrays_2(lst, k):
	q = deque()
	for i in range(k):
		while q and lst[i] >= lst[q[-1]]:
			q.pop()
		q.append(i)

	# Loop invariant: q is a list of indices where their corresponding values are in descending order.
	for i in range(k, len(lst)):
		print(lst[q[0]])
		while q and q[0] <= i - k:
			q.popleft()
		while q and lst[i] >= lst[q[-1]]:
			q.pop()
		q.append(i)
	print(lst[q[0]])


