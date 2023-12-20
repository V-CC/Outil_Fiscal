import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from io import BytesIO

Bleu = '#0D2A59'
Rouge = '#E61434'

col1, col2, col3 = st.columns(3)
with col2 :
    st.subheader("Outil de calcul")


st.subheader("")
revenu_brut = st.number_input("Revenu annuel brut en € : ")
revenu = revenu_brut-revenu_brut*0.15

result = 0

if revenu > 177106 :
    ip = (28797-11294)*0.11 + (82341-28797)*0.3 + (177106-82341)*0.41 + (revenu-177106)*0.45

elif revenu < 177106 and revenu > 82341:
    ip = (28797-11294)*0.11 + (82341-28797)*0.3 + (revenu-82341)*0.41

elif revenu < 82341 and revenu > 28797:
    ip = (28797-11294)*0.11 + (revenu-28797)*0.3

elif revenu < 28797 and revenu > 11294:
    ip = (revenu-11294)*0.11

else:
    ip = 0

result = ip


st.subheader("")
st.subheader("")
col1, col2  = st.columns(2)
with col1:
    st.metric(label="Revenu net annuel avant IR", value=round(revenu,2), delta="en €")
with col2:
    st.metric(label="Impot sur le revenu", value=round(result,2), delta="en €")

col1, col2  = st.columns(2)
with col1:
    st.metric(label="Revenu net sur 12 mois après IR", value=round((revenu/12)-(result/12),2), delta="en €")
with col2:
    st.metric(label="Revenu net sur 13 mois après IR", value=round((revenu/13)-(result/12),2), delta="en €")


# Titre de l'application
st.title("Évolution des indices boursiers")

# Barre de menu à gauche
st.sidebar.header("Menu")
indice_selectionne = st.sidebar.selectbox("Sélectionnez l'indice :", ["S&P500", "Dow Jones", "CAC40"])

# Définition des symboles des indices
symboles_indices = {"S&P500": "^GSPC", "Dow Jones": "^DJI", "CAC40": "^FCHI"}

# Téléchargement des données depuis Yahoo Finance
indice_data = yf.download(symboles_indices[indice_selectionne], start="2022-01-01", end="2023-01-01")

# Créer le graphique avec Matplotlib
fig, ax = plt.subplots()
ax.plot(indice_data.index, indice_data["Close"])
ax.set_title(f"{indice_selectionne} - Évolution du cours")
ax.set_xlabel("Date")
ax.set_ylabel("Close")

# Afficher le graphique dans Streamlit
st.pyplot(fig)