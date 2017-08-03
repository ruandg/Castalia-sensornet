#Ruan Delgado Gomes
#Funcioanndo apenas para redes com dois CH e um SINK

import sys
import os

pasta = sys.argv[1]
filename = sys.argv[2]
number_nodes = int(sys.argv[3])

number_ch = 4

WINDOW = 10

arq_PRRAPP = []
arq_PRRMAC = []
arq_DELAY = []
arq_TEMPO = []
arq_RNP = []
arq_TX = []
arq_RX = []

tx_cont = []
rx_cont = []
last_id = []

tx_cont_mac = []
rx_cont_mac = []
last_id_mac = []

tx_cont_rnp = []
rx_cont_rnp = []
last_id_rnp = []
last_end_rnp = []
recv_pck = []

last_id_delay = []
tempos = []

last_id_tempo = []
pri = []
ePri = []

tx_cons = []
rx_cons = []

for node_id in range(1, 1+number_ch):
    arq_PRRMAC.append(open((pasta+"/PRRMAC_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_RNP.append(open((pasta+"/RNP_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    tx_cont_rnp.append(0)
    rx_cont_rnp.append(0)
    last_id_rnp.append("0")
    last_end_rnp.append("0")
    recv_pck.append(False)
    tx_cont_mac.append(0)
    rx_cont_mac.append(0)
    last_id_mac.append("0")

for node_id in range((1+number_ch), number_nodes+(1+number_ch)):
    arq_PRRAPP.append(open((pasta+"/PRRAPP_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_PRRMAC.append(open((pasta+"/PRRMAC_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_DELAY.append(open((pasta+"/DELAY_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_TEMPO.append(open((pasta+"/TEMPO_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_RNP.append(open((pasta+"/RNP_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_TX.append(open((pasta+"/TX_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    arq_RX.append(open((pasta+"/RX_"+filename+"_node"+str(node_id)+".txt"), 'a'))
    tx_cont.append(0)
    rx_cont.append(0)
    last_id.append("0")
    last_id_delay.append("0");
    tempos.append([0,0,0,0,0,0,0,0,0,0])
    pri.append(0)
    ePri.append(True)
    last_id_tempo.append("0")
    tx_cont_rnp.append(0)
    rx_cont_rnp.append(0)
    last_id_rnp.append("0")
    recv_pck.append(False)
    tx_cont_mac.append(0)
    rx_cont_mac.append(0)
    last_id_mac.append("0")
    tx_cons.append(0)
    rx_cons.append(0)    

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
        saida_t = "\r"+str(tempo)
        sys.stdout.write(saida_t)
        
        for node_id in range(1, 1+number_ch):
            #ANALISE PRR MAC
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmitting" and linha[3] == "packet"):
                tx_cont_mac[node_id-1] = tx_cont_mac[node_id-1]+1.0
              #  print linha2
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmitting" and linha[3] == "packet"):
                tx_cont_mac[node_id-1] = tx_cont_mac[node_id-1]+1.0
            #  print linha2
            
            id_ch = 0
            if(linha[1] == "SN.node["+str(id_ch)+"].Communication.MAC" and linha[2] == "Received" and linha[3] == "packet" and linha[9] == str(node_id)):
                #if linha[7] != last_id_mac[node_id-1]:
                rx_cont_mac[node_id-1] = rx_cont_mac[node_id-1]+1.0
                #last_id_mac[node_id-1] = linha[7]
               # print linha2
            
            if tx_cont_mac[node_id-1]%WINDOW == 0 and tx_cont_mac[node_id-1] != 0:
                PRR = float(rx_cont_mac[node_id-1]/tx_cont_mac[node_id-1])
                tx_cont_mac[node_id-1] = 0
                rx_cont_mac[node_id-1] = 0
                #saida = str(tempo) + "\t" + str(PRR)
                saida = str(PRR)+"\n"
                saida = saida.replace(".",",")
                arq_PRRMAC[node_id-1].write(saida)
                #print saida
                
            #ANALISE RNP
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmitting" and linha[3] == "packet"):
                if (recv_pck[node_id-1]):
                    saida = str(tx_cont_rnp[node_id-1])+"\n"
                    saida = saida.replace(".",",")
                    arq_RNP[node_id-1].write(saida)
                    tx_cont_rnp[node_id-1] = 0

                tx_cont_rnp[node_id-1] = tx_cont_rnp[node_id-1]+1.0
                recv_pck[node_id-1] = True
              #  print linha2
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmitting" and linha[3] == "packet"):
                tx_cont_rnp[node_id-1] = tx_cont_rnp[node_id-1]+1.0
            #  print linha2
        
            #id_ch = 0
            #if(linha[1] == "SN.node["+str(id_ch)+"].Communication.MAC" and linha[2] == "Received" and linha[3] == "packet" and linha[9] == str(node_id)):
            #    if linha[7] != last_id_rnp[node_id-1] or linha[13] != last_end_rnp[node_id-1]:
            #        rx_cont_rnp[node_id-1] = rx_cont_rnp[node_id-1]+1.0
            #    last_id_rnp[node_id-1] = linha[7]
            #    last_end_rnp[node_id-1] = linha[13]
               # print linha2
        
            #if rx_cont_rnp[node_id-1]%WINDOW == 0 and rx_cont_rnp[node_id-1] != 0:
            #    RNP = float(tx_cont_rnp[node_id-1]/rx_cont_rnp[node_id-1])
            #    tx_cont_rnp[node_id-1] = 0
            #    rx_cont_rnp[node_id-1] = 0
            #    saida = str(tempo) + "\t" + str(PRR)
            #    saida = str(RNP)+"\n"
            #    saida = saida.replace(".",",")
            #    arq_RNP[node_id-1].write(saida)
                #print saida
        
        for node_id in range((1+number_ch), number_nodes+(1+number_ch)):
            #ANALISE PRR APP
            if(linha[1] == ("SN.node["+str(node_id)+"].Application") and linha[2] == "Sending" and linha[3] == "packet"):
                tx_cont[node_id-(1+number_ch)] = tx_cont[node_id-(1+number_ch)]+1.0
              #  print linha2
            if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
                if linha[4] != last_id[node_id-(1+number_ch)]:
                    rx_cont[node_id-(1+number_ch)] = rx_cont[node_id-(1+number_ch)]+1.0
                last_id[node_id-(1+number_ch)] = linha[4]
               # print linha2
            #print node_id-(1+number_ch)
            if tx_cont[node_id-(1+number_ch)]%WINDOW == 0 and tx_cont[node_id-(1+number_ch)] != 0:
                PRR = float(rx_cont[node_id-(1+number_ch)]/tx_cont[node_id-(1+number_ch)])
                tx_cont[node_id-(1+number_ch)] = 0
                rx_cont[node_id-(1+number_ch)] = 0
                saida = str(PRR)+"\n"
                saida = saida.replace(".",",")
                #print saida
                arq_PRRAPP[node_id-(1+number_ch)].write(saida)
            
            #ANALISE DELAY
            if(linha[1] == ("SN.node["+str(node_id)+"].Application") and linha[2] == "Sending" and linha[3] == "packet"):
                packet_id = int(linha[4])
                tempos[node_id-(1+number_ch)][packet_id%10] = tempo
                  #  print linha2
            if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
                if linha[4] != last_id_delay[node_id-(1+number_ch)]:
                    packet_id = int(linha[4])
                    tempo_tx = tempos[node_id-(1+number_ch)][packet_id%10]
                    delay = tempo - tempo_tx
                    saida = str(delay)+"\n"
                    saida = saida.replace(".",",")
                    #print saida
                    arq_DELAY[node_id-(1+number_ch)].write(saida)
                last_id_delay[node_id-(1+number_ch)] = linha[4]
               # print linha2
           
            #ANALISE TEMPO
            if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
                if linha[4] != last_id_tempo[node_id-(1+number_ch)]:
                    if ePri[node_id-(1+number_ch)]:
                        pri[node_id-(1+number_ch)] = tempo
                        ePri[node_id-(1+number_ch)] = False
                    else:
                        delay_tempo = tempo - pri[node_id-(1+number_ch)]
                        saida = str(delay_tempo)+"\n"
                        saida = saida.replace(".",",")
                        #print saida
                        arq_TEMPO[node_id-(1+number_ch)].write(saida)
                        pri[node_id-(1+number_ch)] = tempo
                last_id_tempo[node_id-(1+number_ch)] = linha[4]
               # print linha2
           
            #ANALISE PRR MAC
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmitting" and linha[3] == "packet"):
              tx_cont_mac[node_id-1] = tx_cont_mac[node_id-1]+1.0
              tx_cons[node_id-(1+number_ch)] = tx_cons[node_id-(1+number_ch)] + 1
            #  print linha2
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmitting" and linha[3] == "packet"):
              tx_cont_mac[node_id-1] = tx_cont_mac[node_id-1]+1.0
              tx_cons[node_id-(1+number_ch)] = tx_cons[node_id-(1+number_ch)] + 1
            #  print linha2

            id_ch = int((node_id-(1+number_ch))/(number_nodes/number_ch))+1
            if(linha[1] == "SN.node["+str(id_ch)+"].Communication.MAC" and linha[2] == "Received" and linha[3] == "packet" and linha[9] == str(node_id)):
              #if linha[7] != last_id_mac[node_id-1]:
              rx_cont_mac[node_id-1] = rx_cont_mac[node_id-1]+1.0
              #last_id_mac[node_id-1] = linha[7]
             # print linha2

            if tx_cont_mac[node_id-1]%WINDOW == 0 and tx_cont_mac[node_id-1] != 0:
              PRR = float(rx_cont_mac[node_id-1]/tx_cont_mac[node_id-1])
              tx_cont_mac[node_id-1] = 0
              rx_cont_mac[node_id-1] = 0
              #saida = str(tempo) + "\t" + str(PRR)
              saida = str(PRR)+"\n"
              saida = saida.replace(".",",")
              arq_PRRMAC[node_id-1].write(saida)
              #print saida

            #ANALISE RNP
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmitting" and linha[3] == "packet"):
                if (recv_pck[node_id-1]):
                    saida = str(tx_cont_rnp[node_id-1])+"\n"
                    saida = saida.replace(".",",")
                    arq_RNP[node_id-1].write(saida)
                    tx_cont_rnp[node_id-1] = 0

                tx_cont_rnp[node_id-1] = tx_cont_rnp[node_id-1]+1.0
                recv_pck[node_id-1] = True
              #  print linha2
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmitting" and linha[3] == "packet"):
                tx_cont_rnp[node_id-1] = tx_cont_rnp[node_id-1]+1.0
                
            #id_ch = 0
            #if(linha[1] == "SN.node["+str(id_ch)+"].Communication.MAC" and linha[2] == "Received" and linha[3] == "packet" and linha[9] == str(node_id)):
             #  if linha[7] != last_id_rnp[node_id-1]:
              #     rx_cont_rnp[node_id-1] = rx_cont_rnp[node_id-1]+1.0
              # last_id_rnp[node_id-1] = linha[7]
              # print linha2

            #if rx_cont_rnp[node_id-1]%WINDOW == 0 and rx_cont_rnp[node_id-1] != 0:
            #   RNP = float(tx_cont_rnp[node_id-1]/rx_cont_rnp[node_id-1])
            #   tx_cont_rnp[node_id-1] = 0
            #   rx_cont_rnp[node_id-1] = 0
               #saida = str(tempo) + "\t" + str(PRR)
            #   saida = str(RNP)+"\n"
            #   saida = saida.replace(".",",")
            #   arq_RNP[node_id-1].write(saida)
               #print saida
               
            #ANALISE RX
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Listening"):
                rx_cons[node_id-(1+number_ch)] = rx_cons[node_id-(1+number_ch)] + 1
                    

except EOFError as e:
    for node_id in range(1, 1+number_ch):
        arq_PRRMAC[node_id-1].close()
        arq_RNP[node_id-1].close()
        
    for node_id in range((1+number_ch), number_nodes+(1+number_ch)):
        arq_TX[node_id-(1+number_ch)].write(str(tx_cons[node_id-(1+number_ch)])+"\n")
        arq_RX[node_id-(1+number_ch)].write(str(rx_cons[node_id-(1+number_ch)])+"\n")
        arq_TX[node_id-(1+number_ch)].close()
        arq_RX[node_id-(1+number_ch)].close()
        arq_PRRAPP[node_id-(1+number_ch)].close()
        arq_DELAY[node_id-(1+number_ch)].close()
        arq_TEMPO[node_id-(1+number_ch)].close()
        arq_PRRMAC[node_id-1].close()
        arq_RNP[node_id-1].close()