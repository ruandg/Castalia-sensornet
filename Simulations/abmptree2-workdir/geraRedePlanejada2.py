import random
#roteadores tem 15DBM
numNodes = 53
numRouters = 4
x = 85
y = 40

print "SN.node[0]."+"xCoor = 0"
print "SN.node[0]."+"yCoor = 0"
print "SN.node[0]."+"zCoor = 2"
print "SN.node[1]."+"xCoor = "+str(-y+10)
print "SN.node[1]."+"yCoor = "+str(-y-22)
print "SN.node[1]."+"zCoor = 2"
print "SN.node[2]."+"xCoor = "+str(y-15)
print "SN.node[2]."+"yCoor = "+str(y+4)
print "SN.node[2]."+"zCoor = 2"
print "SN.node[3]."+"xCoor = "+str(-y+25)
print "SN.node[3]."+"yCoor = "+str(y+5)
print "SN.node[3]."+"zCoor = 2"
print "SN.node[4]."+"xCoor = "+str(y-35)
print "SN.node[4]."+"yCoor = "+str(-y+40)
print "SN.node[4]."+"zCoor = 2"

for i in range(0, 12):
    print "SN.node["+str(i+5)+"]."+"xCoor = "+str(random.uniform(-x+40, -y+40))
    print "SN.node["+str(i+5)+"]."+"yCoor = "+str(random.uniform(-x+5, -y+5))
    print "SN.node["+str(i+5)+"]."+"zCoor = 2"

for i in range(0, 12):
    print "SN.node["+str(i+17)+"]."+"xCoor = "+str(random.uniform(x-30, y-30))
    print "SN.node["+str(i+17)+"]."+"yCoor = "+str(random.uniform(x-15, y-15))
    print "SN.node["+str(17+i)+"]."+"zCoor = 2"

for i in range(0, 12):
    print "SN.node["+str(i+29)+"]."+"xCoor = "+str(random.uniform(-x+70, -y+50))
    print "SN.node["+str(i+29)+"]."+"yCoor = "+str(random.uniform(x-15, y-15))
    print "SN.node["+str(29+i)+"]."+"zCoor = 2"

for i in range(0, 12):
    print "SN.node["+str(i+41)+"]."+"xCoor = "+str(random.uniform(x-55, y-55))
    print "SN.node["+str(i+41)+"]."+"yCoor = "+str(random.uniform(-x+60, -y+60))
    print "SN.node["+str(41+i)+"]."+"zCoor = 2"