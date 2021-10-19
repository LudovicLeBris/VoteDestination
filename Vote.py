import os, json

DATADIR = os.path.join(os.path.dirname(__file__), "data.json")


def Vote(pays, prenom):
    test = os.path.isfile(DATADIR)

    if not test:
        emptydata = {"Japon": [], "Polynésie Française": [], "Cuba": [], "Pérou": [], "USA": [], "Argentine": []}

        with open(DATADIR, "w", encoding="utf-8") as f:
            json.dump(emptydata, f, ensure_ascii=False, indent=4)

    with open(DATADIR, "r", encoding="utf-8") as f:
        data = json.load(f)

    for value in data.values():
        if prenom in value:
            print("Vous avez déja voté")
            return None

    data[pays].append(prenom)

    with open(DATADIR, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return True

def resultat():
    test = os.path.isfile(DATADIR)

    if not test:
        return None

    with open(DATADIR, "r", encoding="utf-8") as f:
        data = json.load(f)

    nb_japon = len(data["Japon"])
    nb_polynesie = len(data["Polynésie Française"])
    nb_cuba = len(data["Cuba"])
    nb_perou = len(data["Pérou"])
    nb_USA = len(data["USA"])
    nb_argentine = len(data["Argentine"])
    resultat = {"Japon": nb_japon, "Polynésie Française": nb_polynesie, "Cuba": nb_cuba,
            "Pérou": nb_perou, "USA": nb_USA, "Argentine": nb_argentine}
    gagnant = max(resultat, key=resultat.get)

    return resultat, str(gagnant)

if __name__ == "__main__":
    print("test")
    # choixpays = "0"
    # while choixpays not in ["1", "2", "3", "4", "5", "6"]:
    #     choixpays = input("Choisissez un pays :\n1) Japon\n2) Polynésie Française\n3) Cuba\n4) Pérou\n5) USA\n6) Argentine\n"
    #                   "Entrez le numéro de votre choix\n")
    # prenom = input("Entrez votre prénom :\n")
    # if choixpays == "1":
    #     pays = "Japon"
    # elif choixpays == "2":
    #     pays = "Polynésie Française"
    # elif choixpays == "3":
    #     pays = "Cuba"
    # elif choixpays == "4":
    #     pays = "Pérou"
    # elif choixpays == "5":
    #     pays = "USA"
    # elif choixpays == "6":
    #     pays = "Argentine"
    #
    # Vote(pays, prenom)
    # input()
    print(resultat())


