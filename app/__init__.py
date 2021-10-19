from flask import Flask, render_template, redirect, request
import Vote

pays = ""
prenom = ""

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('home.html')

    @app.route('/choixpays', methods=['POST'])
    def btn_choix():
        global pays
        pays = str(request.form['pays'])
        print(pays)
        return redirect("prenom")

    @app.route('/prenom/')
    def prenom():
        return render_template('prenom.html')

    @app.route('/prenom/saisieprenom', methods=['POST'])
    def saisieprenom():
        global prenom
        prenom = str(request.form['prenom'])
        print(prenom)
        vote = Vote.Vote(pays, prenom)
        print(vote)
        if vote == None:
            return redirect("votepasok")
        return redirect("voteok")

    @app.route('/prenom/voteok/')
    def voteok():
        return render_template('voteok.html')

    @app.route('/prenom/votepasok/')
    def votepasok():
        return render_template('votepasok.html')

    @app.route('/resultat')
    def resultat():
        resultat = list(Vote.resultat())
        gagnant = resultat[-1]
        japon = resultat[0]["Japon"]
        polynesie = resultat[0]["Polynésie Française"]
        cuba = resultat[0]["Cuba"]
        perou = resultat[0]["Pérou"]
        USA = resultat[0]["USA"]
        argentine = resultat[0]["Argentine"]

        return render_template('resultat.html', gagnant=gagnant, japon=japon, polynesie=polynesie,
                               cuba=cuba, perou=perou, USA=USA, argentine=argentine)

    return app

