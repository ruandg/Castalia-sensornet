import sys
import os

pasta = sys.argv[1]
filename = sys.argv[2]
node_id = int(sys.argv[3])

arq_PRRAPP = open((pasta+"/PRRAPP_"+filename+"_node"+str(node_id)+".txt"), 'w')
arq_PRRMAC = open((pasta+"/PRRMAC_"+filename+"_node"+str(node_id)+".txt"), 'w')
arq_DELAY = open((pasta+"/DELAY_"+filename+"_node"+str(node_id)+".txt"), 'w')
arq_TEMPO = open((pasta+"/TEMPO_"+filename+"_node"+str(node_id)+".txt"), 'w')

tx_cont = 0
rx_cont = 0
last_id = "0"

tx_cont_mac = 0
rx_cont_mac = 0
last_id_mac = "0"

last_id_delay = "0"
tempos = [0,0,0,0,0,0,0,0,0,0]

last_id_tempo = "0"
pri = 0
ePri = True

WINDOW = 10

try:
    while True:
        linha = raw_input()
        linha = linha.replace("SN"," SN")
        linha = linha.replace("dBm", " dBm")
        if linha == "":
            continue
        linha2 = linha 
        linha = linha.split()
        tempo = float(linha[0])
        
        #ANALISE PRR APP
        if(linha[1] == ("SN.node["+str(node_id)+"].Application") and linha[2] == "Sending" and linha[3] == "packet"):
            tx_cont = tx_cont+1.0
          #  print linha2
        if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
            if linha[4] != last_id:
                rx_cont = rx_cont+1.0
            last_id = linha[4]
           # print linha2
            
        if tx_cont%WINDOW == 0 and tx_cont != 0:
            PRR = float(rx_cont/tx_cont)
            tx_cont = 0
            rx_cont = 0
            saida = str(PRR)+"\n"
            saida = saida.replace(".",",")
            #print saida
            arq_PRRAPP.write(saida)
            
        #ANALISE PRR MAC
        if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmittiing" and linha[3] == "packet"):
            tx_cont_mac = tx_cont_mac+1.0
          #  print linha2
        if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmittiing" and linha[3] == "packet"):
            tx_cont_mac = tx_cont_mac+1.0
        #  print linha2
        if(linha[1] == "SN.node[0].Communication.MAC" and linha[2] == "Received" and linha[6] == str(node_id)):
            if linha[4] != last_id_mac:
                rx_cont_mac = rx_cont_mac+1.0
            last_id_mac = linha[4]
           # print linha2
            
        
        if tx_cont_mac%WINDOW == 0 and tx_cont_mac != 0:
            PRR = float(rx_cont_mac/tx_cont_mac)
            tx_cont_mac = 0
            rx_cont_mac = 0
            #saida = str(tempo) + "\t" + str(PRR)
            saida = str(PRR)+"\n"
            saida = saida.replace(".",",")
            arq_PRRMAC.write(saida)
            #print saida
             
        #ANALISE DELAY
        if(linha[1] == ("SN.node["+str(node_id)+"].Application") and linha[2] == "Sending" and linha[3] == "packet"):
            packet_id = int(linha[4])
            tempos[packet_id%10] = tempo
              #  print linha2
        if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
            if linha[4] != last_id_delay:
                packet_id = int(linha[4])
                tempo_tx = tempos[packet_id%10]
                delay = tempo - tempo_tx
                saida = str(delay)+"\n"
                saida = saida.replace(".",",")
                #print saida
                arq_DELAY.write(saida)
            last_id_delay = linha[4]
           # print linha2
           
        #ANALISE TEMPO
        if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
            if linha[4] != last_id_tempo:
                if ePri:
                    pri = tempo
                    ePri = False
                else:
                    delay_tempo = tempo - pri
                    saida = str(delay_tempo)+"\n"
                    saida = saida.replace(".",",")
                    #print saida
                    arq_TEMPO.write(saida)
                    pri = tempo
            last_id_tempo = linha[4]
           # print linha2
           
except EOFError as e:
    arq_PRRAPP.close()
    arq_PRRMAC.close()
    arq_DELAY.close()
    arq_TEMPO.close()