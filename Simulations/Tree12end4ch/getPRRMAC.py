import sys

node_id = int(sys.argv[1])

tx_cont = 0
rx_cont = 0
tx_cont_mac = []
rx_cont_mac = []
last_id_mac = []
tx_cont_mac.append(0)
rx_cont_mac.append(0)
last_id_mac.append("0")
    
WINDOW = 10

#2.535999999997  SN.node[1].Communication.MAC             Transmittiing packet 1 slot: 0 on channel: 0
#661.748799999997SN.node[1].Communication.MAC             Retransmittiing packet 660 slot: 11 on channel: 0
#2.539507999996  SN.node[0].Communication.MAC             Received packet: 1  from: 1

last_id = "0"

toSink = False

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
        if not toSink:
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmitting" and linha[3] == "packet"):
                tx_cont = tx_cont+1.0
                #print linha2
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmitting" and linha[3] == "packet"):
                tx_cont = tx_cont+1.0
            #  print linha2
            id_ch = int((node_id-3)/(8))+1
            
            if(linha[1] == "SN.node["+str(id_ch)+"].Communication.MAC" and linha[2] == "Received" and linha[3] == "packet" and linha[9] == str(node_id)):
                if linha[7] != last_id:
                    rx_cont = rx_cont+1.0
                last_id = linha[7]
                #print linha2
        
            if tx_cont%WINDOW == 0 and tx_cont != 0:
                PRR = float(rx_cont/tx_cont)
                tx_cont = 0
                rx_cont = 0
                saida = str(tempo) + "\t" + str(PRR)
                #saida = str(PRR)
                saida = saida.replace(".",",")
                print saida
        else:
            #ANALISE PRR MAC
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Transmitting" and linha[3] == "packet"):
                tx_cont_mac[node_id-1] = tx_cont_mac[node_id-1]+1.0
                print linha2
            if(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") and linha[2] == "Retransmitting" and linha[3] == "packet"):
                tx_cont_mac[node_id-1] = tx_cont_mac[node_id-1]+1.0
                print linha2
        
            id_ch = 0
            if(linha[1] == "SN.node["+str(id_ch)+"].Communication.MAC" and linha[2] == "Received" and linha[3] == "packet" and linha[9] == str(node_id)):
                #if linha[7] != last_id_mac[node_id-1]:
                rx_cont_mac[node_id-1] = rx_cont_mac[node_id-1]+1.0
                #last_id_mac[node_id-1] = linha[7]
                print linha2
        
            if tx_cont_mac[node_id-1]%WINDOW == 0 and tx_cont_mac[node_id-1] != 0:
                PRR = float(rx_cont_mac[node_id-1]/tx_cont_mac[node_id-1])
                tx_cont_mac[node_id-1] = 0
                rx_cont_mac[node_id-1] = 0
                #saida = str(tempo) + "\t" + str(PRR)
                saida = str(PRR)+"\n"
                saida = saida.replace(".",",")
                print saida
                if(PRR > 1):
                    break
      
            # 4.764507999996  SN.node[0].Communication.MAC             Received packet at sink node: 3 Through:  1 Power: -83.0437 from: 28
             
except EOFError as e:
    print ""