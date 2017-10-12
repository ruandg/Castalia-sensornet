import numpy as np
import matplotlib.pyplot as plt
import sys
from mpl_toolkits.axes_grid1 import make_axes_locatable

#########################################################
# getting points from topology in omnetpp.ini
def getValueCoord(txt, it):
	it = txt.find("=", it) + 2
	value = ""
	while txt[it] != '\n':
		value += txt[it]
		it += 1
	return float(value), it

#ler a topologia
if len(sys.argv) != 2:
	exit()

top = sys.argv[1]
print "Topologia: " + top

FILE = open("omnetpp.ini", "r")
txt = FILE.read()
output = txt

it = txt.find("Config "+top, 4300)
if it != -1:
	print "\ttopologia encontrada"
else:
	print "\ttopologia nao encontrada"
	exit()

numNodes = 53
cont = 0
node_position_x = [0 for i in range(0, numNodes)]
node_position_y = [0 for i in range(0, numNodes)]
node_position_z = [0 for i in range(0, numNodes)]

while cont < numNodes:
	node_position_x[cont], it = getValueCoord(txt, it)
	node_position_y[cont], it = getValueCoord(txt, it)
	node_position_z[cont], it = getValueCoord(txt, it)
	#print node_position_x[cont], node_position_y[cont], node_position_z[cont]

	cont += 1
#########################################################
#interf e distance
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def interf(ple, d0, pld0, sigma, pt, sen_tr, d):         #prob 95.44
    return pt - (pld0 + 10*ple*math.log10(d/d0) - sigma/2) >= sen_tr

##########################################################
fig, axScatter = plt.subplots()

# the scatter plot:
axScatter.scatter(node_position_x[5:], node_position_y[5:], s=50, c="red", alpha = 0.5, marker='1', label="sensor node")
axScatter.scatter(node_position_x[1:5], node_position_y[1:5], s=100, c="blue", alpha = 0.5, marker='1', label="sink node")
axScatter.scatter(node_position_x[0], node_position_y[0], s=150, c="green", alpha = 0.5, marker='1', label="router node")
axScatter.set_aspect(1)
plt.xlabel("position x axis")
plt.ylabel("position y axis")
plt.legend(loc = 3)

for i in range(1, 5):
    for j in range(5, 53):
    		if interf(i, j)


plt.draw()
plt.show()