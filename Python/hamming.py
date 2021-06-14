def distance(strand_a, strand_b):
	if len(strand_a)!=len(strand_b):
		raise ValueError("Both strand_a and strand_b must of the same length!")
	
	hamming_dist=0
	for i in range(len(strand_a)):
		if strand_a[i]!=strand_b[i]:
			hamming_dist += 1
	return hamming_dist
