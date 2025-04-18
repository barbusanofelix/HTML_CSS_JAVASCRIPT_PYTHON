#Importa la clase Flask desde la biblioteca Flask. Es esencial para crear una aplicación web con Flask.
from django.conf.global_settings import SECRET_KEY

from flask import Flask, render_template, url_for, redirect
from cliente_dao import ClienteDAO
from clientes import Cliente
from cliente_forma import ClienteForma

#Basicamente, inicializa la aplicación Flask, creando una instancia de Flask en app
app = Flask(__name__)   # Asociamos app con una instancia de Flask

app.config['SECRET_KEY'] = 'llave_secreta'   # Ojo: SECRET_KEY entre comillas.

titulo_app="Zona Fit (GYM)"

""" 
Define el localHost de Flask  ( El new * aparece al colocar el @ y no se puede borrar)
"""

@app.route('/')  #url: http://localhost:5000/
@app.route('/index.html')
def inicio():
    app.logger.debug('Entramos al path de inicio /')   # Envia info a la consola
    # recuperamos los clientes de la base de datos
    cliente_db=ClienteDAO.seleccionar()
    # Crear un objeto de cliente form vacío
    cliente=Cliente()  # Como el constructor de Cliente() es None, por defecto, para un cliente nuevo
    # Creamos un objeto cliente Forma y le asignamos un cliente
    cliente_forma=ClienteForma(obj=cliente) # Crea un objeto con el cliente vacio, porque cliente esta iniciado en None en sus campos
    # for c in cliente_db:
    #     print(c.id)
    return render_template('index.html',titulo=titulo_app, clientes=cliente_db, forma=cliente_forma)               # Busca y ejecuta a index.html dentro de la carpeta Templates

@app.route('/guardar',methods=['POST'])
def guardar():
    # Creamos los objetos de cliente , inicialmente vacío.
    cliente= Cliente()
    cliente_forma=ClienteForma(obj=cliente)
    if cliente_forma.validate_on_submit():
        # Llenamos el objeto cliente con los valores del formulario
        # En proxima, tambien se recupera el id oculto en el formulario
        cliente_forma.populate_obj(cliente) # populate se encarga de llenar cada campo segun corresponde.
        # Guardamos el nuevo cliente en la bd
        if not cliente.id:  # Si no hay un valor de id significa que el cliente es nuevo
            ClienteDAO.insertar(cliente)
        else: # El id tiene un valor, entonces significa que lo estamos editando
            ClienteDAO.actualizar(cliente)    # Enviamos los datos para que actualice
    # Redireccionamos a la pagina de inicio para que muestre bd actualizada
    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/editar/<int:id>')   #localhost:5000/editar/id   donde el id sera el numero del registro
def editar(id):
    # Cliente seleccionado en la web y lo recuperamos de la bd
    cliente=ClienteDAO.seleccionar_por_id(id)
    # añadimos el cliente al formulario de la web
    cliente_forma=ClienteForma(obj=cliente)
    # recuperamos todos los clientes para volver a mostrarlos
    cliente_db=ClienteDAO.seleccionar()
    return render_template('index.html',titulo=titulo_app,
                           clientes=cliente_db, forma=cliente_forma)

@app.route('/eliminar/<int:id>')
def confirmar_eliminar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    if cliente:
        return render_template('confirmar_eliminar.html', cliente=cliente)
    else:
        # Manejar el caso en que el cliente no existe (opcional)
        return redirect(url_for('inicio'))

@app.route('/eliminar_confirmado/<int:id>', methods=['POST'])
def eliminar_confirmado(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    if cliente:
        ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

if __name__=='__main__':
    app.run(debug=True)     # cambios se reflejan de manera automática