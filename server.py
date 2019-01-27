from flask import Flask
app = Flask(__name__)

abrir_arquivo = open("curriculo.html", "r")
index = abrir_arquivo.read()
abrir_arquivo.close()

@app.route("/")
def serve_index():
    return index