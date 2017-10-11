#conseguir os valores uteis em omnetpp.ini
#entrada: topologia utilizada
#saida: o mesmo arquivo omnetpp.ini
#       com abmptree2 (mudanca no mac-channel)

import sys
import os
import Queue as Q
import ctypes
import math

#consegue a coordenada do no a partir do arquivo
def getValueCoord(txt, it):
	it = txt.find("=", it) + 2
	value = ""
	while txt[it] != '\n':
		value += txt[it]
		it += 1
	return float(value), it

#realiza a mudanca de canal para o abmptree2
def changeMacChannel(txt, it, MAC, nc):
	it = txt.find("MAC.channels", it) + 16
	mutable = ctypes.create_string_buffer(txt)
	for i in range (0, nc):
		mutable[it+i] = MAC[i]
	return mutable.value, it+i

#verifica a distancia
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#verifica se ha interferencia
def interf(ple, d0, pld0, sigma, pt, sen_tr, d):         #prob 95.44
    return pt - (pld0 + 10*ple*math.log10(d/d0) - 2*sigma) >= -94

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

#ler os nos
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

#pela equacao Pr(d) = Pt - L(d) = - L(d)
#a prob de o valor ficar entre [-2sig, 2sig] eh 95.44
#aa prob da potencia de recepcao ficar entre -(L(d)+2sig) e -(L(d)-2sig) eh 95.44
#entao se a sensibilidade do transceptor eh -94dBm
#as transmissoes de A nao sao percebidas por B se 
# L(d0) + 10nlog(d/d0) +13,24 < -94 : pois esse eh o maior valor possivel

# ou seja se L(d0) + 10nlog(d/d0) +13,24 > 94 entao ha interferencia

# criando o grafo
G = [[0 for u in range(0, number_ch)] for v in range(0, number_ch)]

#no0 -> sinknode
#no1 -> [5,16] no2 -> [17,28] no3 -> [29, 40] no4 -> [41, 52]
 
for i in range (1, number_ch + 1): #roteadores
    for j in range (1, number_ch + 1): #roteadores2
        if i == j:
            continue
        for k in range (j*12-7, j*12+5):
            if interf(ple, d0, pld0, sigma, pt, sen_tr, 
            dist(node_position_x[i], node_position_y[i],
                 node_position_x[k], node_position_y[k])):
                 G[i-1][j-1] = G[j-1][i-1] = 1 #bidirecional
        
# alocando canais de forma inteligente
degrees = [0 for i in range(0, number_ch)]
used = [0 for i in range(0, number_ch)]

q = Q.PriorityQueue()
channels = [[False for i in range(0, NUM_OF_CHANNELS)] for j in range(0, number_ch)]

for i in range(0, number_ch):
    for j in range(0, number_ch):
        if G[i][j]:
            degrees[j] += 1

for i in range(0, number_ch):
    q.put((-degrees[i], -i))

interf = [0 for i in range(0, number_ch)]

while not q.empty():
    act = q.get()
    used[-act[1]] = 1
    f = 0 #quantity of interference nodes
    u = 0 #quantity of sub-redes on interf already calc

    for i in range(0, number_ch):
        if G[-act[1]][i]:
            interf[f] = i
            f += 1
            if used[i]:
                u += 1

    channelsCheck = [False for i in range(0, NUM_OF_CHANNELS)]
    for i in range(0, f):
        for j in range(0, NUM_OF_CHANNELS):
            channelsCheck[j] |= channels[interf[i]][j]

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

MAC_CHANNELLS = ["" for i in range(0, number_ch)]

for i in range(0, number_ch):
    channelsCheckCount = 0
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            channelsCheckCount += 1
    #print "Cluster head " + str(i) + "(" + str(channelsCheckCount) + ")"
    #print "channels -> ",
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            #print str(j),
            MAC_CHANNELLS[i] += "1"
        else:
            MAC_CHANNELLS[i] += "0"
    #print MAC_CHANNELLS[i]

#end algorithm


it = txt.find("SN.node[*].Communication.MACProtocolName = \"ABMPTree\"")
abmptree2 = "[Config abmptree2]\n"
abmptree2 += txt[it:it+11904]
#print abmptree2
#alterar abmptree2

it = abmptree2.find("MAC.channels") + 20
for i in range(0, number_ch):
	abmptree2, it = changeMacChannel(abmptree2, it, MAC_CHANNELLS[i], NUM_OF_CHANNELS)


#gen omnetpp2.ini

FILE = open("omnetpp2.ini", "w")
#print txt[0:-388] + abmptree2 + txt[-392:-3]
FILE.write(txt[0:-388] + abmptree2 + txt[-392:])
print "omnetpp2.ini gerado com sucesso"