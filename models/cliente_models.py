from database.conexion import conex
from .entities.cliente import Cliente

class Modelo_Cliente():
    @classmethod
    def add_cliente(sef  ,  cliente): #Crear Cliente a la Base De Datos
        try:
            conexion = conex()

            with conexion.cursor() as cursor:
                cursor.execute("INSERT INTO customer VALUES ( %s , %s  , %s , %s )"  , (cliente.cedula ,cliente.nombre , cliente.whatsapp , cliente.email ))
                fila_afectada = cursor.rowcount
                conexion.commit()#guardar
            conexion.close()

            return fila_afectada

        except Exception as ex:
            raise Exception(ex)


    @classmethod
    def editar_cliente(self , cliente): #editar cliente
        try:
            conexion =  conex()

            with conexion.cursor() as cursor:
                cursor.execute("""UPDATE customer SET nombre = %s ,  whatsapp= %s  , email= %s WHERE cedula = %s"""  , (cliente.nombre , cliente.whatsapp , cliente.email , cliente.cedula ))
                fila_afectada = cursor.rowcount
                conexion.commit() 
            conexion.close()

            return fila_afectada

        except Exception as ex  :
            raise Exception(ex)

    @classmethod 
    def buscar_cliente(self): #mostrar clientes
        try:
            conexion = conex()
            clientes = []

            with conexion.cursor() as cursor:
                cursor.execute( "SELECT * FROM customer" )
                result_busqueda = cursor.fetchall() #todos los datos

                for i in result_busqueda: 
                    customer = Cliente(i[0] , i[1] , i[2] , i[3])
                    clientes.append(customer.to_JSON())
                conexion.close()

                return clientes #nos retorna un JSON

        except Exception as ex:
            raise Exception(ex)