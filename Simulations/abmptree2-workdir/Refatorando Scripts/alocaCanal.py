import math
import Queue as Q

#verifica se ha interferencia
def interf(ple, d0, pld0, sigma, pt, sen_tr, d):
    return pt - (pld0 + 10*ple*math.log10(d/d0) + sigma) >= sen_tr
#verifica a distancia
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#constantes necessarias
numNodes = 27
cont = 0
npx = [0 for i in range(0, numNodes)]
npy = [0 for i in range(0, numNodes)]
npz = [0 for i in range(0, numNodes)]
pTRS = [0 for i in range(0, numNodes)]
clusterID = [0 for i in range(0, numNodes)]
NUM_OF_CHANNELS = 16
numRouters = 4 #NUMERO DE ROTEADORES
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
pt = 0 #potencia de transmissao
sen_tr = -94 #sensibilidade do transceptor

numSensors = numNodes - numRouters - 1


#LER npx, npy, pTRS, clusterID
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
print(clusterID)

###### ESCOLHENDO QUAL CANAL PERTENCE A QUAL ROTEADOR #######
# criando o grafo
G = [[0 for i in range(0, numRouters)] for j in range(0, numRouters)]

for i in range(0, numSensors):
    for j in range(0, numRouters):
        if clusterID[i + numRouters + 1] == j:
            continue     #+50% do tempo
        if interf(ple, d0, pld0, 0*sigma, pTRS[i], sen_tr, 
                  dist(npx[i + numRouters + 1], npy[i + numRouters + 1], npx[j+1], npy[j+1])):
            G[clusterID[i + numRouters + 1]][j] = G[j][clusterID[i + numRouters + 1]] = 1

# alocando canais de forma inteligente
degrees = [0 for i in range(0, numRouters)]
used = [0 for i in range(0, numRouters)]

q = Q.PriorityQueue()
channels = [[False for i in range(0, NUM_OF_CHANNELS)] for j in range(0, numRouters)]

for i in range(0, numRouters):
    for j in range(0, numRouters):
        if G[i][j]:
            degrees[j] += 1

for i in range(0, numRouters):
    q.put((-degrees[i], -i)) #REVERSE PRIORITY QUEUE

INTERF = [0 for i in range(0, numRouters)]

while not q.empty():
    act = q.get()
    used[-act[1]] = 1
    f = 0 #quantity of interference nodes
    u = 0 #quantity of sub-redes on INTERF already calc

    for i in range(0, numRouters):
        if G[-act[1]][i]:
            INTERF[f] = i #-act[1] interefere com i
            f += 1        #1 intereferencia a mais
            if used[i]:
                u += 1    

    channelsCheck = [False for i in range(0, NUM_OF_CHANNELS)]
    for i in range(0, f):
        for j in range(0, NUM_OF_CHANNELS):
            channelsCheck[j] |= channels[INTERF[i]][j]

    channelsCheckCount = 0
    for i in range(0, NUM_OF_CHANNELS):
        if channelsCheck[i] == True:
            channelsCheckCount += 1

    qtChannels = (NUM_OF_CHANNELS - channelsCheckCount) / (1 + degrees[-act[1]] - u); 

    for i in range(0, NUM_OF_CHANNELS):
        if not channelsCheck[i]:
            channels[-act[1]][i] = True
            qtChannels -= 1
            if qtChannels == 0:
                break

MAC_CHANNELLS = ["" for i in range(0, numRouters)]

for i in range(0, numRouters):
    channelsCheckCount = 0
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            channelsCheckCount += 1
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            MAC_CHANNELLS[i] += "1"
        else:
            MAC_CHANNELLS[i] += "0"

for i in range (0, numRouters):
    print "router", i+1, MAC_CHANNELLS[i]