import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable

###################### UTILITARIOS ######################

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def interf(ple, d0, pld0, sigma, pt, sen_tr, d):
    return pt - (pld0 + 10*ple*math.log10(d/d0) + sigma) >= sen_tr

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

clusterID = map(int, raw_input().split(' '))
clusterID = map(lambda x: x-1, clusterID)

####### SETANDO VALORES DE SIMULACAO MANUALMENTE #######
NUM_OF_CHANNELS = 16
number_ch = 4
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
pt = 0 #potencia de transmissao
sen_tr = -94 #sensibilidade do transceptor

##################### INICIANDO PRINT #################
# * levando em consideracao impressao preto/branco
plt.suptitle("Connections and Interferences in IWSN")
fl1 = fl2 = 0 #flags de legenda
for i in range(1, 5): 
	for j in range(5, 53):       #interfere acima de 50%
		if interf(ple, d0, pld0, 0*sigma, pTRS[j], sen_tr, dist(npx[i], npy[i], npx[j], npy[j])):
			if  clusterID[j] != i:
				plt.plot([npx[i], npx[j]], [npy[i], npy[j]], 'r--', c="#000000", alpha = 0.1, label="interference" if fl2 == 0 else ""); fl2 = 1
		if clusterID[j] == i:
				plt.plot([npx[i], npx[j]], [npy[i], npy[j]], c='#000000', alpha = 0.3, label="connection" if fl1 == 0 else ""); fl1 = 1

plt.axis([min(npx)-5, max(npx)+5, min(npy)-5, max(npy)+5])
plt.plot(npx[5:], npy[5:], 'ro', ms='8', c="#000000", alpha = 0.8, marker='1', label="sensor node")
plt.plot(npx[1:5], npy[1:5], 'ro', ms='12', c="#000000", alpha = 0.8, marker='H', label="router node")
plt.plot(npx[0], npy[0], 'ro', ms='12', c="#000000", alpha = 0.8, marker='$SN$', label="sink node")
plt.xlabel("position x axis")
plt.ylabel("position y axis")
plt.legend(loc = 3)

plt.draw()
plt.savefig(sys.argv[1]+'.png')