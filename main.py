from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Ruta para servir la página HTML
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para servir el archivo JSON  
@app.route('/cursos.json')
def cursos_json():
    return send_from_directory('static', 'cursos.json')

if __name__ == '__main__':
    app.run(debug=False)
