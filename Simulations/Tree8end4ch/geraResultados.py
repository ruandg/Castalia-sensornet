import sys
import os
from datetime import datetime


#protocolos = ["csmaca","chdsmeack","cadsmeack","hdsmeack","tsch","abmpstar"]
protocolos = ["abmptree","tschtree"]

num_nodes = int(sys.argv[1])

num_rep = int(sys.argv[2])

#initial_node = int(sys.argv[3])

now = datetime.now()
pasta = "resultados_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)
comando = "mkdir "+pasta
os.system(comando)

for protocolo in protocolos:
    print "Analisando protocolo ",protocolo
   # for i in range(initial_node,initial_node+num_nodes):
        #print "Gerando resultados para o no ",i
    for j in range(1, num_rep+1):
        print "Replicacao ",j
        comando = "python getTUDOTODOS.py < "+ protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt " + pasta +" "+protocolo+" "+str(num_nodes) 
        os.system(comando)
            #comando = "python getTUDO.py < "+ protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt " + pasta +" "+protocolo+" "+str(i) 
           # os.system(comando)
            #prr app
          #  comando = "python getPRRAPP.py "+str(i)+ " < " + protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt  >> "+pasta+"/PRRAPP_"+protocolo+"_node"+str(i)+".txt" 
           # os.system(comando)

            #prr mac
            #comando = "python getPRRMAC.py "+str(i)+ " < "+protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt >> "+pasta+"/PRRMAC_"+protocolo+"_node"+str(i)+".txt" 
            #os.system(comando)

            #delay
            #comando = "python getDELAY.py "+str(i)+ " < "+protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt >> "+pasta+"/DELAY_"+protocolo+"_node"+str(i)+".txt" 
            #os.system(comando)

            #tempo_desc
            #comando = "python getTempoDesconectado.py "+str(i)+ " < "+protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt >> "+pasta+"/TEMPO_"+protocolo+"_node"+str(i)+".txt"  
            #os.system(comando)

comando = "cp geraMediasTodos.py "+pasta+"/"
os.system(comando)
comando = "cp mediaPRR.py "+pasta+"/"
os.system(comando)
comando = "cp mediaTempo.py "+pasta+"/"
os.system(comando)
comando = "cp mediaDelay.py "+pasta+"/"
os.system(comando)
comando = "cp juntaResultadosPRRAPP.py "+pasta+"/"
os.system(comando)
comando = "cp juntaResultadosPRRMAC.py "+pasta+"/"
os.system(comando)
comando = "cp juntaResultadosRNP.py "+pasta+"/"
os.system(comando)
comando = "cp juntaResultadosTX.py "+pasta+"/"
os.system(comando)
comando = "cp juntaResultadosRX.py "+pasta+"/"
os.system(comando)

        #prr_power
        #comando = "python getTempoDesconectado.py "+str(i)+ " < Castalia-Trace_"protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt" >> "TEMPO_"+protocolo+"_node"+str(i)+".txt" 
        #comando = "python getPRRandPOWER.py "+str(i)+ " < Castalia-Trace.txt > resultadosREP"+str(replicacao)+"/PRRandPOWER_Node"+str(i)+"_rep"+str(replicacao)+"_CD"+str(ch_div)+".txt" 
        #os.system(comando)
    
    