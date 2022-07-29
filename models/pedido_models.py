from database.conexion import conex
from .entities.pedido import Pedido


class Modelo_Pedido:
    @classmethod
    def add_pedido(self, pedido): #agregar un pedido a la BD
             
        try:
            conexion = conex()

            with conexion.cursor() as cursor:

                cursor.execute(" INSERT INTO orders  VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" , (pedido.id , pedido.cedula_cliente, pedido.cantidad, pedido.metodo_pago,  pedido.observacion , pedido.ciudad,  pedido.municipio , pedido.status,  pedido.monto_delivery , pedido.total,  pedido.capture,  pedido.fecha) )
                row_afect =  cursor.rowcount
                conexion.commit()
            
            conexion.close()
            return row_afect

        except Exception as ex:
            raise Exception(ex)

    @classmethod 
    def mostrar_pedidos(self): # mostrar datos
        try:
            conexion = conex() 
            pedidos = [] 

            with conexion.cursor() as cursor:
                cursor.execute( "SELECT * FROM orders")
                resulta = cursor.fetchall()

                for row in resulta: 
                    pedido = Pedido(row[0] , row[1] , row[2] , row[3] ,row[4] , row[5] , row[6] , row[7] , row[8] , row[9] , row[10] , row[11])
                    pedidos.append(pedido.to_JSON()) 

                conexion.close()
                return pedidos

        except Exception as ex:
            raise Exception(ex)

    #editar status
    @classmethod
    def update_pedido_status(sef , pedido):
        try:
            conexion = conex() 

            with conexion.cursor() as cursor:
                cursor.execute("""UPDATE orders SET status = %s 
                               WHERE id = %s""", (pedido.status , pedido.id)) 

                fila_afectada = cursor.rowcount  
                conexion.commit()
            
            conexion.close()
            return fila_afectada

        except Exception as ex :
            raise Exception(ex)