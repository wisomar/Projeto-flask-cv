from flask import Flask, render_template 

app = Flask(__name__)


#route -> williamramos.com/contatos
#função -> o que você quer exibir naquela pagina
#template
@app.route("/")
def homepage():
    return render_template("homepage.html")

#colocar site no ar
if __name__ =="__main__":
    app.run(debug=True)

# deploy para o vercel

#requirement.txt
