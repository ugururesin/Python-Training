# =============================================================================
# FIND THE 3 COORDINATES THAT CAN FORM A TRIANGLE THAT HAS THE MAXIMUM AREA!
# =============================================================================
array_x = [0,4]
array_y = [0,2,10]

sorted_x = sorted(array_x)
sorted_y = sorted(array_y)


# DEFINING A CLASS FOR XY COORDINATE
class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 


## HOLDS THE EXTREME POINTS AS p1 and p3
p1 = Point(min(sorted_x),min(sorted_y))
p3 = Point(max(sorted_x),max(sorted_y))


## CALCULATE THE AREAS for POSSIBLE MIDDLE POINTS (p2)
uplim = len(array_x) #assume array_x and array_y have same length!
arealist = [0]

for i in range(0,uplim):
    for j in range(0,uplim):
        p2 = Point(sorted_x[i],sorted_y[j])
        
        if p2.x != p1.x or p2.y != p1.y:
            if p2.x != p3.x or p2.y != p3.y:
                Area = 0.5*(p1.x*abs(p2.y-p3.y) + p2.x*abs(p3.y-p1.y) + p3.x*abs(p1.y-p2.y))
                print(f'For the p2 = {(p2.x,p2.y)}, the area = {Area}')
            
            if Area >= max(arealist):
                arealist.append(Area)
                if p2.x != p3.x or p2.y != p3.y:
                    p2_final = p2

print("\nThe maximum area is:",max(arealist))
print("The coordinate of the 1st point is:",(p1.x, p1.y))
print("The coordinate of the 2nd point is:",(p2_final.x, p2_final.y))
print("The coordinate of the 3rd point is:",(p3.x, p3.y))