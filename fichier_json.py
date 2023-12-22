import json

data = {
    "nom": "Michael",
    "age": 22,
    "ville": "New York"
}

with open("data.json", "w") as fichier_json :
    json.dump(data, fichier_json, indent=2)

with open("data.json", "r") as fichier_json:
    donnes = json.load(fichier_json)
    print("Contenu du fichier initial :")
    print(donnes)

donnes["nationalite"] = "Americaine"

with open("data.json", "w") as fichier_json:
    json.dump(donnes, fichier_json, indent=2)

with open("data.json", "r") as fichier_json:
    donnes_modifies = json.load(fichier_json)
    print("\nContenu du fichier après modification :")
    print(donnes_modifies)