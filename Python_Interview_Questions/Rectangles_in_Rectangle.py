## THERE ARE 2 RECTANGLES
# THE EDGES of THE BIGGER RECTANGLE is (x,y)
# THE EDGES of THE SMALLER RECTANGLE is (a,b)
# FIND OUT HOW MANY SMALL ONES WE CAN PUT IN THE BIG

'''     big_rec = (x,y)     # x>=y
        small_rec = (a,b)   # a>=b '''

def rectangle_fitter(big_rec,small_rec):
    
    proportion = []
    
    for i in range(len(big_rec)):
        proportion.append(big_rec[0]/ small_rec[i])
        proportion.append(big_rec[1]/ small_rec[i])
    
    p = proportion
    
    '''REMINDER 
    p[0] #x/a
    p[1] #y/a
    p[2] #x/b
    p[3] #y/b '''
    
    case1 = int(p[0])*int(p[3])
    case2 = int(p[1])*int(p[2])
    return max(case1, case2)

# TEST
rectangle_fitter((10,10),(5,5)) #should return 4
rectangle_fitter((20,10),(5,5)) #should return 8
rectangle_fitter((33,17),(5,4)) #should return 24
rectangle_fitter((5,5),(10,10)) #should return 0