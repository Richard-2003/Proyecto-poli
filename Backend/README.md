# Instalación y Ejecución del Backend (Flask + MySQL)
Requisitos
- Python 3.8 o superior
- XAMPP (con MySQL corriendo)
- Base de datos creada: foro_db


1. Instalar dependencias necesarias
Ejecuta dentro de la carpeta Backend en la terminal:
pip install flask flask_sqlalchemy flask_cors pymysql

2. Configurar la base de datos
Asegúrate de que el servidor MySQL esté activo en XAMPP
y que exista la base de datos foro_db.


3. Configurar conexión en main.py
Verifica que la línea en tu código esté igual:
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/foro_db"
Si tu MySQL usa contraseña, agrega:
"mysql+pymysql://root:TU_PASSWORD@localhost/foro_db"

4. Ejecutar la API
Con el entorno activado y estando dentro de la carpeta del backend, corre:
python main.py
Verás algo como:
 * Running on http://127.0.0.1:5000

5. Probar funcionamiento
Abre en tu navegador o usa Postman:
- API activa:
http://127.0.0.1:5000/
- Probar conexión BD:
http://127.0.0.1:5000/ping
- Insertar datos de prueba:
http://127.0.0.1:5000/insertar_prueba
- Ver usuarios registrados:
http://127.0.0.1:5000/usuarios
