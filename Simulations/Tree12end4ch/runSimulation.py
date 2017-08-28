import sys
import os

#protocolos = ["csmaca","chdsmeack","cadsmeack","hdsmeack","tsch","abmp"]
#protocolos = ["abmptree","tschtree"]

num_nodes = int(sys.argv[1])

num_rep = int(sys.argv[2])

protocolos = sys.argv[3:]

print "-----------------------------------------------------"
print "arquivo: runSimulation.py"
print "Numero de nos: " + str(num_nodes)
print "Numero de rep: " + str(num_rep)
print "Protocolos: "+ str(protocolos)
print "-----------------------------------------------------"
#initial_node = sys.argv[3]
p = str()
for protocolo in protocolos:
    print "Simulando protocolo ",protocolo
    for j in range(1, num_rep+1):
        print "Replicacao ",j
        #prr app
        comando = "../../bin/Castalia -c General,amb3,debugALL,top"+str(j)+","+protocolo+" -i omnetpp.ini -o analisar.txt"
        print comando 
        os.system(comando)
        #renomeando
        comando = "mv Castalia-Trace.txt "+protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt"
        os.system(comando)
    p += " " + protocolo #automatizando os comandos


comando = "python geraResultados.py "+str(num_nodes)+" "+str(num_rep)+p
print "Executando o comando: " + comando 
os.system(comando)