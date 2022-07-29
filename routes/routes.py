import datetime
from flask import Blueprint , jsonify , request
from database.conexion import conex
#entidad
from models.entities.cliente import Cliente
from models.entities.pedido import Pedido

#modelo
from models.cliente_models import Modelo_Cliente
from models.pedido_models import Modelo_Pedido

from utils.utils import Utils

main = Blueprint('blueprint' , __name__)

#crear cliente a la base de datos
@main.route('/' , methods = ['POST'])
def add_cliente():
    try:
        cedula = request.json['cedula']
        nombre = request.json['nombre']
        whatsapp = request.json['whatsapp']
        email = request.json['email']
        
        cliente = Cliente(cedula , nombre , whatsapp , email)
        row_afect = Modelo_Cliente.add_cliente(cliente) 

        if row_afect == 1:
            return '<h2>Cliente Creado con Exitos</h2>'
        else:
            return '<h2>Cliente No Creado , hubo un error</h2>' , 500

    except  Exception as error :
        return jsonify({'error' : str(error)}) , 500

#editar cliente por la cedula
@main.route('/customers/<cedula>' , methods = ['PUT'])
def editar_cliente(cedula):
    try:

        nombre = request.json['nombre']
        whatsapp = request.json['whatsapp']
        email = request.json['email']
        
        cliente = Cliente(cedula , nombre , whatsapp , email)
        row_afect = Modelo_Cliente.editar_cliente(cliente) 

        if row_afect == 1:
            return '<h2>Cliente Editado con Exitos</h2>'
        else:
            return '<h2>Cliente No Editado , hubo un error</h2>' , 500
            
    except  Exception as error :
        return jsonify({'error' : str(error)}) , 500

#mostrar todos los clientes
@main.route('/customers' , methods = ['GET'])
def buscar_cliente():
    try:
        clientes = Modelo_Cliente.buscar_cliente()
        return jsonify(clientes)

    except Exception as error:
        return jsonify( {'error' : str(error)} ) , 500 


#mostrar pedido
@main.route('/orders' , methods = ['GET'])
def get_pedido():

    try:
        pedidos = Modelo_Pedido.mostrar_pedidos()
        return jsonify(pedidos)
        
    except  Exception as error :
        return jsonify({'error' : str(error)}) , 500


#agregar pedido
@main.route('/orders' , methods = ['POST'])
def add_pedido():
    try:
        id = Utils.auto_increment()
        time = datetime.datetime.now()
        fecha = Utils.strtime(time)
        capture = "C://"
        monto_delivery= 2
        status = "pending"
        cantidad = request.json['quantity']
        metodo_pago = request.json['payment_method']
        observacion = request.json['remarks']
        ciudad = request.json['city']
        municipio = request.json['municipality']
        cedula_cliente = request.json['cedula']
        
        
        if str(municipio.upper()) == "MANEIRO":
            monto_delivery = 0
        total = (int(cantidad) * 5) + monto_delivery
        
        
        pedido =   Pedido(int(id) ,cedula_cliente, int(cantidad) ,metodo_pago , observacion , ciudad ,municipio ,status , monto_delivery, total, capture , str(fecha))  
        row_afect = Modelo_Pedido.add_pedido(pedido)  

        if row_afect == 1:
            return '<h2>Pedido Creado con Exitos</h2>'
        else:
            return '<h2>Pedido No Creado , hubo un error</h2>' , 500

    except  Exception as error :
        return jsonify({'error' : str(error)}) , 500


@main.route('/orders/<id>/status'  ,  methods = ['PATCH'])
def update_pedido_status(id):
    try:
        status = request.json['status'] #pedir el status mediante JSON

        pedido = Pedido( id , '' , 0 , '' , '' , '' , '' , status.lower(), 0, 0, '' , '') #los otros datos no importan porque no seran modificados
        row_afect = Modelo_Pedido.update_pedido_status(pedido)

        
        if row_afect == 1:
            return '<h2>STATUS MODIFICADO con Exitos</h2>'
        else:
            return '<h2>STATUS NO MODIFICADO , hubo un error</h2>' , 500

    except  Exception as error :
        return jsonify({'error' : str(error)}) , 500



