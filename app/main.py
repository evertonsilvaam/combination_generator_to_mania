from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def raiz():
    return "Olá Mundo"

@app.route('/rota2')
def rota2():
    return "<h1>Rota 2</h1>"

@app.route('/teste/<string:nome>/<string:cidade>')
def rota3(nome, cidade):
    return jsonify({'nome':nome, 'cidade':cidade})

app.run(debug=True)



"""
export FLASK_APP=main.py
flask run
"""