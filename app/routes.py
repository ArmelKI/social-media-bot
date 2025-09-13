from app import app
from flask import render_template, request

#Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

#Route pour la page de connnexion
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Le code pour traiter les données du formulaire sera ici
        username = request.form['username']
        return f"Bonjour {username} ! C'est le début de l'autenthification."
    return render_template('login.html')

# Route pour la page d'inscription
@app.route('/register')
def register():
    return render_template('register.html')
