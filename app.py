from flask import Flask, url_for,render_template

app = Flask(__name__)

@app.route('/')
def Accueil():
    return render_template("Index.html")
@app.route('/index')
def Index():
    return render_template('Index.html')

@app.route("/login")
def Login():
    return render_template("login.html")

@app.route("/pharmacie")
def Pharmacie():
    return render_template('pharmacie.html')

@app.route('/profil')
def Profil():
    return render_template('chat.html')

@app.route('/chat')
def Chat():
    return render_template("chat.html")

if __name__ == '__main__':
    app.run(debug=True)
    