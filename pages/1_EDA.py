import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data

# ────────────────────────────────
# 🔧 Funciones auxiliares
# ────────────────────────────────

def mostrar_dataset(df):
    st.subheader("👀 Vista previa del dataset")
    st.dataframe(df.head())

def seleccionar_filtros(df):
    countries = sorted(df["region"].unique())
    countries.insert(0, "Todos") 
    country = st.selectbox("🌍 Selecciona un país:", countries)

    # Asegurar formato de fecha
    df["date"] = pd.to_datetime(df["date"]).dt.date
    min_date = df["date"].min()
    max_date = df["date"].max()

    date_input = st.date_input(
        "📅 Selecciona el rango de fechas:",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    return df, country, date_input

def filtrar_datos(df, country, date_input):
    if isinstance(date_input, tuple) and len(date_input) == 2:
        start_date, end_date = date_input
        if country == "Todos":
            filtered_df = df[
                (df["date"] >= start_date) &
                (df["date"] <= end_date)
            ]
        else:
            filtered_df = df[
                (df["region"] == country) &
                (df["date"] >= start_date) &
                (df["date"] <= end_date)
            ]
        return filtered_df, start_date, end_date, True
    else:
        st.warning("⚠️ Por favor selecciona un **rango de fechas** válido (inicio y fin). No se puede seleccionar solo un día.")
        return pd.DataFrame(), None, None, False

def mostrar_top_canciones(filtered_df):
    st.subheader("🎧 Canciones más populares")
    top_songs = (
        filtered_df.groupby("title")["streams"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        top_songs, 
        x="streams", 
        y="title", 
        orientation="h", 
        title="Top 10 canciones por streams"
    )
    st.plotly_chart(fig)

def mostrar_top_artista(filtered_df, country, start_date, end_date):
    top_artist = (
        filtered_df.groupby("artist")["streams"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )
    top_artist_name = top_artist.iloc[0]["artist"]
    top_artist_streams = top_artist.iloc[0]["streams"]

    lugar = f"en **{country}**" if country != "Todos" else "en todos los países"

    st.success(
        f"🎧 El artista más escuchado {lugar} entre "
        f"**{start_date}** y **{end_date}** fue: **{top_artist_name}** "
        f"con **{top_artist_streams:,} streams**."
    )

def mostrar_mapa_artista_mas_escuchado(df):
    st.subheader("🌍 Artista más escuchado por país (2017 - 2021)")

    top_artist_country = (
        df.groupby(["region", "artist"])["streams"]
        .sum()
        .reset_index()
    )

    top_artist_per_country = (
        top_artist_country.sort_values("streams", ascending=False)
        .drop_duplicates("region")
    )

    if top_artist_per_country.empty:
        st.warning("⚠️ No hay datos para mostrar en el mapa.")
    else:
        fig = px.choropleth(
            top_artist_per_country,
            locations="region",
            locationmode="country names",
            color="artist",
            title="Artista más escuchado por país",
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        fig.update_geos(showcoastlines=True, showcountries=True)
        st.plotly_chart(fig, use_container_width=True)

# ────────────────────────────────
# 🚀 App principal
# ────────────────────────────────

st.title("📊 Exploración de Datos - Spotify Charts")

df = load_data()

mostrar_dataset(df)

df, country, date_input = seleccionar_filtros(df)
filtered_df, start_date, end_date, filtro_valido = filtrar_datos(df, country, date_input)

if filtro_valido:
    if not filtered_df.empty:
        st.write(f"📌 Mostrando {len(filtered_df)} registros para **{country}**")
        st.dataframe(filtered_df)
        mostrar_top_canciones(filtered_df)
        mostrar_top_artista(filtered_df, country, start_date, end_date)
    else:
        st.warning("⚠️ No hay datos para mostrar la gráfica.")

mostrar_mapa_artista_mas_escuchado(df)
