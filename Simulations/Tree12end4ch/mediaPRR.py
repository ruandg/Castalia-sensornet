media = 0.0
desv = 0.0
qtd = 0
valores = []

try:
    while True:
        valor = raw_input()
        if valor == "":
            continue
        valor = valor.replace(",",".")
        valor = float(valor)
        valores.append(valor)
        qtd = qtd+1
        media = media + valor
             
except EOFError as e:
    saida = ""
    if qtd == 1:
        saida = str(media) + "\t" + "0"
    else:
        #problema qtd pode ser = 0
        if qtd != 0:
            media = media/qtd
        else:
            media = 0
        desvio = 0.0
        for i in range(0,qtd):
            desvio = desvio + pow((valores[i] - media),2)
        desvio = desvio/(qtd-1)
        saida = str(media) + "\t" + str(desvio)
    print saida