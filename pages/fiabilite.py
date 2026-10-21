import streamlit as st

st.title("Fiabilité")
st.write("Voilà la section fiabilité.")

# Création du bouton de navigation
if st.button("Voir l'inventaire des stocks"):
    # Indique le chemin exact du fichier cible
    st.switch_page("pages/fiabilite/fiabilite_stock.py")
