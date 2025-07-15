from flask import Flask, render_template

app = Flask(__name__)

# O Flask automaticamente procura os templates na pasta 'templates'
# e os arquivos estáticos (CSS, JS, Imagens) na pasta 'static'.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/solucao')
def solucao():
    return render_template('solucao.html')

@app.route('/lendas')
def lendas():
    return render_template('lendas.html')

@app.route('/escolas')
def escolas():
    return render_template('escolas.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
