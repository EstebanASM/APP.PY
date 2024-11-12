from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡HOLA SOY ESTEBAN Y ESTE ES MI PROGRAMA EN PYTHON¡"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8083)

