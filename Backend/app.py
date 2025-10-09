from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import text # Importar text para consultas SQL crudas

app = Flask(__name__)
CORS(app)

# ========================================================
#  CONFIGURACIÓN DE LA BASE DE DATOS
# ========================================================
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root@localhost/foro_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# ========================================================
#  MODELO
# ========================================================
class Rol(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    permisos = db.Column(db.String(255))


class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    rol_id = db.Column(db.Integer, db.ForeignKey("roles.id"))


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    contenido = db.Column(db.Text)
    imagen = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))


class Comentario(db.Model):
    __tablename__ = "comentarios"
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))


class Respuesta(db.Model):
    __tablename__ = "respuestas"
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.Text)
    comentario_id = db.Column(db.Integer, db.ForeignKey("comentarios.id"))
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))

@app.route("/insertar_prueba", methods=["GET", "POST"])
def insertar_prueba():
    try:
        # 1. Crear Rol
        rol = Rol(nombre="Administrador", permisos="crear,editar,eliminar")
        db.session.add(rol)
        db.session.commit()

        # 2. Crear Usuario
        usuario = Usuario(nombre="Juan Perez", email="juan@example.com", password="123456", rol_id=rol.id)
        db.session.add(usuario)
        db.session.commit()

        # 3. Crear Post
        post = Post(titulo="Primer Post", contenido="Este es el contenido de prueba", imagen="imagen.png", usuario_id=usuario.id)
        db.session.add(post)
        db.session.commit()

        # 4. Crear Comentario
        comentario = Comentario(contenido="Buen post!", post_id=post.id, usuario_id=usuario.id)
        db.session.add(comentario)
        db.session.commit()

        # 5. Crear Respuesta
        respuesta = Respuesta(contenido="Gracias por comentar!", comentario_id=comentario.id, usuario_id=usuario.id)
        db.session.add(respuesta)
        db.session.commit()

        return jsonify({"status": "ok", "mensaje": "Registros de prueba insertados correctamente"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "detalle": str(e)})


# ========================================================
#  RUTAS
# ========================================================
@app.route("/")
def home():
    return jsonify({"mensaje": "API Flask funcionando 🚀"})

@app.route("/ping")
def ping():
    try:
        db.session.execute(text("SELECT 1"))  # uso correcto de text()
        return jsonify({"status": "ok", "db": "conectado"})
    except Exception as e:
        return jsonify({"status": "error", "detalle": str(e)})
    
@app.route("/usuarios", methods=["GET"])
def get_usuarios():
    try:
        usuarios = Usuario.query.all()
        lista = [
            {
                "id": u.id,
                "nombre": u.nombre,
                "correo": u.email,
                "rol_id": u.rol_id
            }
            for u in usuarios
        ]
        return jsonify({"status": "ok", "usuarios": lista})
    except Exception as e:
        return jsonify({"status": "error", "detalle": str(e)})


# ========================================================
#  MAIN
# ========================================================
if __name__ == "__main__":
    app.run(debug=True)
