## MAP & REDUCE
values = [1,2,3,4,5,6,7,8,9]

def get_squares(n):
    return n**2
    
    
def get_evens(n):
    return n%2 == 0
    
    
def multiply(x,y):
    return x*y


squares = list(map(get_squares, values))
print(squares)

evens = list(map(get_evens, values))
print(squares)


from functools import reduce
product = reduce(multiply, values)
print(product


## LAMBDA
squares = list(map(lambda x:x**2, values))
print(squares)

product = list(map(lambda x,y: x*y, values))
print(squares)