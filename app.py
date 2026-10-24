import os
from transformers import pipeline

print("Connexion au cerveau de l'IA en cours...")
generateur = pipeline("text-generation", model="facebook/opt-1.3b")

def poser_une_question(question):
    print(f"\nQuestion : {question}")
    reponse = generateur(question, max_length=150, num_return_sequences=1)
    print("\n--- Réponse de ton IA ---")
    print(reponse[0]['generated_text'])

ma_question = "Explique-moi comment fonctionne le système solaire."
poser_une_question(ma_question)
