import sys
import os

#protocolos = ["csmaca","chdsmeack","cadsmeack","hdsmeack","tsch","abmp"]
protocolos = ["abmptree","tschtree"]

num_nodes = int(sys.argv[1])

num_rep = int(sys.argv[2])

#initial_node = sys.argv[3]

for protocolo in protocolos:
    print "Simulando protocolo ",protocolo
    for j in range(1, num_rep+1):
        print "Replicacao ",j
        #prr app
        comando = "../../bin/Castalia -c General,amb3,debugALL,top"+str(j)+","+protocolo+" -i omnetpp.ini -o analisar.txt"
        print comando 
        os.system(comando)
        comando = "mv Castalia-Trace.txt "+protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt"
        os.system(comando)

comando = "python geraResultados.py "+str(num_nodes)+" "+str(num_rep)
os.system(comando)