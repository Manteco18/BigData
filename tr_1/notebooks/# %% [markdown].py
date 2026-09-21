# %% [markdown]
# # Examen Práctico Topicos de Big Data - 1er Parcial

# %% [markdown]
# Tópicos de Big Data
# Instrucciones generales
# 
# Este notebook es tu entregable. Complétalo en orden, sin borrar los enunciados.
# Al final debes subir este archivo (.ipynb) al repositorio de GitHub del curso, en la carpeta correspondiente a tu nombre/usuario.
# Se evaluará tanto el código (que corra sin errores, de arriba hacia abajo) como tus interpretaciones escritas en las celdas de texto marcadas como "Interpretación".
# Cada quien trabaja con un dataset distinto, asignado por la profesora. No copies celdas de un compañero con un dataset diferente: aunque las preguntas se parecen, los datos y las columnas no son las mismas.

# %% [markdown]
# # 0. Datos del alumno
# Completa la siguiente celda con tus datos y el nombre del dataset que te fue asignado.

# %%
# --- COMPLETA CON TUS DATOS ---
NOMBRE = "Osmar"            # Tu nombre completo
MATRICULA = "81739"         # Tu matrícula o número de cuenta
DATASET_ASIGNADO = "PIB"  # Debe ser uno de: "alcohol", "migracion", "desnutricion", "pib", "homicidios"

print(f"Alumno: {NOMBRE}")
print(f"Matrícula: {MATRICULA}")
print(f"Dataset asignado: {DATASET_ASIGNADO}")


# %% [markdown]
# # 1. Configuración del entorno virtual (Visual Studio Code)
# Antes de instalar librerías directamente en tu sistema, es una buena práctica crear un entorno virtual exclusivo para este examen. Esto evita conflictos de versiones con otros proyectos y hace que tu entorno de trabajo sea reproducible.
# 
# Requisitos previos en VS Code: ten instaladas las extensiones oficiales "Python" y "Jupyter" (ambas de Microsoft), disponibles en la pestaña de Extensiones (ícono de cuadritos en la barra lateral izquierda, o Ctrl+Shift+X / Cmd+Shift+X).
# 
# Abre una terminal dentro de VS Code (menú Terminal → New Terminal, o Ctrl+ñ/Ctrl+`) y verifica que estés ubicado en la carpeta de tu repositorio del curso (donde vas a guardar este notebook).

# %% [markdown]
# # 1. Crear el entorno virtual (se creará una carpeta llamada ".venv")
# python -m venv .venv
# 
# # 2. Activar el entorno virtual
# .venv\Scripts\Activate.ps1
# 
# # Si PowerShell bloquea la ejecución de scripts, ejecuta una sola vez:
# #   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
# # y vuelve a intentar activar el entorno.
# 
# # 3. Instalar las librerías necesarias
# pip install pandas numpy ipykernel matplotlib requests

# %%
import sys
print(sys.executable)
# Debe mostrar una ruta dentro de tu carpeta "venv" (o de tu entorno "examen-bigdata" si usas conda).
# Si muestra la ruta de tu instalacion global de Python, regresa al paso anterior
# y selecciona el kernel correcto antes de continuar.


# %% [markdown]
# # 2. Configuración y carga de datos
# La siguiente celda no se modifica. Contiene la configuración de los 5 datasets posibles del examen. A partir de tu variable DATASET_ASIGNADO de la celda anterior, el notebook cargará automáticamente el dataset y los metadatos que te corresponden.

# %%
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASET_ASIGNADO = "pib"
# --- NO MODIFICAR: configuración de los 5 datasets del examen ---
DATASETS = {
    "pib": {
        "csv": "https://ourworldindata.org/grapher/gdp-per-capita-worldbank-constant-usd.csv?v=1&csvType=full&useColumnShortNames=true",
        "meta": "https://ourworldindata.org/grapher/gdp-per-capita-worldbank-constant-usd.metadata.json?v=1&csvType=full&useColumnShortNames=true",
        "valor_col": "ny_gdp_pcap_kd",
        "filtro_paises": "code",
        "descripcion": "PIB per capita (dolares constantes de 2015)",
        "unidad": "USD",
    }
}

assert DATASET_ASIGNADO in DATASETS, (
    "DATASET_ASIGNADO debe ser uno de: " + ", ".join(DATASETS.keys())
)

config = DATASETS[DATASET_ASIGNADO]
print(f"Cargando dataset: {DATASET_ASIGNADO}")
print(f"Descripcion: {config['descripcion']} ({config['unidad']})")


# %%
df = pd.read_csv(
    config["csv"],
    storage_options={'User-Agent': 'Our World In Data data fetch/1.0'}
)

metadata = requests.get(config["meta"]).json()

df = df.rename(columns={config["valor_col"]: "valor"})

# %%
df.head(25)

# %% [markdown]
# # 3. Exploración inicial
# Antes de responder las preguntas de análisis, explora el dataset: tipos de datos, dimensiones, valores nulos y estadísticas descriptivas básicas.

# %%
# Forma del dataset (filas, columnas)
df.shape

# %%
# Tipos de datos e informacion general
df.info()

# %%
# Estadisticas descriptivas de la columna 'valor'
df['valor'].describe()

# %%
# Conteo de valores nulos por columna
df.isnull().sum()

# %% [markdown]
# Interpretación (2-3 líneas): ¿qué observas sobre los valores nulos, el rango de años y el tipo de variable con la que vas a trabajar?
# : Se observa que no existen algunos valores nulos en la variable valor, por lo que deben considerarse antes del análisis.

# %% [markdown]
# # 4. Preguntas de análisis
# A continuación responde las 10 preguntas.
# 
# Cada una tiene una celda de código para su solución y, cuando aplica, una celda de texto para tu interpretación. Recuerda que tu dataset (DATASET_ASIGNADO) puede o no tener la columna owid_region; revisa el diccionario DATASETS de la celda de configuración para saber qué columna (code u owid_region) te toca usar para distinguir países reales de agregados (continentes, "World", grupos de ingreso, etc.).

# %% [markdown]
# # Pregunta 1 — Filtrado de países reales y ranking
# Filtra el DataFrame para quedarte solo con países reales (usa la columna indicada en config['filtro_paises'] de tu dataset). Guarda el resultado en una nueva variable df_paises. ¿Cuántos países distintos hay? Muestra los 10 países con mayor valor y los 10 con menor valor.

# %%
df.head(5)

# %%
# Pregunta 1
# Tu codigo aqui
# Filtrar únicamente países reales
df_paises = df[df[config["filtro_paises"]].notna()].copy()

# Número de países distintos
num_paises = df_paises["entity"].nunique()

print("Número de países distintos:", num_paises)

# 10 países con mayor valor
print("\n10 países con mayor valor:")
print(df_paises.nlargest(10, "valor")[["entity", "year", "valor"]])

# 10 países con menor valor
print("\n10 países con menor valor:")
print(df_paises.nsmallest(10, "valor")[["entity", "year", "valor"]])

# %% [markdown]
# # Pregunta 2 — Filtro por país y rango de años
# Elige dos paises (Mexico y algún otro de tu interés) y filtra df_paises para mostrar únicamente su información dentro del rango de años disponible para ambos.

# %%
Mexico_df = df[df["entity"] == "Mexico"].copy()

Japon_df = df[df["entity"] == "Japan"].copy()

print("\nMexico valor:")
print(Mexico_df[["entity", "year", "valor"]])

print("\nJapon valor:")
print(Japon_df[["entity", "year", "valor"]])

# %% [markdown]
# # Pregunta 3 — Comparación entre países
# Elige 5 países de tu interés (de distintos continentes) y compara el valor de tu indicador en el año más reciente disponible. ¿Cuál tiene el valor más alto y cuál el más bajo? Calcula la diferencia entre ambos.

# %%
# Países seleccionados
paises = ["Mexico", "Japan", "Germany", "Nigeria", "Australia"]

# Filtrar los países
comparacion = df[df["entity"].isin(paises)].copy()

# Obtener el año más reciente disponible
anio_reciente = comparacion["year"].max()

# Filtrar únicamente ese año
comparacion_reciente = comparacion[
    comparacion["year"] == anio_reciente
][["entity", "year", "valor"]]

# Ordenar de mayor a menor
comparacion_reciente = comparacion_reciente.sort_values(
    by="valor", ascending=False
)

print("Comparación entre países en el año más reciente:")
print(comparacion_reciente)

# País con valor más alto
mayor = comparacion_reciente.iloc[0]

# País con valor más bajo
menor = comparacion_reciente.iloc[-1]

# Diferencia
diferencia = mayor["valor"] - menor["valor"]

print("\nPaís con el valor más alto:")
print(mayor)

print("\nPaís con el valor más bajo:")
print(menor)

print("\nDiferencia entre ambos:")
print(diferencia)

# %% [markdown]
# # Pregunta 4 — Comparación entre grupos
# Define dos grupos de países, el primero "latinoamerica" con Mexico, Colombia y Argentina, y el segundo "Asia" con China, Japon y Vietnam ( si algun pais no tiene informacion disponible, sustitúyelo por algún otro) y calcula el promedio de tu indicador en el año más reciente disponible.

# %%
latinoamerica = ["Mexico", "Argentina", "Colombia"]
Asia = ["Japan", "China", "Vietnam"]

latinoamerica_df = df[df["entity"].isin(latinoamerica)].copy()
#promedio de latinoamerica
promedio_latinoamerica = latinoamerica_df.groupby("year")["valor"].mean().reset_index()
print(promedio_latinoamerica)
Asia_df = df[df["entity"].isin(Asia)].copy()
#promedio de Asia
promedio_Asia = Asia_df.groupby("year")["valor"].mean().reset_index()
print(promedio_Asia)


# %% [markdown]
# # Pregunta 5 — Tendencia temporal de un país
# Para un país de tu elección, analiza cómo cambió tu indicador a lo largo del tiempo disponible en el dataset. ¿En qué año tuvo su valor máximo y en cuál el mínimo? ¿La tendencia general es creciente, decreciente o fluctuante?

# %%
Mexico_df = df[df["entity"] == "Mexico"].copy()

# Ordenar por año
Mexico_df = Mexico_df.sort_values("year")

print("Valores de México a lo largo del tiempo:")
print(Mexico_df[["entity", "year", "valor"]])

# Año con valor máximo
maximo = Mexico_df.loc[Mexico_df["valor"].idxmax()]

# Año con valor mínimo
minimo = Mexico_df.loc[Mexico_df["valor"].idxmin()]

print("\nValor máximo:")
print(f"Año: {maximo['year']}, Valor: {maximo['valor']}")

print("\nValor mínimo:")
print(f"Año: {minimo['year']}, Valor: {minimo['valor']}")

# %% [markdown]
# # Pregunta 6 — Cambio porcentual
# Para Mexico, calcula el cambio porcentual entre el primer y el último año con datos disponible. ¿presenta un incremento relativo o una caída? En tus palabras, ¿a qué crees que se debe el resultado?

# %%
### Pregunta 6 — Cambio porcentual

Mexico_df = df[df["entity"] == "Mexico"].copy()

# Ordenar por año
Mexico_df = Mexico_df.sort_values("year")

# Primer y último dato
primer_valor = Mexico_df.iloc[0]["valor"]
ultimo_valor = Mexico_df.iloc[-1]["valor"]

primer_anio = Mexico_df.iloc[0]["year"]
ultimo_anio = Mexico_df.iloc[-1]["year"]

# Calcular cambio porcentual
cambio_porcentual = ((ultimo_valor - primer_valor) / primer_valor) * 100

print(f"Primer año: {primer_anio}")
print(f"Primer valor: {primer_valor}")

print(f"\nÚltimo año: {ultimo_anio}")
print(f"Último valor: {ultimo_valor}")

print(f"\nCambio porcentual: {cambio_porcentual:.2f}%")

if cambio_porcentual > 0:
    print("Presenta un incremento relativo.")
elif cambio_porcentual < 0:
    print("Presenta una caída.")
else:
    print("No presenta cambios.")

# %% [markdown]
# # Pregunta 7 — Estadísticas descriptivas con NumPy
# Usando NumPy (no .describe() de pandas), calcula la media, la mediana y la desviación estándar de tu columna valor entre todos los países reales, para el año más reciente disponible. Recuerda filtrar los NaN antes de calcular.

# %%
import numpy as np

# Año más reciente disponible
anio_reciente = df["year"].max()

# Filtrar el año más reciente
datos_recientes = df[df["year"] == anio_reciente].copy()

# Eliminar NaN de la columna valor
valores = datos_recientes["valor"].dropna().to_numpy()

# Estadísticas con NumPy
media = np.mean(valores)
mediana = np.median(valores)
desviacion = np.std(valores)

print("Año más reciente:", anio_reciente)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion)

# %% [markdown]
# # Pregunta 8 — Visualización de tendencia
# Crea una gráfica de líneas con matplotlib que muestre la evolución de tu indicador a lo largo del tiempo para 3 países de tu elección, en una sola figura, con título, etiquetas de ejes y leyenda.

# %%
# Seleccionar 3 países
paises = ["Mexico", "Japan", "Germany"]

# Filtrar los datos
datos = df[df["entity"].isin(paises)].copy()

# Ordenar por año
datos = datos.sort_values("year")

# Crear gráfica
plt.figure(figsize=(10, 6))

for pais in paises:
    pais_df = datos[datos["entity"] == pais]
    plt.plot(
        pais_df["year"],
        pais_df["valor"]       
    )

# Título y etiquetas
plt.title("Evolución del indicador en México, Japón y Alemania")
plt.xlabel("Año")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

plt.show()

# %% [markdown]
# # Pregunta 9 — Visualización integradora
# Crea dos gráficas de barras (horizontales o verticales) con el Top 10 de países según tu indicador en la primera consulta el año de tu nacimiento, y en la segunda el año 2023, ordenados de mayor a menor. Qué movimientos hubo en ambas gráficas? Agrega título y etiquetas de ejes.

# %%
datos_2005 = df[df["year"] == 2005].copy()
datos_2023 = df[df["year"] == 2023].copy()

# Top 10 de cada año

top10_2005 = datos_2005.nlargest(10, "valor").sort_values("valor")
top10_2023 = datos_2023.nlargest(10, "valor").sort_values("valor")


plt.figure(figsize=(10, 6))

plt.barh(top10_2005["entity"], top10_2005["valor"])

plt.title("Top 10 países según el indicador — 2005")
plt.xlabel("Valor")
plt.ylabel("País")
plt.grid(axis="x")

plt.show()


plt.figure(figsize=(10, 6))

plt.barh(top10_2023["entity"], top10_2023["valor"])

plt.title("Top 10 países según el indicador — 2023")
plt.xlabel("Valor")
plt.ylabel("País")
plt.grid(axis="x")

plt.show()



# %% [markdown]
# # 5. Conclusión general
# En 5 - 10 líneas, resume qué aprendiste sobre el dataset que te tocó trabajar: ¿qué patrones encontraste?, ¿qué limitaciones tiene la información (por ejemplo, valores absolutos sin normalizar por población, datos faltantes, etc.)?, ¿qué harías distinto si tuvieras más tiempo?

# %% [markdown]
# Durante el análisis del dataset aprendí a trabajar y comparar los valores de un indicador entre diferentes países y años.
# Encontré que los valores presentan variaciones importantes entre países y que algunos muestran tendencias crecientes mientras otros presentan cambios fluctuantes.


