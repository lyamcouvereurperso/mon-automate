import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import urllib.request
import json

# Récupération des secrets configurés dans GitHub
MAIL_USER = os.getenv("MAIL_USER")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

def envoyer_alerte_email(sujet, message):
    if not MAIL_USER or not MAIL_PASSWORD:
        print("[AVERTISSEMENT] Identifiants e-mail non trouvés, impossible d'envoyer l'alerte.")
        return

    try:
        msg = MIMEMultipart()
        msg['From'] = MAIL_USER
        msg['To'] = MAIL_USER
        msg['Subject'] = sujet
        msg.attach(MIMEText(message, 'plain'))

        # Connexion au serveur sécurisé de Gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MAIL_USER, MAIL_PASSWORD)
        server.sendmail(MAIL_USER, MAIL_USER, msg.as_string())
        server.quit()
        print("[SUCCÈS] E-mail d'alerte de radar envoyé avec succès !")
    except Exception as e:
        print(f"[ERREUR] Échec de l'envoi de l'e-mail : {e}")

def radar_jeux_video():
    print("--- Lancement du Radar : Jeux PS5 & Switch (< 15€) ---")
    
    # Ici, on configure la recherche pour cibler nos critères
    plateformes = ["PS5", "Nintendo Switch"]
    budget_max = 15
    
    # Simulation de la veille du marché (le script analyse les critères)
    # Dans les prochaines étapes, on branchera des sources d'annonces en direct.
    trouvaille_exemple = {
        "titre": "Jeu Nintendo Switch - Bon plan détecté",
        "prix": 12,
        "plateforme": "Nintendo Switch",
        "lien": "https://www.leboncoin.fr (Exemple de lien à surveiller)"
    }
    
    if trouvaille_exemple["prix"] <= budget_max:
        message = (
            f"🎯 ALERTE BON PLAN JEU VIDÉO !\n\n"
            f"Un article correspondant à tes critères a été repéré :\n"
            f"- Article : {trouvaille_exemple['titre']}\n"
            f"- Plateforme : {trouvaille_exemple['plateforme']}\n"
            f"- Prix : {trouvaille_exemple['prix']} € (Inférieur à ton max de {budget_max} €)\n"
            f"- Lien : {trouvaille_exemple['lien']}\n\n"
            f"Fonce vérifier l'annonce pour faire une revente !"
        )
        envoyer_alerte_email("🚨 Radar Bon Plan : Jeu PS5/Switch à -15€ !", message)
    else:
        print("Aucune offre sous les 15€ pour le moment.")

if __name__ == "__main__":
    print("Démarrage du radar de bonnes affaires...")
    radar_jeux_video()
    print("Exécution du radar terminée.")
