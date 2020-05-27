
def ex2(number, array):
    if number>20:
        res = number - 20
        array=res
        while array<number:
            print(array)
            array+=1
    elif number == 20:
        print(0)
    else:
        res = 20 - number #10
        array=res
        while array<20:
            print(array)
            array+=1

num = int(input('Digite o número...   '))
arr = 0

ex2(num, arr)