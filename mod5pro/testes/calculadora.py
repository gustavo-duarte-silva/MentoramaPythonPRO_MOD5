def multiple():
    """
    FUNÇÃO QUE VERIFICA SE O NUMERO NATURAL INSERIDO É MULTIPLO DE 3 E 7
    Se a Saida for fizzbuzz é multiplo de 3 e 7
    Se a saida for fizz é multiplo de 3
    Se a saida for buzz é multiplo de 7
    Se a saida for miss não é multiplo de 3 e 7
    """
    num = int(input('Digite um Numero!'))
    if num%3 == 0 and num%7 == 0:
        print('fizzbuzz')
        return num%3
    elif num%3 == 0:
        print('fizz')
        return num%3
    elif num%7 == 0:
        print('buzz')
        return num%7
    else:
        print('miss')
        return None
