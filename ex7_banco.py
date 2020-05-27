from utils.modules.config.connection import mycursor, mydb
from utils.modules.DatabaseOperations import DatabaseOperations


num = 1

db_opr = DatabaseOperations()

print('\n Bem-vindo(a) ao Mercado Dois Irmãos \n')


while num==1:
    st = str(input('Deseja continuar?(S, s/ N, n)'))
    if st in('S', 's', 'Sim', 'y', 'Y'):
        print('Escolha uma opção...')
        choice = str(input('Visualizar, Atualizar, Inserir    ')).lower()
        if choice == 'visualizar':
              db_opr.index()
        elif choice == 'atualizar':
              db_opr.update()
        elif choice == 'inserir':
              db_opr.store()
        else:
              print('Você não digitou nenhuma das opções referidas')
              print('Sessão finalizada!')
              num=0
    else:
        print('Sessão finalizada!')
        mycursor.execute('SELECT SUM(total) FROM storage')
        result = mycursor.fetchall()
        for x in result:
          print('O seu lucro total de hoje foi \n')
          print(x)
          print()
        mycursor.execute('SELECT SUM(final_amount) FROM storage')
        result2 = mycursor.fetchall()
        for x in result2:
          print('Hoje foram efetuadas')
          print(x)
        num=0