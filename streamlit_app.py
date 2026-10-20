import streamlit as st

# Configuration globale de l'application (doit être la première ligne)
st.set_page_config(page_title="Portail Test", page_icon="🔬", layout="wide")

# 1. Déclaration des pages pointant vers tes fichiers
page_accueil = st.Page("pages/accueil.py", title="Accueil", icon="🏠", default=True)
page_prod = st.Page("pages/production.py", title="Production", icon="⚙️")
page_eng = st.Page("pages/engineering.py", title="Engineering", icon="📐")
#page_infos = st.Page("pages/fiabilite_infos.py", title="Infos", icon="📄")
#page_stock = st.Page("pages/fiabilite_stock.py", title="Stock (A & B)", icon="📦")

# 2. Création du menu latéral avec tes sections personnalisées
navigation = st.navigation(
    {
        "Général": [page_accueil],
        "Départements": [page_prod, page_eng],
        #"Fiabilité - Projet": [page_infos, page_stock]
    }
)

# 3. Lancement de l'affichage
navigation.run()
