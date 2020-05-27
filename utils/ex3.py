
def ex3(number, number2):
    res = abs(number - number2)
    while res<number:
        print(res)
        res+=1


num = int(input('Digite o número...   '))
arr = int(input('Digite o número 2...   '))

ex3(num, arr)