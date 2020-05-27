num = 1

amount = [10, 6, 4, 3, 7]
prices = [100, 540, 90, 30, 25]
products= ['camisa', 'tênis', 'calça', 'camiseta', 'meia']
total = [0, 0]

while num==1:
    st = str(input('Deseja continuar?(S, s/ N, n)'))
    print('')
    if st in('S', 's', 'Sim', 'y', 'Y'):
        pd_id = int(input('Digite o código do produto[1 a 5]...    '))
        if pd_id > 5 or pd_id <=0:
            print('Por favor, só números de 1 a 5!!! \n')
            exit()
        pd_am = int(input('Digite a quantidade que deseja retirar...    '))
        if amount[pd_id-1] == 0:
            print('A compra falhou! \n')
        elif amount[pd_id-1] - pd_am < 0:
            print('A compra falhou! \n')
        else:
            amount[pd_id - 1] -=pd_am
            print(products[pd_id-1].capitalize()  + '        '+ 'R$ ' + str(prices[pd_id-1]) + '      '+ str(amount[pd_id-1]))
            total[0] += pd_am*prices[pd_id-1]
            total[1] += pd_am
    else:
        print('Encerrando sessão...     \n')
        print('O seu lucro hoje foi:       ' +  'R$ ' + str(total[0]) + '\n')
        print('Você efetuou ' + str(total[1]) +' vendas \n')
        num=0