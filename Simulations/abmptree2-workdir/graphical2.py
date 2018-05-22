import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import sys
import math
import smallestEnclosingCircle
from mpl_toolkits.axes_grid1 import make_axes_locatable

###################### UTILITARIOS ######################

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def interf(ple, d0, pld0, sigma, pt, sen_tr, d):
    return pt - (pld0 + 10*ple*math.log10(d/d0) + sigma) >= sen_tr

def router_reach(ple, d0, pld0, sigma, pt, sen_tr):
    return 10**( (sen_tr - pt + sigma + pld0)/(-10*ple) + math.log10(d0) )

############## INICIALIZACAO ###############
numNodes = 53
cont = 0
npx = [0 for i in range(0, numNodes)]
npy = [0 for i in range(0, numNodes)]
npz = [0 for i in range(0, numNodes)]
clusterID = [0 for i in range(0, numNodes)]
pTRS = [0 for i in range(0, numNodes)]


############## LEITURA ###############
cont = 0
while True:
    inp = raw_input()
    if inp.strip() == "*":
        break
    for i in range(0, len(inp)):
        if inp[i] == '=':
            if cont%3 == 0: #x
                npx[cont/3] = float(inp[i+2:])
            elif cont%3 == 1: #y
                npy[cont/3] = float(inp[i+2:])
            else: #z
                npz[cont/3] = float(inp[i+2:])
            break
    cont = cont + 1

cont = 0
while True:
    inp = raw_input()
    if inp.strip() == "*":
        break
    for i in range(0, len(inp)):
        if inp[i] == '=':
            pTRS[cont] = float(inp[i+3:-4])
            break
    cont = cont + 1
pTRS = [0 for i in range(0, numNodes)]

clusterID = map(int, raw_input().split(' '))
clusterID = map(lambda x: x-1, clusterID)

####### SETANDO VALORES DE SIMULACAO MANUALMENTE #######
NUM_OF_CHANNELS = 16
number_ch = 4
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
pt = 7.5 #potencia de transmissao
sen_tr = -94 #sensibilidade do transceptor

##################### INICIANDO PRINT #################
plt.suptitle("Connections and Interferences in IWSN")
fl1 = fl2 = 0 #flags de legenda
for i in range(1, 5): 
	for j in range(5, 53): #interfere acima de 50% (0*sigma)
		if interf(ple, d0, pld0, 0*sigma, pTRS[j], sen_tr, dist(npx[i], npy[i], npx[j], npy[j])):
			if  clusterID[j] != i:
				plt.plot([npx[i], npx[j]], [npy[i], npy[j]], 'r--', c="#000000", alpha = 0.1, label="interference" if fl2 == 0 else ""); fl2 = 1
		if clusterID[j] == i:
				plt.plot([npx[i], npx[j]], [npy[i], npy[j]], c='#000000', alpha = 0.3, label="connection" if fl1 == 0 else ""); fl1 = 1


#SEC algorithm to get position of sink node
sn_pos = smallestEnclosingCircle.make_circle(zip(npx[5:], npy[5:]))
circle1=patches.Circle((sn_pos[0],sn_pos[1]),sn_pos[2], color='g', alpha=0.5)
plt.gcf().gca().add_artist(circle1)

#area of router nodes             #o alcance ta durante 95% do tempo
radius = router_reach(ple, d0, pld0, 2*sigma, pTRS[1], sen_tr)
for i in range(1, 5):
    circle1=patches.Circle((npx[i],npy[i]), radius, color='r', alpha=0.5)
    plt.gcf().gca().add_artist(circle1)

#ploting points
plt.plot(npx[5:], npy[5:], 'ro', ms='8', c="#000000", alpha = 0.8, marker='1', label="sensor node")
plt.plot(npx[1:5], npy[1:5], 'ro', ms='12', c="#000000", alpha = 0.8, marker='H', label="router node")
plt.plot(npx[0], npy[0], 'ro', ms='12', c="#000000", alpha = 0.8, marker='$SN$', label="sink node")

#grid format
plt.xlabel("position x axis")
plt.ylabel("position y axis")
plt.legend(loc = 3)
plt.minorticks_on()
plt.xticks(np.arange(-100, 101, 20.0))
plt.yticks(np.arange(-100, 101, 20.0))
plt.gca().set_aspect('equal', adjustable='box')
plt.grid(linestyle=':', linewidth='0.5', color='black')

#printing
plt.draw()
plt.savefig(sys.argv[1]+'.png')