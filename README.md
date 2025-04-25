# 🎧 RecTuneAI - Sistema de Recomendación Musical basado en Spotify Charts

RecTuneAI es una aplicación interactiva desarrollada con Python y Streamlit que permite analizar tendencias musicales globales y generar recomendaciones personalizadas. Utiliza datos reales del ranking Top 200 de Spotify para ofrecer insights musicales a partir de cinco enfoques distintos: tendencias por país, popularidad, similitud de usuarios, evolución temporal y búsqueda personalizada.

---

## 📑 Índice

1. [Descripción del Proyecto](#-descripción-del-proyecto)
2. [Descripción de las columnas](#-descripción-de-las-columnas)
3. [Demo](#-demo)
4. [Instalación](#-instalación)
5. [Estructura del Proyecto](#-estructura-del-proyecto)
6. [Uso de la Aplicación](#-uso-de-la-aplicación)
7. [Funcionalidades](#-funcionalidades)
8. [Dataset](#-dataset)
9. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
10. [Contribuciones](#-contribuciones)
11. [Licencia](#-licencia)

---

## 📌 Descripción del Proyecto

**RecTuneAI** es una aplicación interactiva desarrollada con Python y Streamlit que analiza tendencias musicales globales usando datos reales de Spotify Charts. El sistema permite explorar, visualizar y generar recomendaciones musicales personalizadas a partir de múltiples enfoques: popularidad por país, estado de ánimo, similitud entre canciones y artistas, evolución en el tiempo y más.

La app está pensada tanto para amantes de la música como para analistas de datos que quieran entender mejor el comportamiento musical global.

---

## 🧾 Descripción de las Columnas

| Columna    | Descripción |
|------------|-------------|
| **title**  | Nombre de la canción. |
| **rank**   | Posición de la canción en el ranking diario (1 es la más popular). |
| **date**   | Fecha en la que la canción aparece en el ranking (formato `YYYY-MM-DD`). |
| **artist** | Nombre del/los artista/s de la canción. |
| **url**    | Enlace directo a la canción en Spotify. |
| **region** | País o región a la que pertenece el ranking. |
| **chart**  | Tipo de lista, puede ser:<br>• `top200`: canciones más reproducidas.<br>• `viral50`: canciones virales con mayor crecimiento. |
| **trend**  | Movimiento de la canción respecto al día anterior:<br>• `SAME_POSITION`: Mismo puesto.<br>• `MOVE_UP`: Subió posiciones.<br>• `MOVE_DOWN`: Bajó posiciones.<br>• `NEW_ENTRY`: Nueva entrada en el ranking. |
| **streams**| Número de reproducciones diarias en esa región (solo disponible para `top200`).<br>⚠️ Para `viral50`, este valor es `NULL`. |

--- 

## 🎥 Demo

> Próximamente: incluye aquí un enlace a un video o captura de pantalla con tu app funcionando.

---

## ⚙️ Instalación

```bash
# Clona el repositorio
git clone https://github.com/carlotaGP/RecTuneAI.git
cd RecTuneAI

# Entorno
Crear y configurar entorno con Conda
  conda create --n env
  conda activate env
  conda env create -f environment.yml

Si prefires usar pip para el entorno
  pip install -r requirements.txt

# Ejecuta la app
streamlit run app.py
```
---

## 📁 Estructura del Proyecto

---

## 🧭 Uso de la Aplicación

Aquí irá una explicación de cómo usar la app: seleccionar país, explorar charts, generar recomendaciones, etc.

---

## 🎯 Funcionalidades

- Recomendación de canciones por país y tendencias globales.
- Playlist dinámica por mood y nivel de popularidad.
- Recomendación colaborativa simplificada (usuarios ficticios).
- Análisis de evolución musical por artista y región.
- Buscador + sistema de recomendación personalizada.

---

## 📊 Dataset

- **Nombre:** Spotify Top 200 Charts  
- **Fuente:** [Kaggle - Spotify Charts Dataset](https://www.kaggle.com/datasets/dhruvildave/spotify-charts)  
- **Campos principales:** `Track Name`, `Artist`, `Streams`, `Date`, `Region`, `Position`, `URL`
- Para pruebas rápidas, se ha creado una muestra reducida: `spotify_dataset_short.csv`

---

## 🛠 Tecnologías Utilizadas

- Python
- Conda
- Pandas, NumPy  
- Streamlit  
- Plotly / Seaborn  
- Scikit-learn  
- *(Opcional)* MongoDB, Surprise, Docker

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres aportar, abre un issue o haz un pull request.

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
