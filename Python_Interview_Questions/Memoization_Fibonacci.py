# =============================================================================
# MEMOIZATION-1 (MANUALLY)
# =============================================================================
fibonacci_cache = {}

def fibonacci(n):
    #If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    #Compute the Nth term
    if n<=2:
        value =1
    elif n>2:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    #Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1,1001):
    print(n,":",fibonacci(n))
    

# =============================================================================
# ## MEMOIZATION-2 (USING LIBRARY: lru_cache)
# =============================================================================
from functools import lru_cache #lru:"least recently used"

@lru_cache(maxsize=1000) #default maxsize=128
def fibonacci(n):
    #Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n<1:
        raise ValueError("n must be a positive int")
    
    #Compute the Nth term
    if n<=2:
        return 1
    elif n>2:
        return fibonacci(n-1) + fibonacci(n-2)
    
for n in range(1,501):
    print(n,":",fibonacci(n+1)/fibonacci(n))