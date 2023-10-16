from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("html.html")

"para não ficar o tempo todo parando o codigo coloca app.run(debug=True)" \
"para rodar colocar app.run()"

if __name__ == "__main__":
    app.run(debug=True)
