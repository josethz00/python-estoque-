from utils.modules.config.connection import mycursor, mydb
class DatabaseOperations:

    def index(self):
        mycursor.execute('SELECT * FROM storage')
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

    def store(self):
        query = ('INSERT INTO storage(products, prices, amount) values(%s,%s,%s)')
        product = str(input('Digite o nome do produto...    ')).lower()
        price = float(input('Digite o preço do produto...    '))
        amount = int(input('Digite a quantidade estocada...   '))

        if not product or not price or not amount:
            print('Tente novamente digitando um valor válido')
        
        else:
            values = ( product, price, amount)
            mycursor.execute(query, values)
            mydb.commit()
            print('Registros inseridos')
    
    def update(self):
        self.index()

        code = int(input('Digite o código do produto que deseja atualizar...    '))
        amount = int(input('Quantas unidades estão sendo retiradas...   '))

        qry = "SELECT prices, amount, final_amount, total FROM storage WHERE id = %s"
        val = (code, )

        mycursor.execute(qry, val)
        c = mycursor.fetchall()
        for x in c:
            pr = x[0]
            am = x[1]
            fa = x[2]
            tt = x[3]

        upd_amount = am - amount
        if upd_amount <= 0:
            print('Não foi possível efetuar a venda')
            query = "UPDATE storage SET amount = %s WHERE id = %s "
            values = ('0', code,)
            mycursor.execute(query, values)
            mydb.commit()

            query2 = "UPDATE storage SET final_amount = %s WHERE id = %s "
            fa+=amount
            values2 = (fa, code,)
            mycursor.execute(query2, values2)
            mydb.commit()

            query3 = "UPDATE storage SET total = %s WHERE id = %s "
            tt+=pr
            values3 = (pr, code,)
            mycursor.execute(query3, values3)
            mydb.commit()

            print('Registros atualizados com sucesso!')

        else:
            query = "UPDATE storage SET amount = %s WHERE id = %s "
            values = (upd_amount, code,)
            mycursor.execute(query, values)
            mydb.commit()

            query2 = "UPDATE storage SET final_amount = %s WHERE id = %s "
            fa += amount
            values2 = (fa, code,)
            mycursor.execute(query2, values2)
            mydb.commit()

            query3 = "UPDATE storage SET total = %s WHERE id = %s "
            tt += pr
            values3 = (tt, code,)
            mycursor.execute(query3, values3)
            mydb.commit()

            print('Os Registros foram atualizados com sucesso!')
