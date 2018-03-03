#conseguir os valores uteis em omnetpp.ini
#entrada: topologia utilizada
#saida: o mesmo arquivo omnetpp.ini
#       com abmptree3 
#       * mudanca no mac-channel e clusterID
#       * mudanca na posicao do roteador/sinknode)
#       * mudanca na potencia dos nos
#       modelo de roteador: quadrado

import sys
import os
import Queue as Q
import ctypes
import math
import smallestEnclosingCircle

################# UTILIDADES ########################
#consegue a coordenada do no a partir do arquivo
def getValueCoord(txt, it):
	it = txt.find("=", it) + 2
	value = ""
	while txt[it] != '\n':
		value += txt[it]
		it += 1
	return float(value), it

#muda a coordenada a partir do arquivo
# *necessario que o valor em omnetpp.ini esteja em decimal
def getValueCoordandChange(txt, it, new_value):
    it = txt.find("=", it) + 2
    i = 0
    new_value = str(new_value)
    
    if new_value.find('.') == -1:
        new_value += '.'

    while len(new_value) < 15:
        new_value += '0'
    
    mutable = ctypes.create_string_buffer(txt)
    while txt[it] != '\n':
        mutable[it] = new_value[i]
        i += 1
        it += 1
    return mutable.value, it

#realiza a mudanca de canal
def changeMacChannel(txt, it, MAC, nc):
	it = txt.find("MAC.channels", it) + 16
	mutable = ctypes.create_string_buffer(txt)
	for i in range (0, nc):
		mutable[it+i] = MAC[i]
	return mutable.value, it+i

#realiza a mudanca de clusterID
def changeClusterId(txt, it, cluster_id):
    it = txt.find("clusterID", it) + 12
    mutable = ctypes.create_string_buffer(txt)
    mutable[it] = str(cluster_id+1)[0]
    return mutable.value, it

#verifica a distancia
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#verifica se ha interferencia
def interf(ple, d0, pld0, sigma, pt, sen_tr, d):
    return pt - (pld0 + 10*ple*math.log10(d/d0) + sigma) >= sen_tr

#alcance do roteador
def router_reach(ple, d0, pld0, sigma, pt, sen_tr):
    return 10**( (sen_tr - pt + sigma + pld0)/(-10*ple) + math.log10(d0) )

#potencia de transmissao
def ptransmissao(ple, d0, pld0, sigma, sen_tr, d): #perda no percurso + limiar
    return (pld0 + 10*ple*math.log10(d/d0) + sigma) + sen_tr

def set_bits(num):
    ans = list()
    router = 0
    while num != 0:
        if num & 1:
            ans.append(router)
        num >>= 1
        router += 1
    return ans


#choosing ptrs by potency level
def choosePTRs(n):
    n = float(n)
    ptrsLEVELS = [15, 10, 5, 0, -1, -3, -5, -7, -10, -15, -25]
    for i in range(0, 11):
        if n > ptrsLEVELS[i]:
            return ptrsLEVELS[i-1]


############## INICIO DA LEITURA ##################
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
npx = [0 for i in range(0, numNodes)]
npy = [0 for i in range(0, numNodes)]
npz = [0 for i in range(0, numNodes)]
clusterID = [0 for i in range(0, numNodes)]

while cont < numNodes:
    npx[cont], it = getValueCoord(txt, it)
    npy[cont], it = getValueCoord(txt, it)
    npz[cont], it = getValueCoord(txt, it)
    cont += 1

####### SETANDO VALORES DE SIMULACAO MANUALMENTE #######
NUM_OF_CHANNELS = 16
number_ch = 4
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
pt = 0 #potencia de transmissao
sen_tr = -94 #sensibilidade do transceptor


############## INICIANDO ALGORITMO ###########

#topologia adotada para 4 roteadores

#pela equacao Pr(d) = Pt - L(d) = - L(d)
#a prob de o valor ficar entre [-2sig, 2sig] eh 95.44
#aa prob da potencia de recepcao ficar entre -(L(d)+2sig) e -(L(d)-2sig) eh 95.44
#entao se a sensibilidade do transceptor eh -94dBm
#as transmissoes de A nao sao percebidas por B se 
# L(d0) + 10nlog(d/d0) +13,24 < -94 : pois esse eh o menor valor possivel de receber
# ou seja se L(d0) + 10nlog(d/d0) +13,24 > 94 entao ha interferencia (ou comunicacao)

#conseguindo posicao do sink node com smallestenclosecircle
sn_pos = smallestEnclosingCircle.make_circle(zip(npx[5:], npy[5:]))
npx[0] = sn_pos[0]
npy[0] = sn_pos[1]

#alterando a potencia manualmente para os sink e router nodes
pTRS = [0 for i in range(0, numNodes)]
pTRS[0] = 15 #setando manualmente sink node
pTRS[1:5] = [10 for i in range(0, 4)] #setando manualmente router node

#conseguindo posicao otima dos roteadores 
sin45 = math.sqrt(2)/2 # posicionar os nos na arquitetura de quadrado
inters_p = 0.80 # intersect percentage (util para todos intereseccionarem com sink node)
                                    #comunicacao com o sink node garantida
radious = router_reach(ple, d0, pld0, 2*sigma, 7.5, sen_tr) 

npx[1] =  inters_p*radious*sin45 + sn_pos[0]
npy[1] =  inters_p*radious*sin45 + sn_pos[1]
npx[2] = -inters_p*radious*sin45 + sn_pos[0]
npy[2] =  inters_p*radious*sin45 + sn_pos[1]
npx[3] =  inters_p*radious*sin45 + sn_pos[0]
npy[3] = -inters_p*radious*sin45 + sn_pos[1]
npx[4] = -inters_p*radious*sin45 + sn_pos[0]
npy[4] = -inters_p*radious*sin45 + sn_pos[1]

#reposicionando sink node e router node
it = txt.find("Config "+top, 4300)

for i in range(0, 1+number_ch):
    txt, it = getValueCoordandChange(txt, it, npx[i])
    txt, it = getValueCoordandChange(txt, it, npy[i])
    it = getValueCoord(txt, it)[1] #jump coord z


#alterando a potencia para cada no final
for i in range(5, numNodes): #pegando o min(menor + 5%menor, 0) com 2*sigma (garante comunicacao confiavel)
    for j in range(1, 5):    #0.95 pois a potencia eh negativa (+5% do sinal)
        pTRS[i] = choosePTRs(min(pTRS[i], 0.95*(ptransmissao(ple, d0, pld0, 2*sigma, sen_tr,
                    dist(npx[i], npy[i], npx[j], npy[j])))))


###### ESCOLHENDO QUAL NO PERTENCE A QUAL ROTEADOR #######
#para cada no verificar com que roteador ele interfere (e quantos)
#ordenar por quantidade menor para o maior
#se nao interfere com nenhum coloca no mais proximo

numSensors = numNodes - number_ch - 1
sensors = [0 for i in range(0, numSensors)] #bitwise
routers = [0 for i in range(0, number_ch)] #quantidade de nos roteados
clusterID = [-1 for i in range(0, numSensors)] #no pai do sensor i
areas = [list() for i in range(0, 2**number_ch)] #area em que tao os nos finais

for i in range(0, numSensors):
    for j in range(0, number_ch): # se interfere + 50% do tempo
        if interf(ple, d0, pld0, 0*sigma, pTRS[i], sen_tr, 
             dist(npx[i+number_ch+1], npy[i+number_ch+1], npx[j+1], npy[j+1])):
            sensors[i] |= (1 << j)

    areas[sensors[i]].append(i)
    
    intf = set_bits(sensors[i])
    if len(intf) == 0:
        nearest = -1
        mindist = 100000
        for k in range (0, 4):
            if dist(npx[i+number_ch+1], npy[i+number_ch+1], npx[k+1], npy[k+1]) < mindist:
                nearest = k
                mindist = dist(npx[i+number_ch+1], npy[i+number_ch+1], npx[k+1], npy[k+1])
        clusterID[i] = nearest #mais proximo
        routers[nearest] += 1
    elif len(intf) == 1:
        clusterID[i] = intf[0]
        routers[intf[0]] += 1


print "Quantidade de nos exclusivos para roteadores: ", routers[0], routers[1], routers[2], routers[3]

#atribuir ao roteador que possui menos sensors nodes
for i in range(1, 2**number_ch): #para cada area
    if (i&(i-1)): #se interfere com alguem
        q = Q.PriorityQueue()
        sets = set_bits(i)
        for j in sets: # para cada roteador que afeta a area
            q.put((routers[j], j)) #salvar quantidade de nos roteados e numero do roteador
        for j in areas[i]: #para cada no sensor pertencente a area
            v = q.get() #verifico o roteador na fila de prioridade
            clusterID[j] = v[1] #roteador
            routers[v[1]] += 1 #roteador roteia agora 1 no a mais
            q.put((routers[v[1]], v[1]))

#printando os resultados
for i in range (0, number_ch):
    print "Para o roteador", i+1, "->", str(routers[i]), "sensor nodes (",
    for j in range (0, numSensors):
        if clusterID[j] == i:
            print j+5,
    print ")"


###### ESCOLHENDO QUAL CANAL PERTENCE A QUAL ROTEADOR #######
# criando o grafo
G = [[0 for i in range(0, number_ch)] for j in range(0, number_ch)]

for i in range(0, numSensors):
    for j in range(0, 4):
        if clusterID[i] == j:
            continue     #+50% do tempo
        if interf(ple, d0, pld0, 0*sigma, pTRS[i], sen_tr, 
                  dist(npx[i + number_ch + 1], npy[i + number_ch + 1], npx[j+1], npy[j+1])):
            G[clusterID[i]][j] = G[j][clusterID[i]] = 1

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
    for j in range(0, NUM_OF_CHANNELS):
        if channels[i][j] == True:
            MAC_CHANNELLS[i] += "1"
        else:
            MAC_CHANNELLS[i] += "0"

for i in range (0, number_ch):
    print "router", i+1, MAC_CHANNELLS[i]


##################ESCREVENDO OS RESULTADOS#######################3


it = txt.find("SN.node[*].Communication.MACProtocolName = \"ABMPTree\"")
abmptree3 = "[Config abmptree3]\n"
for i in range(0, numNodes):
    abmptree3 += "SN.node["+str(i)+"].Communication.Radio.TxOutputPower = \""+str(pTRS[i])+"dBm\"\n"
abmptree3 += txt[it:it+11904]

#alterar abmptree3

it = abmptree3.find("MAC.channels") + 20
for i in range(0, number_ch):
	abmptree3, it = changeMacChannel(abmptree3, it, MAC_CHANNELLS[i], NUM_OF_CHANNELS)

# para cada nosensor alterar seu valor de roteador no abmptree

it = abmptree3.find("SN.node["+str(number_ch+1)+"].Communication.MAC.clusterID ")
for i in range(0, numNodes - number_ch - 1):
    abmptree3, it = changeClusterId(abmptree3, it, clusterID[i])


FILE = open("omnetpp5.ini", "w")

FILE.write(txt[0:-389] + abmptree3 + txt[-392:])
print "omnetpp3.ini gerado com sucesso"
