import numpy as np

def findGap_n( x_key_indcies, X_rBound , n):
    previous_x = X_rBound
    GapFound = False
    index_ = -1
    x = 0

    X_lBound = 0
    Y_lBound = 0

    while not GapFound and index_ *-1 < len(x_key_indcies)/2:
        index_ -= 1
        x = x_key_indcies[index_][0]

        if abs(previous_x-x) > n:
            X_lBound = x_key_indcies[index_+1][0]
            Y_lBound = x_key_indcies[index_+1][1]
            GapFound = True
        else:
            previous_x = x
            
    return X_lBound, Y_lBound



def CreateRightLineEquation(image_key):
    key_indecies = []
    key_arr = np.array(image_key)

    for i in range(0,len(image_key)):
        for j in range(0,len(image_key[0])):

            pixel = key_arr[i, j]

            if pixel ==  1:
                #mark its index
                pixel_index = (j, i)
                key_indecies.append(pixel_index)

    x_key_indcies = (sorted(key_indecies, key = lambda x: x[0]))
    y_key_indcies = (sorted(key_indecies, key = lambda x: x[1]))


    #find the max X
    X_rBound = x_key_indcies[-1][0]
    Y_rBound = x_key_indcies[-1][1]

    #find first gap > 5 pixels moving from max x dirrection
    
    X_lBound = 0
    Y_lBound = 0
    Gap_size = 5
    
    while Gap_size > 2 and  X_lBound == 0 and  Y_lBound == 0:
        X_lBound, Y_lBound = findGap_n(x_key_indcies, X_rBound, Gap_size)
        Gap_size -= 1
    
    
    #error checking
    if X_lBound  == 0 or Y_lBound == 0:
        print("!!Error!! edges not found end set to mid point", X_lBound, Y_lBound)
        #print(x_key_indcies)
        indi = int(len(x_key_indcies)/2)
        X_lBound = x_key_indcies[indi *-1][0]
        Y_lBound =x_key_indcies[indi *-1][1]
        
        
        
    elif X_lBound == X_rBound:
        print("!! Error !! No gap found setting end to highest point")
        print(x_key_indcies)
        X_lBound = y_key_indcies[-1][0]
        Y_lBound = y_key_indcies[-1][1]



    #create the slope 
    print("Left Bound: ({},{})".format(X_lBound, Y_lBound))
    print("Rigth Bound: ({},{})".format(X_rBound, Y_rBound))
    
    #find the angle 
    x_leg = X_rBound-X_lBound
    y_leg = Y_lBound- Y_rBound
    angle = np.degrees(np.arctan(y_leg/x_leg))
    print("line angle {:.2f} degrees".format(angle))
    
    slope =  ( Y_rBound - Y_lBound ) / (X_rBound - X_lBound)
    b = Y_rBound - (slope)*X_rBound
    print("vector Equation")
    print("Slope: {:.2f}".format(slope))
    print("B intercept: {:.2f}".format(b))
    x_steps = np.arange(X_lBound, X_rBound)
    line = slope * x_steps +b
    
    
    return slope, b, X_lBound, Y_lBound,  X_rBound, Y_rBound
