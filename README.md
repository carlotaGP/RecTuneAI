# 🎧 RecTuneAI - Sistema de Recomendación Musical basado en Spotify Charts

RecTuneAI es una aplicación interactiva desarrollada con Python y Streamlit que permite analizar tendencias musicales globales y generar recomendaciones personalizadas. Utiliza datos reales del ranking Top 200 de Spotify para ofrecer insights musicales a partir de cinco enfoques distintos: tendencias por país, popularidad, similitud de usuarios, evolución temporal y búsqueda personalizada.

---

## 📑 Índice

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Demo](#demo)
3. [Instalación](#instalación)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Uso de la Aplicación](#uso-de-la-aplicación)
6. [Funcionalidades](#funcionalidades)
7. [Dataset](#dataset)
8. [Tecnologías Utilizadas](#tecnologías-utilizadas)
9. [Contribuciones](#contribuciones)
10. [Licencia](#licencia)

---

## 📌 Descripción del Proyecto

**RecTuneAI** es una aplicación interactiva desarrollada con Python y Streamlit que analiza tendencias musicales globales usando datos reales de Spotify Charts. El sistema permite explorar, visualizar y generar recomendaciones musicales personalizadas a partir de múltiples enfoques: popularidad por país, estado de ánimo, similitud entre canciones y artistas, evolución en el tiempo y más.

La app está pensada tanto para amantes de la música como para analistas de datos que quieran entender mejor el comportamiento musical global.

---

## 🎥 Demo

> Próximamente: incluye aquí un enlace a un video o captura de pantalla con tu app funcionando.

---

## ⚙️ Instalación

```bash
# Clona el repositorio
git clone https://github.com/tu_usuario/vibesage.git
cd vibesage

# Instala las dependencias
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

---

## 🛠 Tecnologías Utilizadas

- Python  
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
