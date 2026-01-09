import streamlit as st
import requests
import os

# On récupère l'URL depuis le .env (injecté par Docker)
API_URL = os.getenv("API_URL")

st.title("🚀 YouExpress V2 - Test Docker")

st.write("Si vous voyez ceci, le conteneur Frontend fonctionne.")
st.info(f"Le Frontend va essayer de contacter le Backend sur : {API_URL}")

if st.button("Tester la connexion Backend"):
    try:
        # Le frontend (dans Docker) appelle le backend (dans Docker)
        response = requests.get(f"{API_URL}/")
        if response.status_code == 200:
            st.success(f"Réponse du Backend : {response.json()}")
        else:
            st.error(f"Erreur : {response.status_code}")
    except Exception as e:
        st.error(f"Échec de connexion : {e}")