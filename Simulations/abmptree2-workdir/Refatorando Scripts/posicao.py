import smallestEnclosingCircle as sec
import math

#funcao de alcance do roteador
def router_reach(ple, d0, pld0, sigma, pt, sen_tr):
    return 10**( (sen_tr - pt + sigma + pld0)/(-10*ple) + math.log10(d0) )

#setando constantes manualmente
numNodes = 27
numRouters = 4
inters_p = 0.80 # intersect percentage (util para todos intereseccionarem com sink node) comunicacao com o sink node garantida
ple = 1.69 #expoente de perda
pld0 = 80.48 #perda na distancia de referencia
d0 = 15 #distancia de referencia
sigma = 6.62 #desvio padrao em dB a ser aplicado
pt = 0 #potencia de transmissao
sen_tr = -94 #sensibilidade do transceptor
sin45 = math.sqrt(2)/2 # posicionar os nos na arquitetura de quadrado

#zerando os valores de posicionamento
npx = [0 for i in range(0, numNodes)]
npy = [0 for i in range(0, numNodes)]
npz = [0 for i in range(0, numNodes)]

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

#calculando o valor do posicionamento do sink node com smallestEncloseCircle
sn_pos = sec.make_circle(zip(npx[numRouters+1:], npy[numRouters+1:]))
npx[0] = sn_pos[0]
npy[0] = sn_pos[1]

#calculando o valor do posicionamento para os routers
radious = router_reach(ple, d0, pld0, 2*sigma, 7.5, sen_tr) 

npx[1] =  inters_p*radious*sin45 + sn_pos[0]
npy[1] =  inters_p*radious*sin45 + sn_pos[1]
npx[2] = -inters_p*radious*sin45 + sn_pos[0]
npy[2] =  inters_p*radious*sin45 + sn_pos[1]
npx[3] =  inters_p*radious*sin45 + sn_pos[0]
npy[3] = -inters_p*radious*sin45 + sn_pos[1]
npx[4] = -inters_p*radious*sin45 + sn_pos[0]
npy[4] = -inters_p*radious*sin45 + sn_pos[1]

#imprimindo resultado final
for i in range(0, numRouters+1):
    print("SN.node["+str(i)+"].xCoor = " + str(npx[i]))
    print("SN.node["+str(i)+"].yCoor = " + str(npy[i]))
    print("SN.node["+str(i)+"].zCoor = 2")