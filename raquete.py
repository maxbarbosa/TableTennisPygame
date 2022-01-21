#CONTROLANDO AS AÇÕES DA RAQUETE
def R_praCima(y_rqt, limite):
    y_rqt -= 5

    if y_rqt < limite:
        y_rqt = limite
    
    return y_rqt

def R_praBaixo(y_rqt, limite):
    y_rqt += 5

    if y_rqt > limite:
        y_rqt = limite
    
    return y_rqt

def R_praEsquerda(x_rqt, limite):
    x_rqt -= 5

    if x_rqt < limite:
        x_rqt = limite
    
    return x_rqt

def R_praDireita(x_rqt, limite):
    x_rqt += 5

    if x_rqt > limite:
        x_rqt = limite
    
    return x_rqt