from flask import Flask, render_template, request

app = Flask(__name__)


# Ejercicio 1: Cálculo de precio con descuento
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        # Descuento según la edad
        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               total=total_con_descuento)

    return render_template('ejercicio1.html')


# Ejercicio 2: Inicio de sesión
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {"juan": "admin", "pepe": "user"}
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

        return render_template('ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')


# Página principal
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
