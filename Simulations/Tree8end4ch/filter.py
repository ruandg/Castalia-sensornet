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
        if(linha[1] == ("SN.node["+str(node_id)+"].Application") or linha[1] == "SN.node[0].Application" or linha[1] == "SN.node[2].Application"):
            print linha2
        elif(linha[1] == ("SN.node["+str(node_id)+"].Communication.MAC") or linha[1] == "SN.node[0].Communication.MAC" or linha[1] == "SN.node[2].Communication.MAC"):
            print linha2
        elif(linha[1] == ("SN.node["+str(node_id)+"].Communication.Radio") or linha[1] == "SN.node[0].Communication.Radio" or linha[1] == "SN.node[2].Communication.Radio" or linha[1] == "SN.wirelessChannel"):
            print linha2
except EOFError as e:
    print ""