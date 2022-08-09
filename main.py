from flask import Flask, render_template

class Fruta:
  def __init__(self, nome, arquivo, texto):
    self.nome = nome
    self.arquivo = arquivo
    self.texto = texto

cagaita = Fruta('Cagaita', 'cagaita.webp', '''
É uma fruta com a casca amarela esverdeada e polpa suculenta e ácida, o que lhe garante um sabor um pouco azedo. Rica em vitaminas do complexo B, vitamina C e niacina, pode ser encontrada nos estados de Goiás, Bahia e Minas Gerais. Pode ser consumida naturalmente.
''')

bacupari = Fruta('Bacupari-do-cerrado', 'bacupari.webp', '''
É uma fruta muito apreciada, mas que é conhecida por poucos. Ela é nativa do vale do são Francisco, do pantanal e do planalto central. É uma fruta que se destaca por sua polpa consistente, mas com um sabor bem adocicado.
''')

pera = Fruta('Pêra-do-cerrado', 'peradocerrado.jpg', '''
Conhecida também como Pêra-do-campo, perinha-do-campo, cabacinha-do-campo ou simplesmente cabacinha, ela se destaca como sendo uma das maiores frutas do cerrado, podendo pesar entre 60 e 90 gramas. Sua casca é bem fininha e a polpa possui um sabor bastante característico, já que é doce e ao mesmo tempo tem um toque azedo.''')

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cagaita')
def pag_cagaita():
  return render_template('fruta.html', fruta=cagaita)

@app.route('/bacupari')
def pag_bacupari():
  return render_template('fruta.html', fruta=bacupari)
  
@app.route('/pera')
def pag_pera():
  return render_template('fruta.html', fruta=pera)

app.run(host='0.0.0.0', port=81)