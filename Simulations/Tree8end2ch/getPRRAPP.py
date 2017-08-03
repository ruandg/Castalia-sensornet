import sys

tx_cont = 0
rx_cont = 0

WINDOW = 10


node_id = int(sys.argv[1])

#2.503553241428  SN.node[1].Application                   Sending packet #1
#2.539507999996  SN.node[0].Application                   Received packet #1 from node 1: -76.8543 23.1457 fromNetworkLayer (olhar duplicacoes)

last_id = "0"

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
        if(linha[1] == ("SN.node["+str(node_id)+"].Application") and linha[2] == "Sending" and linha[3] == "packet"):
            tx_cont = tx_cont+1.0
            print linha2
        if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
            if linha[4] != last_id:
                rx_cont = rx_cont+1.0
            last_id = linha[4]
            print linha2
            
        
        if tx_cont%WINDOW == 0 and tx_cont != 0:
            PRR = float(rx_cont/tx_cont)
            tx_cont = 0
            rx_cont = 0
            saida = str(PRR)
            saida = saida.replace(".",",")
            print saida
            if(PRR > 1):
                quit()
      
             
except EOFError as e:
    print ""