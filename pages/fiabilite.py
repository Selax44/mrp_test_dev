import streamlit as st

st.title("Fiabilité")
st.write("Voilà la section fiabilité.")

if st.button("Voir l'inventaire des stocks"):
    st.switch_page("pages/fiabilite/fiabilite_stock.py")
