import sys

node_id = int(sys.argv[1])

tx_cont = 0
rx_cont = 0

WINDOW = 10

#2.503553241428  SN.node[1].Application                   Sending packet #1
#2.539507999996  SN.node[0].Application                   Received packet #1 from node 1: -76.8543 23.1457 fromNetworkLayer (olhar duplicacoes)

last_id = "0"

tempos = [0,0,0,0,0,0,0,0,0,0]

pri = 0
ePri = True

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
        
        if(linha[1] == "SN.node[0].Application" and linha[2] == "Received" and linha[7] == (str(node_id)+":")):
            if linha[4] != last_id:
                if ePri:
                    pri = tempo
                    ePri = False
                else:
                    delay = tempo - pri
                    saida = str(delay)
                    saida = saida.replace(".",",")
                    print saida
                    pri = tempo
            last_id = linha[4]
           # print linha2
            
             
except EOFError as e:
    print ""