# Importação das tecnologias de visualização web e de dados

import streamlit as st
import pandas as pd

#  Cabeçalho de texto do trabalho

st.title("Músicas do Spotify Brasil")

st.divider()

st.subheader("A base de dados irá mostrar os artistas e suas músicas respectivamente quando selecionados.")
st.markdown("Tem como base as músicas mais ouvidas no Brasil entre 2021 à 2023.")

# Corpo do trabalho
    
spotify_chart = pd.read_csv("archive/tracks_info-update.csv")[['artist_names', 'name']]
st.dataframe(spotify_chart)

# Corpo da barra de pesquisa

artista = st.multiselect("Escolha um artista:", spotify_chart["artist_names"].unique())

# Terceira parte quando o streamlit mostra os resultados

st.subheader("Vamos descobrir se o seu artista aparece?")

spotify_artistas = spotify_chart[spotify_chart['artist_names'].isin(artista)][['artist_names', 'name']]
st.data_editor(spotify_artistas)

st.divider()




# Anotações
# spotify:track:2MuWTIM3b0YEAskbeeFE1i
# Example: http://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6
# https://developer.spotify.com/documentation/web-api/concepts/spotify-uris-ids

# href para direcionar a track com base nos dados das músicas mais ouvidas dessa data específica