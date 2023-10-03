from flask import Flask, redirect, render_template, request, url_for, flash
from config import *


con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key = 'root'
def crearTablaPersonas():
    cursor = con_bd.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS personas(
                       id serial NOT NULL,
                       nombre character varying(30),
                       apellido character varying(30),
                       telefono character varying,
                       CONSTRAINT pk_personas_id PRIMARY KEY (id));
                   """)
    con_bd.commit()
@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM personas"
    cursor.execute(sql)
    PersonasRegistradas = cursor.fetchall()
    return render_template('index.html',datos=PersonasRegistradas)

@app.route('/eliminar_persona/<string:id>')
def eliminar(id):
    cursor = con_bd.cursor()
    sql = """
            DELETE FROM personas WHERE id=%s;"""
    cursor.execute(sql,(id,))
    return redirect(url_for('index'))

@app.route('/guardar_personas', methods=['POST'])
def agregarPersona():
 crearTablaPersonas()
 cursor = con_bd.cursor()
 nombre = request.form['nombre']
 apellido = request.form['apellido']
 telefono = request.form['telefono']
 if nombre and apellido and telefono:
     sql="""INSERT INTO personas (nombre , apellido , telefono) VALUES (%s,%s,%s)"""
     cursor.execute(sql,(nombre,apellido,telefono))
     con_bd.commit() 
     flash("Registro guardado correctamente","warning")
     return redirect(url_for('index'))
 else:
     return "Error"
 
@app.route('/editar_persona/<int:id_persona>', methods=['POST'])
def editar(id_persona):
    cursor = con_bd.cursor() 
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    telefono = request.form['telefono']
    if nombre and apellido and telefono:
        sql ="""UPDATE personas SET  nombre=%s,apellido=%s,telefono=%s where id=%s"""
        cursor.execute(sql,(nombre,apellido,telefono,id_persona))
        con_bd.commit()
        return redirect(url_for('index'))
    else:
        return 'error en la consulta'
if __name__== '__main__':
    app.run(debug=True)