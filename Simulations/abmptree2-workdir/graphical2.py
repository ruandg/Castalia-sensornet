import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
import math
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
npx = [0 for i in range(0, numNodes)]
npy = [0 for i in range(0, numNodes)]
npz = [0 for i in range(0, numNodes)]

while cont < numNodes:
	npx[cont], it = getValueCoord(txt, it)
	npy[cont], it = getValueCoord(txt, it)
	npz[cont], it = getValueCoord(txt, it)
	#print npx[cont], npy[cont], npz[cont]

	cont += 1
#########################################################
#interf e distance
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def interf(ple, d0, pld0, sigma, pt, sen_tr, d):         #prob 95.44
    return pt - (pld0 + 10*ple*math.log10(d/d0) - sigma/2) >= sen_tr

##########################################################

#levando em consideracao que vou imprimir em papel preto/branco


# conseguir valore uteis em omnetpp.ini
NUM_OF_CHANNELS = 16
number_ch = 4
    #poreqnuanto estou setando os valores
ple = 2.4 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
pt = 0 #potencia de transmissao
sen_tr = -94 #sensibilidade do transceptor

##############################
plt.suptitle("Connections and Interferences in IWSN")
fl1 = fl2 = 0 #flags de legenda
for i in range(1, 5):
	for j in range(5, 53):
		if interf(ple, d0, pld0, sigma, pt, sen_tr, dist(npx[i], npy[i], npx[j], npy[j])):
			if  i*12 - 7 <= j <= i*12+5:
				plt.plot([npx[i], npx[j]], [npy[i], npy[j]], c='#000000', alpha = 0.3, label="connection" if fl1 == 0 else ""); fl1 = 1
			else:
				plt.plot([npx[i], npx[j]], [npy[i], npy[j]], 'r--', c="#000000", alpha = 0.1, label="interference" if fl2 == 0 else ""); fl2 = 1


circle1=patches.Circle((0,0),40, color='r', alpha=0.5)
plt.gcf().gca().add_artist(circle1)

plt.plot(npx[5:], npy[5:], 'ro', ms='8', c="#000000", alpha = 0.8, marker='1', label="sensor node")
plt.plot(npx[1:5], npy[1:5], 'ro', ms='12', c="#000000", alpha = 0.8, marker='H', label="router node")
plt.plot(npx[0], npy[0], 'ro', ms='12', c="#000000", alpha = 0.8, marker='$SN$', label="sink node")
plt.xlabel("position x axis")
plt.ylabel("position y axis")

plt.legend(loc = 3)
plt.minorticks_on()
plt.xticks(np.arange(-100, 101, 20.0))
plt.yticks(np.arange(-100, 101, 20.0))
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(linestyle=':', linewidth='0.5', color='black')



plt.draw()
plt.show()
