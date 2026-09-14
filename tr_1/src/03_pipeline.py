import pandas as pd
import requests


# ==========================================
# 1. Obtener los datos
# ==========================================

url_datos = "https://ourworldindata.org/grapher/refugee-population-by-country-or-territory-of-asylum.csv?v=1&csvType=full&useColumnShortNames=true"

df = pd.read_csv(
    url_datos,
    storage_options={
        "User-Agent": "Our World In Data data fetch/1.0"
    }
)


# ==========================================
# 2. Obtener los metadatos
# ==========================================

url_metadata = "https://ourworldindata.org/grapher/refugee-population-by-country-or-territory-of-asylum.metadata.json?v=1&csvType=full&useColumnShortNames=true"

metadata = requests.get(url_metadata).json()


# ==========================================
# 3. Información del DataFrame
# ==========================================

print("Dimensiones del DataFrame:")
print(df.shape)

print("\nColumnas:")
print(df.columns.tolist())

print("\nTipos de datos:")
print(df.dtypes)

print("\nValores nulos:")
print(df.isnull().sum())


# ==========================================
# 4. Mostrar los primeros registros
# ==========================================

print("\nPrimeros registros:")
print(df.head())


# ==========================================
# 5. Población refugiada promedio por país
# ==========================================

promedio_pais = (
    df.groupby("entity")["refugees"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

print("\nPromedio de población refugiada por país:")
print(promedio_pais)


# ==========================================
# 6. Redondear los resultados
# ==========================================

promedio_pais = promedio_pais.round(2)

print("\nPromedio de población refugiada por país (redondeado):")
print(promedio_pais)


# ==========================================
# 7. Guardar resultado
# ==========================================

archivo_salida = "data/processed/promedio_refugiados.csv"

promedio_pais.to_csv(
    archivo_salida,
    header=["Average refugee population"]
)

print(f"\nArchivo guardado en: {archivo_salida}")