from pymongo import MongoClient
import pandas as pd

# === 1️⃣ Conectarse a MongoDB Atlas ===
# Usa el mismo enlace que ya funcionó antes
uri = "mongodb+srv://Awilar:1234@cluster0.p3arddl.mongodb.net/?appName=Cluster0"
cliente = MongoClient(uri)

# === 2️⃣ Seleccionar base y colección ===
db = cliente["league_of_legends"]
coleccion = db["campeones"]

# === 3️⃣ Obtener algunos documentos ===
campeones = list(coleccion.find().limit(25))  # Muestra solo los primeros 10
df = pd.DataFrame(campeones)

# === 4️⃣ Mostrar en pantalla ===
print(" Campeones obtenidos desde MongoDB Atlas:")
print(df[["Name", "Tags", "Role", "Attack damage", "Attack speed"]])
