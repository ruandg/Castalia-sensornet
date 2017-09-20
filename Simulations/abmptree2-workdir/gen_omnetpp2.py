#conseguir os valores uteis em omnetpp.ini
#entrada: topologia utilizada
#saida: o mesmo arquivo omnetpp.ini
#       com abmptree2 (mudanca no mac-channel)

import sys
import os
import Queue as Q
import ctypes

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

# criando o grafo
G = [[0 for u in range(0, number_ch)] for v in range(0, number_ch)]
#necessario definir grafo aqui

 
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