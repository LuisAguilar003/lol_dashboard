import pandas as pd
from pymongo import MongoClient
import certifi

# === 1. Leer archivo CSV ===
archivo = "LoL_champions.csv"
df = pd.read_csv(archivo)
print("✅ Archivo CSV cargado correctamente.")
print(df.head())  # mostrar primeras filas para verificar

# === 2. Conectarse a MongoDB Atlas ===
uri = "mongodb+srv://Awilar:1234@cluster0.p3arddl.mongodb.net/?appName=Cluster0"
cliente = MongoClient(uri, tlsCAFile=certifi.where())

# === 3. Seleccionar base y colección ===
db = cliente["league_of_legends"]
coleccion = db["campeones"]

# === 4. Eliminar documentos anteriores ===
coleccion.delete_many({})
print("🧹 Colección limpiada. Datos antiguos eliminados.")

# === 5. Insertar los datos nuevos ===
data = df.to_dict(orient="records")
coleccion.insert_many(data)
print("🚀 Datos actualizados sin duplicados en MongoDB Atlas.")
