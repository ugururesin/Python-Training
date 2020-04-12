## FIND THE PAIR WHOSE SUM IS CLOSEST TO THE TARGET VALUE

# x and y are the given lists, and target is the target sum.
# The output should be a tuple of two integers

def closest_sum_pair(x, y, target):
    x_sorted = sorted(x)
    y_sorted = sorted(y)
    
    i = 0
    j = len(y_sorted) - 1
    
    smallest_dif = abs(x_sorted[0] + y_sorted[0] - target)
    closest_pair = (x_sorted[0], y_sorted[0])
    
    while i < len(x_sorted) and j >= 0:
        v1 = x_sorted[i]
        v2 = y_sorted[j]
        current_dif = v1 + v2 - target
        
        if abs(current_dif) < smallest_dif:
            smallest_dif = abs(current_dif)
            closest_pair = (v1, v2)

        if current_dif == 0:
            return closest_pair
        
        elif current_dif < 0:
            i += 1
        else:
            j -= 1
    
    return closest_pair

# NOTE: You can use the following values to test this function.
a1 = [-1, 3, 8, 2, 9, 5]
a2 = [4, 1, 2, 10, 5, 20]
a_target = 18
closest_sum_pair(a1, a2, a_target) #should return (8, 10)