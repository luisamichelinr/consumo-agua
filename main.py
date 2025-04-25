from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular_agua', methods=['POST'])
def calcular_agua():
    try:
        peso = float(request.form['peso'])
        qtd = (peso * 35) / 1000
        return render_template('index.html', qtd = qtd)
    except Exception as e:
        qtd = f"Ocorreu um erro inesperado {e}"
        return render_template('index.html', qtd = qtd)

if __name__ == '__main__':
    app.run(debug=True)
