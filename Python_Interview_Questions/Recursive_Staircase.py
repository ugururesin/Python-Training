'''RECURSIVE STAIRCASE PROBLEMS

PROBLEM-1:
N (Given): Number of steps in staircase
Suppose you can take only 1 or 2 steps at a time

Write a function:
    num_ways(N)
    returns number of possible ways to reach top from the bottom 
    
    e.g. for N=2
    #1: you can reach the top 1+1 steps
    #2: you can reach the top a 2 step
    
    thus num_ways(2)=2
    
Solution: Dynamic Programming (Bottom-Up Approach)'''

# Recurssive program to find n'th fibonacci number 
def fib(n): 
    if n <= 1: 
        return n 
    return fib(n-1) + fib(n-2) 
  
# returns no. of ways to reach s'th stair 
def countWays(s): 
    return fib(s + 1) 
  
# Driver program 
s = 4
print ("Number of ways = ",countWays(s))
  
    
''' PROBLEM-2:
    Find num_ways(N,X)  
    X is the set of 'allowed steps' '''


# Recursive function used by countWays 
def countWaysUtil(n,m): 
	res = [0 for x in range(n)] # Creates list res witth all elements 0 
	res[0],res[1] = 1,1
	
	for i in range(2,n): 
		j = 1
		while j<=m and j<=i: 
			res[i] = res[i] + res[i-j] 
			j = j + 1
	return res[n-1] 

# Returns number of ways to reach s'th stair 
def countWays(s,m): 
	return countWaysUtil(s+1, m) 
	
# Driver Program 
s,m = 4,2
print("Number of ways =",countWays(s,m))


def getFactorial(n):
    if n<2:
        return 1
    else:
        return n*getFactorial(n-1)