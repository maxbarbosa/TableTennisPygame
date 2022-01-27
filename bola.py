#CONTROLANDO A POSIÇÃO DA BOLINHA DURANTE O SAQUE
def B_praCima (y_bolinha, limite):
    y_bolinha -= 5

    if y_bolinha < limite:
        y_bolinha = limite
    
    return y_bolinha

def B_praBaixo (y_bolinha, limite):
    y_bolinha += 5

    if y_bolinha > limite:
        y_bolinha = limite
    
    return y_bolinha

#POSICIONANDO O SAQUE DE ACORDO COM O RESULTADO DO SORTEIO
def posicionarSaque (posicao_seta):
    posicao_saque = []

    if posicao_seta == [850, 15]:
        posicao_saque = [92, 359]
    else:
        posicao_saque = [1005, 359]

    return posicao_saque