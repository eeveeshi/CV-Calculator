calcSProbs = [1.4970, 1.5167, 1.5364, 1.5561, 1.5758, 1.5955, 1.6153,
1.6350, 1.6547, 1.6744, 1.6941, 1.7139, 1.7336, 1.7533, 1.7730, 1.7927,
1.8105, 1.8303, 1.8499, 1.8697, 1.8894, 1.9189, 1.9485, 1.9781, 2.0046,
2.0342, 2.0638, 2.0933, 2.1210, 2.1506, 2.1801, 2.2097, 2.2393, 2.2689,
2.2984, 2.3281, 2.3576, 2.3872, 2.4168, 2.4444, 2.4741, 2.5036, 2.5332,
2.5597, 2.5893, 2.6189, 2.6484, 2.6780, 2.7076, 2.7353, 2.7649, 2.7944,
2.8240, 2.8536, 2.8832, 2.9128, 2.9424, 2.9719, 3.0015, 3.0311, 3.0588,
3.0883, 3.1149, 3.1444, 3.1741, 3.2036, 3.2332, 3.2627, 3.2924, 3.3219,
3.3515, 3.3792, 3.4088, 3.4384, 3.4679, 3.4976, 3.5272, 3.5568, 3.5864,
3.6159, 3.6455, 3.6701, 3.6997, 3.7293, 3.7588, 3.7884, 3.8180, 3.8476,
3.8772, 3.9068, 3.9364, 3.9660, 3.9936]

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
            probOfNotS *= (1-calcSProbs[startLV+i]/100)
            
        print("Probability of S-limited in %d rolls using calculated values, starting at %d Lucky Value: %0.02f%%\n" % (numRolls, startLV, 100-probOfNotS*100))
        cont = not cont
