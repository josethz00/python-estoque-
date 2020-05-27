
def ex6(number):
    if number>20:
        while number>1:
            print(number)
            number-=1
    else:
        print('O número de entrada deve ser maior que 20')


num = int(input('Digite o número...   '))

ex6(num)