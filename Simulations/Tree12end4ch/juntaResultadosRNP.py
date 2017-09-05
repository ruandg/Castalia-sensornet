import os
import sys

num_nodes = int(sys.argv[1])

#protocolos = ["csmaca","chdsmeack","cadsmeack","hdsmeack","tsch","abmpstar"]
protocolos = sys.argv[3:]

media_nodes = []
var_nodes = []

for i in range(0,num_nodes*len(protocolos)):
    media_nodes.append(0)
    var_nodes.append(0)
    
j = 0
for protocolo in protocolos:
    for i in range(1,num_nodes+1):
        nome_arquivo = "MediaRNP_"+protocolo+".txt" 
        ref_arquivo = open(nome_arquivo,'r')	
        lines = ref_arquivo.readlines()
        k = 0
        lim = j*num_nodes
        while k < num_nodes:
            linha = lines[k].split()
            media_nodes[lim+k] = linha[0]
            var_nodes[lim+k] = linha[1]
            k = k+1
    j = j + 1 

saida = ""
for protocolo in protocolos:
    saida = saida + protocolo + "\t"

print saida
    
for k in range(0, num_nodes):
    j = 0
    saida = ""
    for i in range(0,len(protocolos)):
        lim = j*num_nodes
        saida = saida + str(media_nodes[lim+k]) + "\t"
        j = j+1
    print saida
        
print ""
for k in range(0, num_nodes):
    j = 0
    saida = ""
    for i in range(0,len(protocolos)):
        lim = j*num_nodes
        saida = saida + str(var_nodes[lim+k]) + "\t"
        j = j+1
    print saida

print ""
saida = ""
for protocolo in protocolos:
    nome_arquivo = "Resultados_RNP_Geral_"+protocolo+".txt" 
    ref_arquivo = open(nome_arquivo,'r')	
    lines = ref_arquivo.readlines()
    linha = lines[0].split()
    saida = saida + linha[0] + "\t"
saida = saida.replace(".",",")
print saida
    
saida = ""
for protocolo in protocolos:
    nome_arquivo = "Resultados_RNP_Geral_"+protocolo+".txt" 
    ref_arquivo = open(nome_arquivo,'r')	
    lines = ref_arquivo.readlines()
    linha = lines[0].split()
    saida = saida + linha[1] + "\t"
saida = saida.replace(".",",")
print saida