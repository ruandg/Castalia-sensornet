import random

numNodes = 53
numRouters = 4
for i in range(0, numNodes):
    print "SN.node["+str(i)+"]."+"xCoor = "+str(random.uniform(-99, 99))
    print "SN.node["+str(i)+"]."+"yCoor = "+str(random.uniform(-99, 99))
    print "SN.node["+str(i)+"]."+"zCoor = 2"
