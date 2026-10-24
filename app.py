import streamlit as st
from transformers import pipeline

# 1. On crée le titre de ton application web
st.title("Mon IA Universelle 🚀")
st.write("Pose-moi n'importe quelle question, dans n'importe quelle langue !")

# 2. On charge le modèle d'IA gratuit en mémoire
@st.cache_resource # Cette ligne évite de recharger l'IA à chaque fois
def charger_ia():
    return pipeline("text-generation", model="facebook/opt-1.3b")

generateur = charger_ia()

# 3. On crée la zone de texte pour l'utilisateur
question = st.text_input("Écris ta question ici :", "")

# 4. Quand l'utilisateur valide, l'IA lui répond
if question:
    with st.spinner("L'IA réfléchit..."):
        reponse = generateur(question, max_length=100)
        st.subheader("Réponse :")
        st.write(reponse[0]['generated_text'])
