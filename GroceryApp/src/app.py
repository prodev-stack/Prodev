from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


#"Configuración inicial de flask y la base de datos"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_llave_secreta_muy_segura'
DATABASE = 'GroceryApp.db'

#"Funciones de la base de datos"
def get_db_connection():
    #"Conexión con la base de datos"
    conn = sqlite3.connect(DATABASE)
    #"Accede a las columnas por sunombre"
    conn.row_factory = sqlite3.Row
    return conn

#"Ruta inicio"
@app.route('/')
def home():
    #"Ruta principal inicio de sesión"
    return render_template('Iniciar_sesión.html')

#"Ruta para registro de usuarios"
@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        #"Para obtener los datos del registro de usuarios"
        nombre = request.form['nombre_completo']
        email = request.form['correo_electronico']
        telefono = request.form['numero_telefono']
        password = request.form['contrasena']

        #"Hashea la contraseña antes de guardarla"
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            #"Inserta el usuario registrado a la tabla"
            cursor.execute(
                "INSERT INTO Usuarios (Nombre_usuario, Correo_electronico, Numero_telefono, Contrasena_hash) VALUES (?, ?, ?, ?)",
                (nombre, email, telefono, hashed_password)
            )
            conn.commit()
            flash('!Cuenta creada exitosamente¡ Ahora puedes iniciar sesión.', 'SUCCES')
        except sqlite3.IntegrityError:
            #"Mensaje flash si el corroe y el número de telefono ya existen por la restricción UNIQUE"
            flash('El correo electronico o el número de celular ya estan registrados', 'ERROR')
        finally:
            conn.close()

    return redirect(url_for('home'))
        
#"Ruta para inicio de sesión"
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.form['correo_electronico_login']
        password = request.form['contrasena_login']

        conn = get_db_connection()
        cursor = conn.cursor()
        #"Busca al usuario por su correo electronico"
        cursor.execute("SELECT * FROM Usuarios WHERE Correo_electronico = ?", (email,))
        user = cursor.fetchone()
        conn.close()

        #"Verificación si el usuario existe y si la contraseña es correcta"
        if user and check_password_hash (user['Contrasena_hash'], password):
            #"Permite guardar información del usuario en la sesión"
            session['user_id'] = user['id']
            session['user_name'] = user['Nombre_usuario']
            #"Dirige a la pantalla de productos si la información es la correcta"
            return redirect(url_for('productos'))
        else:
            #"Si los datos son incorrectos mostrara un mensaje flash de ERROR"
            flash('Correo electronico o contraseña son incorrectos.', 'ERROR')
    return redirect(url_for('home'))
            
#"Ruta para la pantalla productos"
@app.route('/productos')
def productos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id_Productos, Nombre_Producto, Precio_Producto, Url_imagen FROM Productos')
    productos = cursor.fetchall()
    conn.close()
    #"Verificación si el usuario ha iniciado sesión y en caso de que no muestra un mensaje flash solicitando inicio de sesión"
    if 'user_id' not in session:
        flash('Por favor iniciar sesión para acceder.', 'WARNING')
        return redirect(url_for('home'))
    return render_template('Productos.html', productos = productos)

#"Ruta para la pantalla producto e informacion del producto"
@app.route('/produto')
def producto():
    return render_template('producto.html')

#"Ruta comentarios y reseñas"
@app.route('/comentarios')
def comentarios():
    return render_template('comentarios.html')

#"Ruta para la pantalla categorias"
@app.route('/Categorias')
def Categorias():
    return render_template('Categorias.html')

#"Ruta para la pantalla pedidos"
@app.route('/Pedidos')
def Pedidos():
    return render_template('Pedidos.html')

#"Ruta de perfiles"
@app.route('/dashb')
def dashb():
    return render_template('dashb.html')

#"Ruta perfil"
@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

        
if __name__ == '__main__':
    app.run(debug=True,port=5000)