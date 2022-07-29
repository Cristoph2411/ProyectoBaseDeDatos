from flask import Flask
from routes import routes

app=Flask(__name__)
app.secret_key = 'admin12345'


#Por si no encontramos la ruta seleccionada
def manejo_error(error):
    return '<h2>Verifique el url ingresado</h2>', 404



#Arranque de App
if __name__ == '__main__':
    
    #Acceder a dichas rutas con "BLUEPRINTS"
    app.register_blueprint(routes.main)

    #manejo de error
    app.register_error_handler(404 , manejo_error)

    app.run(debug=True) #debug=True para que autoguarde cada cambio..