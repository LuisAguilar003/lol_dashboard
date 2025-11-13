from django.shortcuts import render
from pymongo import MongoClient
import os

def lista_campeones(request):
    # URI de conexión (puedes usar variable de entorno o ponerla directamente)
    MONGO_URI = os.environ.get(
        "MONGO_URI",
        "mongodb+srv://Awilar:1234@cluster0.p3arddl.mongodb.net/league_of_legends?retryWrites=true&w=majority"
    )

    # Conectar a MongoDB
    client = MongoClient(MONGO_URI)
    db = client["league_of_legends"]  # nombre de la base
    coleccion = db["campeones"]       # nombre de la colección

    # Obtener todos los documentos
    campeones = list(coleccion.find({}, {"_id": 0}))  # excluir el _id para evitar errores

    for c in campeones:
        nombre = c["Name"].replace(" ", "")
        c["ImageURL"] = f"https://ddragon.leagueoflegends.com/cdn/14.3.1/img/champion/{nombre}.png"
        c["Range_type"] = c.pop("Range type", None)
        c["Resourse_type"] = c.pop("Resourse type", None)
        c["Base_HP"] = c.pop("Base HP", None)


    # Enviar los datos al HTML
    return render(request, "campeones.html", {"campeones": campeones})
