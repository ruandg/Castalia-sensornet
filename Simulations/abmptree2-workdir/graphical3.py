import numpy as np
import matplotlib.pyplot as plt
import sys
import math
from mpl_toolkits.axes_grid1 import make_axes_locatable

###################### UTILITARIOS ######################

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#2*sigma interfere com 98% de probabilidade
#0*sigma interfere com 50% de probablidade
def interf(ple, d0, pld0, sigma, pt, sen_tr, x1, y1, x2, y2):
    return node_reach(ple, d0, pld0, sigma, pt, sen_tr) >= dist(x1, y1,x2, y2)

def node_reach(ple, d0, pld0, sigma, pt, sen_tr):
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

clusterID = map(int, raw_input().split(' '))
clusterID = map(lambda x: x-1, clusterID)


#FACILITANDO OS TESTES
if len(sys.argv) <= 2:
    print "sem potencia\nsem clusterID"
    pTRS = [0 for i in range(0, numNodes)]
    for i in range(5, 17): clusterID[i] = 0;
    for i in range(17, 29): clusterID[i] = 1;
    for i in range(29, 41): clusterID[i] = 2;
    for i in range(41, 53): clusterID[i] = 3;
else:
    if (len(sys.argv) == 3):
        if (sys.argv[2] == 'p'):
            print "com potencia\nsem clusterID"
            for i in range(5, 17): clusterID[i] = 0;
            for i in range(17, 29): clusterID[i] = 1;
            for i in range(29, 41): clusterID[i] = 2;
            for i in range(41, 53): clusterID[i] = 3;
        else:
            print "com clusterId\nsem potencia"
            pTRS = [0 for i in range(0, numNodes)]
    else:
        print "com potencia\ncom clusterId"


print(clusterID)

####### SETANDO VALORES DE SIMULACAO MANUALMENTE #######
NUM_OF_CHANNELS = 16
number_ch = 4
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
sen_tr = -94 #sensibilidade do transceptor

##################### INICIANDO PRINT #################
# * levando em consideracao impressao preto/branco
plt.suptitle("Connections and Interferences in IWSN")
fl1 = fl2 = 0 #flags de legenda
for i in range(1, 5): 
    for j in range(5, 53):
        if clusterID[j] != i-1: #interfere acima de 50%
            if interf(ple, d0, pld0, 0*sigma, pTRS[j], sen_tr, npx[i], npy[i], npx[j], npy[j]):
                plt.plot([npx[i], npx[j]], [npy[i], npy[j]], 'r--', c="#000000", alpha = 0.1, label="p(interference) >= 50%" if fl2 == 0 else ""); fl2 = 1
        else: #conecta acima de 98%
            if interf(ple, d0, pld0, 2*sigma, pTRS[j], sen_tr, npx[i], npy[i], npx[j], npy[j]):
                plt.plot([npx[i], npx[j]], [npy[i], npy[j]], c='#000000', alpha = 0.3, label="p(connection) >= 98%" if fl1 == 0 else ""); fl1 = 1

#yellow - router 1
plt.plot(npx[1], npy[1], 'ro', ms='12', c="yellow", alpha = 0.8, marker='H', label="router node 1")
#red    - router 2
plt.plot(npx[2], npy[2], 'ro', ms='12', c="red", alpha = 0.8, marker='H', label="router node 2")
#blue   - router 3
plt.plot(npx[3], npy[3], 'ro', ms='12', c="blue", alpha = 0.8, marker='H', label="router node 3")
#green  - router 4
plt.plot(npx[4], npy[4], 'ro', ms='12', c="green", alpha = 0.8, marker='H', label="router node 4")


plt.axis([min(npx)-15, max(npx)+15, min(npy)-15, max(npy)+15])
for i in range(5, numNodes):
    if clusterID[i] == 0: cor = 'yellow';
    if clusterID[i] == 1: cor = 'red';
    if clusterID[i] == 2: cor = 'blue';
    if clusterID[i] == 3: cor = 'green';
    #plt.plot(npx[i], npy[i], 'ro', ms='12', c=cor, alpha = 0.8, marker='$'+str(i%10)+'$')
    plt.plot(npx[i], npy[i], 'ro', ms='12', c=cor, alpha = 0.8, marker='1')


plt.plot(npx[0], npy[0], 'ro', ms='12', c="#000000", alpha = 0.8, marker='$SN$', label="sink node")
plt.xlabel("position x axis")
plt.ylabel("position y axis")
from matplotlib.font_manager import FontProperties
plt.legend(bbox_to_anchor=(1.04,1), loc="upper left")

plt.draw()
plt.savefig(sys.argv[1]+'.png', bbox_inches="tight")