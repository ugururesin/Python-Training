# =============================================================================
# PYTHON PROGRAM TO CHECK IF RECTANGLES OVERLAP 
# =============================================================================
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
  
# Returns true if two rectangles(l1, r1)  
# and (l2, r2) overlap 
def doOverlap(l1, r1, l2, r2): 
      
    # If one rectangle is on left side of other 
    if(l1.x > r2.x or l2.x > r1.x): 
        return False
  
    # If one rectangle is above other 
    if(l1.y < r2.y or l2.y < r1.y): 
        return False
  
    return True
  
# Driver Code 
if __name__ == "__main__": 
    l1 = Point(0, 10) 
    r1 = Point(10, 0) 
    l2 = Point(0, 10) 
    r2 = Point(10, 0) 
  
    if(doOverlap(l1, r1, l2, r2)): 
        print("Rectangles Overlap") 
    else: 
        print("Rectangles Don't Overlap")


# =============================================================================
# RECTANGLE OVERLAP AREA CALCULATOR
# =============================================================================
''' Area = Height * Width 
    Area = dY * dX '''

# REC2 is the UPPER one
if (l1.y-r2.y) > 0:
    
    if(r1.x-l2.y) > 0:
        #REC2 is on RHS of REC1
        Area = (l1.y-r2.y)*(r1.x-l2.y)
    
    else:
        #REC2 is on LHS of REC1
        Area = (l1.y-r2.y)*(r2.x-l1.x)

# REC1 is the UPPER one
else:
    
    if (l2.y-r2.x) > 0:
        #REC2 is on LHS of REC1
        Area = (l2.y-r2.y)*(l1.x-r2.x)
    
    else:
        #REC2 is on RHS of REC1
        Area = (l2.y-r1.y)*(r1.x-l2.x)

if Area > 0:        
    print("The Overlapping Area: ",Area)
else:
    print("Rectangles Don't Overlap. Therefore no overlapped area!")