import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
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
        print("[SUCCÈS] E-mail d'alerte envoyé avec succès !")
    except Exception as e:
        print(f"[ERREUR] Échec de l'envoi de l'e-mail : {e}")

def mission_surveillance_marche():
    print("--- Lancement de la Mission 1 : Surveillance ---")
    url = "https://api.publicapis.org/entries"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        req = urllib.request.Request(url, headers=headers)
        time.sleep(1)
        reponse = urllib.request.urlopen(req, timeout=5)
        data = json.loads(reponse.read().decode('utf-8'))
        total = data.get('count', 0)
        
        # Si tout va bien, on prépare un petit message
        message = f"Bonjour,\n\nLa mission de surveillance s'est déroulée avec succès.\nTotal des éléments scannés : {total}."
        envoyer_alerte_email("Rapport Automate : Mission Réussie 🚀", message)
        
    except Exception as e:
        print(f"[ERREUR] Mission 1 : {e}")
        envoyer_alerte_email("Alerte Automate : Erreur détectée ⚠️", str(e))

if __name__ == "__main__":
    print("Démarrage du pipeline avec alertes e-mail...")
    mission_surveillance_marche()
    print("Exécution terminée.")
