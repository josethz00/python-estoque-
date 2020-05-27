def ex5(number):
    if number in(0, 1, 2, 4):
        x = 0
        while x < number:
            if x % 2 == 0:
                print(x)
            x+=1
    else:
        print('O número deve estar entre 0 e 5')


num = int(input('Digite um número entre 0 e 5...     '))


ex5(num)