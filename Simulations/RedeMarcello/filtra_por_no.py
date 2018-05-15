node_id = 5
cluster_id = 2
try:
    while True:
        linha = raw_input()
        linha = linha.replace("SN"," SN")
        linha = linha.replace("dBm", " dBm")
        if linha == "":
            continue
            
        linha1 = linha.split()
        #print linha1[1][:11]
        if(linha1[1] == "SN.wirelessChannel" or linha1[1][:11] == ("SN.node["+str(node_id)+"].") or linha1[1][:11] == ("SN.node["+str(cluster_id)+"].") or linha1[1][:11] == "SN.node[0]."):
            print linha
    
except EOFError as e:
    print ""