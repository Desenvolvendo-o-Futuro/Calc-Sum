NUMEROS = ["0","1","2","3","4","5","6","7","8","9","."]

#verifica se é um número
def isNumber(valor):
    for caractere in valor:
        if caractere not in NUMEROS:
            return False 
    if valor.count(".") > 1:
        return False
    return True 


def validateNumber(number):
    if not isNumber(number):
        print("você não digitou o numero")
        raise SystemExit(0)
    
if __name__ == "__main__":
    print("Digite um número:")
    primeiroNumero = input()
    validateNumber(primeiroNumero)  
    print("Digite outro número")
    segundoNumero = input() 
    validateNumber(segundoNumero)
    resultado = float(primeiroNumero) + float(segundoNumero)
    print(resultado)