import math
import Queue as Q

#lista com bits setados
def set_bits(num):
    ans = list()
    router = 0
    while num != 0:
        if num & 1:
            ans.append(router)
        num >>= 1
        router += 1
    return ans

#verifica se ha interferencia
def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

#2*sigma interfere com 98% de probabilidade
#0*sigma interfere com 50% de probablidade
def interf(ple, d0, pld0, sigma, pt, sen_tr, x1, y1, x2, y2):
    return node_reach(ple, d0, pld0, sigma, pt, sen_tr) >= dist(x1, y1,x2, y2)

def node_reach(ple, d0, pld0, sigma, pt, sen_tr):
    return 10**( (sen_tr - pt + sigma + pld0)/(-10*ple) + math.log10(d0) )

#constantes necessarias
numNodes = 53
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


#lendo npx npy e ptrs
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

###### ESCOLHENDO QUAL NO PERTENCE A QUAL ROTEADOR #######
#para cada no verificar com que roteador ele interfere (50% do tempo)(e quantos)
#ordenar por quantidade menor para o maior
#se nao interfere com nenhum coloca no mais proximo

numSensors = numNodes - numRouters - 1
sensors = [0 for i in range(0, numSensors)] #bitwise
routers = [0 for i in range(0, numRouters)] #quantidade de nos roteados
clusterID = [-1 for i in range(0, numSensors)] #no pai do sensor i
areas = [list() for i in range(0, 2**numRouters)] #area em que tao os nos finais


for i in range(0, numSensors):
    for j in range(0, numRouters): # se interfere + 50% do tempo
        if interf(ple, d0, pld0, -0*sigma, pTRS[i], sen_tr, 
             npx[i+numRouters+1], npy[i+numRouters+1], npx[j+1], npy[j+1]):
            sensors[i] |= (1 << j)

    areas[sensors[i]].append(i)
    
    intf = set_bits(sensors[i])
    if len(intf) == 0:
        nearest = -1
        mindist = 100000
        for k in range (0, numRouters):
            if dist(npx[i+numRouters+1], npy[i
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
+numRouters+1], npx[k+1], npy[k+1]) < mindist:
                nearest = k
                mindist = dist(npx[i+numRouters+1], npy[i+numRouters+1], npx[k+1], npy[k+1])
        clusterID[i] = nearest #mais proximo
        routers[nearest] += 1
    elif len(intf) == 1:
        clusterID[i] = intf[0]
        routers[intf[0]] += 1


print "Quantidade de nos exclusivos para roteadores: ", routers[0], routers[1], routers[2], routers[3]

#atribuir ao roteador que possui menos sensors nodes
for i in range(1, 2**numRouters): #para cada area
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
maxx = -1
print "           CLUSTER_ID                 SENSOR_NODE"
for i in range (0, numRouters):
    if routers[i] > maxx:
        maxx =routers[i]
    print "Para o roteador", i+1, "->", str(routers[i]), "sensor nodes (",
    for j in range (0, numSensors):
        if clusterID[j] == i:
            print j+numRouters+1,
    print ")"


#SALVA COM VALOR DO CLUSTER ID
print "\n\n-1 0 0 0 0",
for i in range (0, numSensors):
    print str(clusterID[i]+1),

nodeIdSlot = [str() for i in range(0, numRouters)]
for i in range (0, numSensors):
    if i%4 == 0:
        print
        print str(i/4) + " -",
    nodeIdSlot[clusterID[i]] += str(i+numRouters+1).zfill(2)
    print str(clusterID[i]+1),
print
for i in range(0, numRouters):
    print(nodeIdSlot[i])

allocatedslot = [str() for i in range(0, numSensors)]
aparicao = [0 for i in range(0, numRouters)]
totalAllocatedSlot = maxx+1 #maxx = valor maximo desnsor node por roteador
for i in range(0, numSensors):
    aparicao[clusterID[i]] += 1
    print "SN.node["+str((i+numRouters+1))+"].Communication.MAC.allocatedSlots = \""+'0'*aparicao[clusterID[i]] + '1' + '0'*(totalAllocatedSlot - aparicao[clusterID[i]] - 1) + "\"";

