#the experiment is following:
#for each time, get 1 sample uniformly from n collection (1 .. n)
#what is the average number of times need to get samples from all collection

import numpy as np

#run with n from 10 to 200
for n in range (10, 200):
	#run experiment 1000 times
	counts = [0] * 1000
	for exp_id in range (1000):
		visited = [False] * n
		count = 0
		while (False in visited):
			visit = np.random.randint (1, n + 1)
			visited [visit - 1] = True
			count += 1
		counts [exp_id] = count

	print "n = " + str (n) + ": average times = " + str (float (sum(counts)) / len (counts))
