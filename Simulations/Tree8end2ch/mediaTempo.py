import os
import sys

qtd = 0

cumulative = []
maxi = 0
maxi_id = 0

protocolo = sys.argv[1]

num_nodes = int(sys.argv[2])

values  = []
node_id = []

num_ch = 2

for i in range(1+num_ch,num_nodes+1+num_ch):
    nome_arquivo = "TEMPO_"+protocolo+"_node"+str(i)+".txt" 
    ref_arquivo = open(nome_arquivo,'r')	
    for linha in ref_arquivo:
        if not linha.isspace():
            values.append(linha)
            node_id.append(i)

for i in range(0,len(values)):
    valor = values[i]
    valor = valor.replace(",",".")
    valor = float(valor)
    valor = valor*10.0
    qtd = qtd+1
    ind = int(valor)
    if ind >= len(cumulative):
        for j in range(0,(ind-len(cumulative))):
            cumulative.append(0)
        cumulative.append(1)
    else:
        cumulative[ind] = cumulative[ind]+1
    #print ind
    #print cumulative
    if valor > maxi:
        maxi = valor
        maxi_id = node_id[i]

print "Histograma"
print ""
i = 1
for e in cumulative:
    e = float(e)
    v = str(float(e/qtd))
    v = v.replace(".",",")
    saida = str(i) + "\t" + v
    i = i+1
    saida = saida.replace(".",",")
    print saida
cumul = 0
print ""
print "Cumulative"
print ""
i = 1
for e in cumulative:
    cumul = cumul + e
    saida = str(i)+ "\t" + str(float(cumul)/qtd) 
    i = i+1
    saida = saida.replace(".",",")
    print saida
print ""
print "Maximo"
print ""
saida = str(maxi)
saida = saida.replace(".",",")
print saida
print maxi_id