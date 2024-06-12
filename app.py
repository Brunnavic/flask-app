from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)


@app.route("/")
def get_list_personagens_page():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", meus_personagens=dict["results"])



@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id 
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)


    return render_template("profile.html", profile=dict)





@app.route("/lista")
def get_list_personagens():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    pessoas_serie = response.read()
    dict = json.loads(pessoas_serie)

    meus_personagens = []

    for personagem in dict["results"]:

        personagem = {
            "name": personagem["name"],
            "status": personagem["status"]
        }

        meus_personagens.append(personagem)

    return {"personagem": meus_personagens}

    

#if __name__ == "__main__":
 #   app.run(debug=True)