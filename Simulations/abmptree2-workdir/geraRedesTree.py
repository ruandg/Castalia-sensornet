#Criaca: Ruan Delgado Gomes - ruan.gomes@ifpb.edu.br
#Alteracao: Marcello Marques de Oliveira - prodmarcello@gmail.com
#Referente a alteracao: 
#  * aplicacao de um novo algoritmo de alocacao de canais
#  * comparacao com o algoritmo antigo
#  * dados referentes apenas ao protocolo ABMP
#Works for networks with up to 100 nodes (including ONE sink node, cluster heads, and end nodes)
#coordenada z igual para todos
#TODO: suport for multiple sinks

from random import randrange, uniform
import math as m

number_attempts = 1
prrThreshold = 0.9
beaconThreshold = 0.9
slotSize = 10 #ms

packet_rate = 1

max_ch = 30
max_end = 40

number_ch = 4
number_endnodes = 12

buffersize_ch = int(number_endnodes*1.5)
buffersize_endnode = 1

number_txch = 9
numbertx_end = 1

num_rep = 5

#TODO: calculate the size of slotframe
slotframe_size = 2 + number_endnodes + number_ch*number_txch


nodes_positions_x = []
nodes_positions_y = []

saida_positions = ""
saida_abmp = ""

distancias = ""

saida_abmp = saida_abmp + "SN.node[*].Communication.MACProtocolName = \"ABMPTree\"\n"
saida_abmp = saida_abmp + "SN.node[*].Communication.treeTopology = true\n"
saida_abmp = saida_abmp + "SN.node[*].Communication.MAC.slotFrameSize = "+str(slotframe_size)+"\n"
saida_abmp = saida_abmp + "SN.node[*].Communication.MAC.numberOfAttempts = "+str(number_attempts)+"\n"
saida_abmp = saida_abmp + "SN.node[*].Communication.MAC.prrThreshold = "+str(prrThreshold)+"\n"
saida_abmp = saida_abmp + "SN.node[*].Communication.MAC.beaconThreshold = "+str(beaconThreshold)+"\n"
saida_abmp = saida_abmp + "SN.node[*].Communication.MAC.slotSize = "+str(slotSize)+"\n"
saida_abmp = saida_abmp + "************************************************************\n"

#sink node
saida_positions = saida_positions + "SN.node[0].xCoor = 0\n"
saida_positions = saida_positions + "SN.node[0].yCoor = 0\n"
saida_positions = saida_positions + "SN.node[0].zCoor = 2\n"
saida_abmp = saida_abmp + "SN.node[0].Communication.MAC.isCoordinator = true\n"

nodes_positions_x.append(0);
nodes_positions_y.append(0);

saida_abmp = saida_abmp + "SN.node[0].Communication.MAC.nodeIdSlot = \"0000"
for i in range(0,number_endnodes):
    saida_abmp = saida_abmp + "00"

for k in range(0,number_txch):
    for i in range(1,number_ch+1):
        if i < 10:
            idslot = "0"+str(i)
        else:
            idslot = str(i)
        saida_abmp = saida_abmp + idslot
saida_abmp = saida_abmp + "\"\n"

saida_abmp = saida_abmp + "SN.node[0].Application.packet_rate = 0\n"


#sinc node tem acesso a todos os canais
saida_abmp = saida_abmp + "SN.node[0].Communication.MAC.channels = \"1111111111111111\"\n";
saida_abmp = saida_abmp + "************************************************************\n"
#cluster heads
x_base = nodes_positions_x[0]
y_base = nodes_positions_y[0]

for i in range(1,number_ch+1):
    xCoor = uniform(-max_ch,max_ch) + x_base #randomiza entre -30 e 30
    yCoor = uniform(-max_ch,max_ch) + y_base

    dist = m.sqrt(m.pow(xCoor-x_base,2)+m.pow(yCoor-y_base,2)) #distancia euclidiana
    distancias = distancias + "# "+ str(dist)+"\n"

    saida_positions = saida_positions + "SN.node["+str(i)+"].xCoor = "+str(xCoor)+"\n"
    saida_positions = saida_positions + "SN.node["+str(i)+"].yCoor = "+str(yCoor)+"\n"
    saida_positions = saida_positions + "SN.node["+str(i)+"].zCoor = 2"+"\n"
    saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.isClusterHead = true\n"
    saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.clusterID = 0\n"
    saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.macBufferSize = "+str(buffersize_ch)+"\n"
    nodes_positions_x.append(xCoor);
    nodes_positions_y.append(yCoor);
    saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.allocatedSlots = \"01"
    for k in range(0,number_endnodes):
        saida_abmp = saida_abmp + "0"

    qtd_ant = i-1
    qtd_dep = number_ch-i

    for n in range (0,number_txch):
       for k in range(0,qtd_ant):
           saida_abmp = saida_abmp + "0"
       saida_abmp = saida_abmp + "1"
       for k in range(0,qtd_dep):
           saida_abmp = saida_abmp + "0"
    
    saida_abmp = saida_abmp + "\"\n"

    if i < 10:
        saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.nodeIdSlot = \"00"+"0"+str(i)
    else:
       saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.nodeIdSlot = \"00"+str(i)
    

    for n in range(0,number_endnodes):
        if (1+number_ch+(i-1)*number_endnodes + n) < 10:
            idslot = "0"+str(1+number_ch+(i-1)*number_endnodes + n)
        else:
            idslot = str(1+number_ch+(i-1)*number_endnodes + n)
        saida_abmp = saida_abmp + idslot
    
    qtd_ant = i-1
    qtd_dep = number_ch-i

    for n in range (0,number_txch):
        for k in range(0,qtd_ant):
            saida_abmp = saida_abmp + "00"
        if i < 10:
            saida_abmp = saida_abmp + "0"+str(i)
        else:
            saida_abmp = saida_abmp + str(i)
        for k in range(0,qtd_dep):
            saida_abmp = saida_abmp + "00"
        
    saida_abmp = saida_abmp + "\"\n"
       
    saida_abmp = saida_abmp + "SN.node["+str(i)+"].Communication.MAC.channels = \"";
  
    qtd_ant = i-1
    qtd_dep = number_ch-i

    contc = 0
    for n in range (0,(16/number_ch)):
        for k in range(0,qtd_ant):
            saida_abmp = saida_abmp + "0"
            contc = contc + 1
        saida_abmp = saida_abmp + "1"
        contc = contc + 1
        for k in range(0,qtd_dep):
            saida_abmp = saida_abmp + "0"
            contc = contc + 1

    for n in range(0, (16-contc)):
        saida_abmp = saida_abmp + "0"
    
    saida_abmp = saida_abmp + "\"\n"

    saida_abmp = saida_abmp + "SN.node["+str(i)+"].Application.packet_rate = 0\n"

saida_abmp = saida_abmp + "************************************************************\n"

end_nodes_positions_x = [] #criado para armazenar os nos finais 
end_nodes_positions_y = [] #para comparar com os nos representantes da subrede
j = number_ch+1
#end nodes
for i in range(1,number_ch+1):
    x_base = nodes_positions_x[i]
    y_base = nodes_positions_y[i]
    for k in range(0,number_endnodes):
        xCoor = uniform(-max_end,max_end) + x_base
        yCoor = uniform(-max_end,max_end) + y_base
        end_nodes_positions_x.append(xCoor) 
        end_nodes_positions_y.append(yCoor)

    
        dist = m.sqrt(m.pow(xCoor-x_base,2)+m.pow(yCoor-y_base,2))
        distancias = distancias + "# "+str(dist)+"\n"

        saida_positions = saida_positions + "SN.node["+str(j+k)+"].xCoor = "+str(xCoor)+"\n"
        saida_positions = saida_positions + "SN.node["+str(j+k)+"].yCoor = "+str(yCoor)+"\n"
        saida_positions = saida_positions + "SN.node["+str(j+k)+"].zCoor = 2"
        if not(i == number_ch and k == (number_endnodes-1)):
           saida_positions = saida_positions+"\n"
        saida_abmp = saida_abmp + "SN.node["+str(j+k)+"].Communication.MAC.clusterID = "+str(i)+"\n"
        saida_abmp = saida_abmp + "SN.node["+str(j+k)+"].Communication.MAC.macBufferSize = "+str(buffersize_endnode)+"\n"
    
        saida_abmp = saida_abmp + "SN.node["+str(j+k)+"].Communication.MAC.allocatedSlots = \"0"
    
        qtd_ant = k
        qtd_dep = number_endnodes-1-qtd_ant

        for n in range (0,numbertx_end):
          for p in range(0,qtd_ant):
              saida_abmp = saida_abmp + "0"
          saida_abmp = saida_abmp + "1"
          for p in range(0,qtd_dep):
              saida_abmp = saida_abmp + "0"
        
        saida_abmp = saida_abmp + "\"\n"
    
        saida_abmp = saida_abmp + "SN.node["+str(j+k)+"].Application.packet_rate = "+str(packet_rate)+"\n"
    
    j = j + number_endnodes





print "#Numero de nos"
print "SN.numNodes = "+str(1+number_ch*number_endnodes+number_ch)
#print "#positions"
#print saida_positions
print distancias
print "[Config abmptree]"
print saida_abmp


############### algoritmo novo

print (number_endnodes)

def EuclidDist(x1, y1, x2, y2):
    return m.sqrt(m.pow(x1-x2,2)+m.pow(y1-y2,2))

############### criando grafo a partir das informacoes de distancia

G = [[0 for u in range(0, number_ch)] for v in range(0, number_ch)]

LIMIAR = 15 #menos que isso causa intereferencia
#se algum end node pertencente a sub-rede y interferir com 
#o ch da sub-rede x entao ha interferencia entre
#as subredes x e y
for x in range(0, number_ch):
    for y in range(0, number_ch):
        if x != y:
            for z in range(0, number_endnodes):
                if EuclidDist(end_nodes_positions_x[y*number_endnodes + z], 
                    end_nodes_positions_y[y*number_endnodes + z],
                    nodes_positions_x[x+1], 
                    nodes_positions_y[x+1]) <= LIMIAR:
                    G[x][y] = G[y][x] = 1

############ teste manual
#G[0] = [0, 1, 0, 1]
#G[1] = [1, 0, 1, 1]
#G[2] = [0, 1, 0, 1]
#G[3] = [1, 1, 1, 0]

############ printando o grafo de interferencia
for i in range(0, number_ch):
    for j in range(0, number_ch):
        print G[i][j],
    print

############# algoritmo alocando canais para o grafo acima

NUM_OF_CHANNELS = 16
degrees = [0 for i in range(0, number_ch)]
used = [0 for i in range(0, number_ch)]
import  Queue as Q
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

    channelsCheck = [False for i in range(0, NUM_OF_CHANNELS)] #16 number of channels
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


############### print na resposta

for i in range(0, number_ch):
    channelsCheckCount = 0
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            channelsCheckCount += 1
    print "Cluster head " + str(i) + "(" + str(channelsCheckCount) + ")"
    print "channels -> ",
    MAC_CHANNELLS = ""
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            print str(j),
            MAC_CHANNELLS += "1"
        else:
            MAC_CHANNELLS += "0"
    print MAC_CHANNELLS

    print
    print


#################