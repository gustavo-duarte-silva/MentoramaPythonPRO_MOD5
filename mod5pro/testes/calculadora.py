def multiple():
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
