import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# 1. Cargar dataset
df = pd.read_csv("LoL_champions.csv")
print("Dataset cargado correctamente")
print(df.head())

# 2. Codificar variable objetivo (Role)
label_encoder = LabelEncoder()
df['Role'] = label_encoder.fit_transform(df['Role'])

# 3. Eliminar roles que solo tengan 1 campeón
role_counts = df['Role'].value_counts()
valid_roles = role_counts[role_counts >= 2].index
df = df[df['Role'].isin(valid_roles)]

print("\nRoles válidos después de limpiar:")
print(label_encoder.inverse_transform(valid_roles))

# 4. Selección de variables numéricas (features)
X = df.select_dtypes(include=['float64', 'int64'])
y = df['Role']

# 5. División de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Modelo Random Forest
rf_model = RandomForestClassifier(n_estimators=300, random_state=42)
rf_model.fit(X_train, y_train)

# 7. Predicciones
y_pred = rf_model.predict(X_test)

# 8. Evaluación
accuracy = accuracy_score(y_test, y_pred)
print("\n✅ Resultados del modelo Random Forest:")
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 9. Importancia de características
importances = rf_model.feature_importances_
feature_importance_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

print("\n🔍 Top características más importantes:")
print(feature_importance_df.head(10))



# Obtener solo los roles con los que sí se entrenó el modelo
unique_roles = np.unique(y)
role_names = label_encoder.inverse_transform(unique_roles)

# Crear la matriz de confusión basada en y_test & y_pred
cm = confusion_matrix(y_test, y_pred, labels=unique_roles)

# Graficar con nombres de roles
fig, ax = plt.subplots(figsize=(12, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=role_names)
disp.plot(xticks_rotation=90, cmap="Blues", ax=ax)

plt.title("Matriz de Confusión - Random Forest (con nombres de roles)")
plt.xlabel("Rol Predicho")
plt.ylabel("Rol Real")
plt.tight_layout()
plt.show()

