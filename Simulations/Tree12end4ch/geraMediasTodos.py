#SO funciona para redes som 2 CH e 1 sink

import sys
import os

#protocolos = ["csmaca","chdsmeack","cadsmeack","hdsmeack","tsch","abmpstar"]
protocolos = ["tschtree","abmptree"]

num_nodes = int(sys.argv[1])

#(num_ch+1) = int(sys.argv[2])
num_ch = 4

for protocolo in protocolos:
    print "Analisando protocolo ",protocolo
    
    for i in range(1,num_ch+1):
        print "Gerando resultados para o CH ",i
        #prr mac
        comando = "python mediaPRR.py "+str(i)+ " < PRRMAC_" +protocolo+"_node"+str(i)+".txt  | tr '.' ',' >> "+" MediaPRRMAC_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat PRRMAC_"+protocolo+"_node"+str(i)+".txt >> MediaTodosPRRMAC_"+protocolo+".txt"
        os.system(comando)
        
        #RNP
        comando = "python mediaPRR.py "+str(i)+ " < RNP_" +protocolo+"_node"+str(i)+".txt  | tr '.' ',' >> "+" MediaRNP_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat RNP_"+protocolo+"_node"+str(i)+".txt >> MediaTodosRNP_"+protocolo+".txt"
        os.system(comando)
        
    
    for i in range((num_ch+1),num_nodes+(num_ch+1)):
        print "Gerando resultados para o no ",i
        #prr app
        comando = "python mediaPRR.py "+str(i)+ " < PRRAPP_" +protocolo+"_node"+str(i)+".txt | tr '.' ',' >> "+" MediaPRRAPP_"+protocolo+".txt" 
        os.system(comando)
        
        #prr mac
        comando = "python mediaPRR.py "+str(i)+ " < PRRMAC_" +protocolo+"_node"+str(i)+".txt  | tr '.' ',' >> "+" MediaPRRMAC_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat PRRAPP_"+protocolo+"_node"+str(i)+".txt >> MediaTodosPRRAPP_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat PRRMAC_"+protocolo+"_node"+str(i)+".txt >> MediaTodosPRRMAC_"+protocolo+".txt"
        os.system(comando)
        
        #RNP
        comando = "python mediaPRR.py "+str(i)+ " < RNP_" +protocolo+"_node"+str(i)+".txt  | tr '.' ',' >> "+" MediaRNP_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat RNP_"+protocolo+"_node"+str(i)+".txt >> MediaTodosRNP_"+protocolo+".txt"
        os.system(comando)
        
        #TX
        comando = "python mediaPRR.py "+str(i)+ " < TX_" +protocolo+"_node"+str(i)+".txt  | tr '.' ',' >> "+" MediaTX_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat TX_"+protocolo+"_node"+str(i)+".txt >> MediaTodosTX_"+protocolo+".txt"
        os.system(comando)
        
        #RX
        comando = "python mediaPRR.py "+str(i)+ " < RX_" +protocolo+"_node"+str(i)+".txt  | tr '.' ',' >> "+" MediaRX_"+protocolo+".txt"
        os.system(comando)
        
        comando = "cat RX_"+protocolo+"_node"+str(i)+".txt >> MediaTodosRX_"+protocolo+".txt"
        os.system(comando)
        
    comando = "python mediaPRR.py < MediaTodosPRRAPP_"+protocolo+".txt >>  Resultados_PRRAPP_Geral_"+protocolo+".txt"
    os.system(comando)
    comando = "python mediaPRR.py < MediaTodosPRRMAC_"+protocolo+".txt >>  Resultados_PRRMAC_Geral_"+protocolo+".txt"
    os.system(comando)
    comando = "python mediaPRR.py < MediaTodosRNP_"+protocolo+".txt >>  Resultados_RNP_Geral_"+protocolo+".txt"
    os.system(comando)
    comando = "python mediaPRR.py < MediaTodosTX_"+protocolo+".txt >>  Resultados_TX_Geral_"+protocolo+".txt"
    os.system(comando)
    comando = "python mediaPRR.py < MediaTodosRX_"+protocolo+".txt >>  Resultados_RX_Geral_"+protocolo+".txt"
    os.system(comando)
    #delay
    comando = "python mediaDelay.py "+protocolo+" "+str(num_nodes)+ " "+str((num_ch+1))+" > MediaDelay_"+protocolo+".txt" 
    os.system(comando)

    #tempo_desc
    comando = "python mediaTempo.py "+protocolo+" "+str(num_nodes)+ " "+str((num_ch+1))+ " > MediaTempo_"+protocolo+".txt" 
    os.system(comando)

comando = "python juntaResultadosPRRAPP.py "+str(num_nodes)+" > Resultados_PRRAPP.txt"
os.system(comando)

comando = "python juntaResultadosPRRMAC.py "+str(num_nodes+num_ch)+" > Resultados_PRRMAC.txt"
os.system(comando)

comando = "python juntaResultadosRNP.py "+str(num_nodes+num_ch)+" > Resultados_RNP.txt"
os.system(comando)

comando = "python juntaResultadosTX.py "+str(num_nodes)+" > Resultados_TX.txt"
os.system(comando)

comando = "python juntaResultadosRX.py "+str(num_nodes)+" > Resultados_RX.txt"
os.system(comando)
        #prr_power
        #comando = "python getTempoDesconectado.py "+str(i)+ " < Castalia-Trace_"protocolo+"_"+str(num_nodes)+"_"+str(j)+".txt" >> "TEMPO_"+protocolo+"_node"+str(i)+".txt" 
        #comando = "python getPRRandPOWER.py "+str(i)+ " < Castalia-Trace.txt > resultadosREP"+str(replicacao)+"/PRRandPOWER_Node"+str(i)+"_rep"+str(replicacao)+"_CD"+str(ch_div)+".txt" 
        #os.system(comando)
    
    