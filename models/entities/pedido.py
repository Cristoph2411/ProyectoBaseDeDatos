class Pedido():

    def __init__(self, id, cedula_cliente, cantidad, metodo_pago, observacion, 
                ciudad,  municipio , status, monto_delivery,  total, capture,  fecha):
        
        self.id = id
        self.cedula_cliente = cedula_cliente
        self.cantidad = cantidad
        self.metodo_pago = metodo_pago
        self.observacion = observacion
        self.ciudad = ciudad
        self.municipio = municipio
        self.status = status
        self.monto_delivery = monto_delivery
        self.total = total
        self.capture = capture
        self.fecha = fecha
        
    def to_JSON(self):
    
        return {
            'quantity' : self.cantidad,
            'payment_method' : self.metodo_pago,
            'remarks' : self.observacion,
            'city' : self.ciudad,
            'municipality' : self.municipio,
            'cedula' : self.cedula_cliente,
            'total' : f"{self.total}$",
            'payment_screenshot' : self.capture,
            'status' : self.status,
            'delivery_amount' : f"${self.monto_delivery}",
            'order_number' : str(self.id),
            'datetime' : self.fecha
        }