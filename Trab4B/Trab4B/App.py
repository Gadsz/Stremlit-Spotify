import streamlit as st
import pandas as pd
import numpy as np

# Cabeçalho de texto do trabalho
st.title("Músicas do Spotify Brasil")

st.divider()

st.subheader("A base de dados irá mostrar os artistas e suas músicas respectivamente quando selecionados.")
st.markdown("Tem como base as músicas mais ouvidas no Brasil entre 2021 à 2023.")

# Carregar os dados
spotify_chart = pd.read_csv("archive/tracks_info-update.csv")[['artist_names', 'name', 'energy', 'tempo', 'danceability']]
st.dataframe(spotify_chart)

# Corpo da barra de pesquisa
artista = st.multiselect("Escolha um artista:", spotify_chart["artist_names"].unique())

# Filtrar os resultados dos artistas escolhidos
st.subheader("Vamos descobrir se o seu artista aparece?")
spotify_artistas = spotify_chart[spotify_chart['artist_names'].isin(artista)][['artist_names', 'name']]
st.data_editor(spotify_artistas)

# Dados novos

# Inserir aqui os dados da energia e tempo da música selecionada (consultar tabela CSV a cima)
st.divider()
st.subheader("Inserir aqui os dados da energia e tempo da música selecionada (consultar tabela CSV a cima)")

# Inserir aqui os dados da energia e tempo da música selecionada (consultar tabela CSV a cima)
energy = st.slider('Energy (0 a 1)', 0.0, 1.0, 0.5) # Os números depois é só o minimo, maximo e meio do slider
tempo = st.slider('Tempo (BPM)', 50.0, 200.0, 120.0) # Os números depois é só o minimo, maximo e meio do slider

# O BPM pode variar de 150 a 200, foi escolhido esse valor para fazer uma média dividindo ele
# A energia na tabela vai de 0 a 1, por isso foi escolhido uma média de 0.6 
dançavel = (energy * 0.6 + tempo / 200)

# Exibir a previsão com 4 caracteres (.4f)
st.subheader("Previsão do quanto a música é dançável") # Texto do cabeçalho
st.write(f"**A dançabilidade prevista é:** {dançavel:.4f}")
# Ele puxa a string por f dentro das chaves, no caso a variável dançavel com 4 caracteres depois
# python -m streamlit run App.py