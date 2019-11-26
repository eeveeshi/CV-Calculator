dispSProbs = [1.50, 1.52, 1.54, 1.56, 1.58, 1.60, 1.62, 1.64, 1.66, 1.68,
1.70, 1.72, 1.74, 1.76, 1.78, 1.80, 1.82, 1.84, 1.86, 1.88, 1.90, 1.93,
1.96, 1.99, 2.02, 2.05, 2.08, 2.11, 2.14, 2.17, 2.20, 2.23, 2.26, 2.29,
2.32, 2.34, 2.37, 2.40, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64,
2.67, 2.70, 2.73, 2.76, 2.79, 2.82, 2.85, 2.88, 2.91, 2.94, 2.97, 3.00,
3.03, 3.06, 3.09, 3.12, 3.15, 3.18, 3.21, 3.23, 3.26, 3.29, 3.32, 3.35,
3.38, 3.41, 3.44, 3.47, 3.50, 3.53, 3.56, 3.59, 3.62, 3.65, 3.68, 3.71,
3.74, 3.77, 3.80, 3.83, 3.86, 3.89, 3.92, 3.95, 3.98, 4.01, 4.04]

cont = True
while cont:
    startLV = int(input("Starting Lucky Value?\n"))
    numRolls = int(input("Number of rolls?\n"))
    if not isinstance(startLV, int):
        print("Not an integer or not positive. Cannot compute")
        
    elif startLV + numRolls > 93:
        print("Not enough Lucky Value data yet!\n")
    
    else:        
        probOfNotS = 1
        
        for i in range(numRolls):
            probOfNotS *= (1-dispSProbs[startLV+1]/100)
            
        print("Probability of S-limited in %d rolls using in-game displayed values, starting at %d Lucky Value: %0.02f%%\n" % (numRolls, startLV, 100-probOfNotS*100))
        cont = not cont
