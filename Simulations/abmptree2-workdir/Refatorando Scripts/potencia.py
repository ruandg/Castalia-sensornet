#MUDANCA: RECEBE POSICIONAMENTO E CLUSTER-ID, CALCULA A MENOR POTENCIA NECESSARIA
#PARA GARANTIR QUASE 95% DE COMUNICACAO (-2sigma)
#UTILIZANDO A 68 95 99.7 RULE
import smallestEnclosingCircle as sec
import math

#verifica a distancia
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
#potencia de transmissao
def ptransmissao(ple, d0, pld0, sigma, sen_tr, d): #perda no percurso + limiar
    return (pld0 + 10*ple*math.log10(d/d0) + sigma) + sen_tr
    
#choosing ptrs by potency level
def choosePTRs(n):
    n = float(n)
    ptrsLEVELS = [0, -1, -3, -5, -7, -10, -15, -25]
    for i in range(0, 8):
        if n > ptrsLEVELS[i]:
            if i == 0: 
                return 0
            return ptrsLEVELS[i-1]
    return -25

#setando constantes manualmente
numNodes = 53
numRouters = 4
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
sen_tr = -94 #sensibilidade do transceptor

#zerando os valores de posicionamento
npx = [0 for i in range(0, numNodes)]
npy = [0 for i in range(0, numNodes)]
npz = [0 for i in range(0, numNodes)]
pTRS = [15 for i in range(0, numNodes)]

#valor de potencia para router, sinknode
pTRS[0] = 15 #setando manualmente sink node
pTRS[1:5] = [10 for i in range(0, 4)] #setando manualmente router node

#adquirindo os valores do posicionamento do arquivo < topologia.txt
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
#alterando a potencia para cada no final
for i in range(5, numNodes):
    ptrans = ptransmissao(ple, d0, pld0, 2*sigma, sen_tr, dist(npx[i], npy[i], npx[clusterID[i]+1], npy[clusterID[i]+1]))
    pTRS[i] = choosePTRs(min(pTRS[i], ptrans))

for i in range(5, numNodes):
    print "SN.node["+str(i)+"].Communication.Radio.TxOutputPower = \""+str(pTRS[i])+"dBm\""


#PROBLEMA: COM 2 SIGMA AS POTENCIAS DAO MUITO ALTAS