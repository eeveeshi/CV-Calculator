limitedSProbs = [0.3467, 0.3664, 0.3861, 0.4058, 0.4255, 0.4452, 0.4650,
        0.4847, 0.5044, 0.5241, 0.5438, 0.5636, 0.5833, 0.6030, 0.6227, 0.6424,
        0.6621, 0.6819, 0.7015, 0.7213, 0.7410, 0.7705, 0.8001, 0.8297, 0.8593,
        0.8889, 0.9185, 0.9480,
        0.9776, 1.0072, 1.0367, 1.0663, 1.0959, 1.1255, 1.1550, 1.1847, 1.2142,
        1.2438, 1.2734, 1.3029, 1.3326, 1.3621, 1.3917, 1.4213, 1.4509, 1.4805,
        1.5100, 1.5396, 1.5692, 1.5988, 1.6284, 1.6579, 1.6875, 1.7171, 1.7467,
        1.7763, 1.8059, 1.8354, 1.8650, 1.8946, 1.9242, 1.9537, 1.9834, 2.0129,
        2.0426, 2.0721, 2.1017, 2.1312, 2.1609, 2.1904, 2.2200, 2.2496, 2.2792,
        2.3088, 2.3383, 2.3680, 2.3976, 2.4272, 2.4568, 2.4863, 2.5159, 2.5455,
        2.5751, 2.6047, 2.6342, 2.6638, 2.6934, 2.7230, 2.7526, 2.7822, 2.8118,
        2.8414, 2.8709]

cont = True
while cont:
    startLV = int(input("Starting Lucky Value?\n"))
    numRolls = int(input("Number of rolls?\n"))
    if not isinstance(startLV, int):
        print("Not an integer or not positive. Cannot compute")
        
    elif startLV + numRolls > 93:
        print("Not enough Lucky Value data yet!\n")
    
    else:        
        probOfNotSLimited = 1
        
        for i in range(numRolls):
            probOfNotSLimited *= (1-limitedSProbs[startLV+1]/100)
            
        print("Probability of S-limited in %d rolls, starting at %d Lucky Value: %0.02f%%\n" % (startLV, numRolls, 100-probOfNotSLimited*100))
        cont = not cont
