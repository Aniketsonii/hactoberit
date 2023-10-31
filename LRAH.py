--------
from math import ceil,log2;
	
# A utility function to get
# minimum of two numbers
def minVal(hist,x, y) :
	if x==-1:
		return y
	if y==-1:
		return x
	return x if (hist[x] < hist[y]) else y;
	
# A utility function to get the
# middle index from corner indexes.
def getMid(s, e) :
	return s + (e - s) // 2;
	
""" A recursive function to get the
minimum value in a given range
of array indexes. The following
are parameters for this function.
	
	st --> Pointer to segment tree
	index --> Index of current node in the
		segment tree. Initially 0 is
		passed as root is always at index 0
	ss & se --> Starting and ending indexes
				of the segment represented
				by current node, i.e., st[index]
	qs & qe --> Starting and ending indexes of query range """
def RMQUtil( hist,st, ss, se, qs, qe, index) :
	
	# If segment of this node is a part
	# of given range, then return
	# the min of the segment
	if (qs <= ss and qe >= se) :
		return st[index];
	
	# If segment of this node
	# is outside the given range
	if (se < qs or ss > qe) :
		return -1;
	
	# If a part of this segment
	# overlaps with the given range
	mid = getMid(ss, se);
	return minVal(hist,RMQUtil(hist,st, ss, mid, qs,
						qe, 2 * index + 1),
				RMQUtil(hist,st, mid + 1, se,
						qs, qe, 2 * index + 2));
	
# Return minimum of elements in range
# from index qs (query start) to
# qe (query end). It mainly uses RMQUtil()
def RMQ( hist,st, n, qs, qe) :
	
	# Check for erroneous input values
	if (qs < 0 or qe > n - 1 or qs > qe) :
		
		print("Invalid Input");
		return -1;
		
	return RMQUtil(hist,st, 0, n - 1, qs, qe, 0);
	
# A recursive function that constructs
# Segment Tree for array[ss..se].
# si is index of current node in segment tree st
def constructSTUtil(hist, ss, se, st, si) :
	
	# If there is one element in array,
	# store it in current node of
	# segment tree and return
	if (ss == se) :
	
		st[si] = ss;
		return st[si];
	
	# If there are more than one elements,
	# then recur for left and right subtrees
	# and store the minimum of two values in this node
	mid = getMid(ss, se);
	st[si] = minVal(hist,constructSTUtil(hist, ss, mid,
									st, si * 2 + 1),
					constructSTUtil(hist, mid + 1, se,
									st, si * 2 + 2));
		
	return st[si];
	
"""Function to construct segment tree
from given array. This function allocates
memory for segment tree and calls constructSTUtil()
to fill the allocated memory """
def constructST( hist, n) :
	
	# Allocate memory for segment tree
	
	# Height of segment tree
	x = (int)(ceil(log2(n)));
	
	# Maximum size of segment tree
	max_size = 2 * (int)(2**x) - 1;
	
	st = [0] * (max_size);
	
	# Fill the allocated memory st
	constructSTUtil(hist, 0, n - 1, st, 0);
	
	# Return the constructed segment tree
	return st;
	

#----------------------------------------------------------------

# main program
# Python3 program using Divide and Conquer
# to find maximum rectangular area under a histogram


def max_area_histogram(hist):
	area=0
	#initialize area
	
	st = constructST(hist, len(hist))
	# construct the segment tree
	
	try:
		# try except block is generally used in this way
		# to suppress all type of exceptions raised.
		
		def fun(left,right):
			
		# this function "fun" calculates area
		# recursively between indices left and right
			
			nonlocal area
			
			# global area won't work here as
			# variable area is defined inside function
			# not in main().
			
			if left==right:
				return
			
			index = RMQ(hist,st, len(hist), left, right-1)
			area=max(area,hist[index]*(right-left))
			# calculate area with minimum above
			
			fun(index+1,right)
			fun(left,index)
			# initiate further recursion
			
			return
				
		fun(0,len(hist))
		# initializes the recursion
		
		return(area)
		
	except:
		pass
	
# Driver Code
hist = [6, 2, 5, 4, 5, 1, 6]
print("Maximum area is",
	max_area_histogram(hist))
	
