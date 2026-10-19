import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.parse

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
        print("[SUCCÈS] E-mail d'alerte de radar optimisé envoyé avec succès !")
    except Exception as e:
        print(f"[ERREUR] Échec de l'envoi de l'e-mail : {e}")

def radar_jeux_video_opti():
    print("--- Lancement du Radar Optimisé : Jeux PS5 & Switch ---")
    
    # Paramètres de recherche ultra-ciblés
    mots_cles = "jeu ps5 switch"
    budget_max = 15
    
    # URL optimisée avec catégorie jeux vidéo (c=27) et tri par date (sort=time)
    query_encoded = urllib.parse.quote(mots_cles)
    lien_direct = f"https://www.leboncoin.fr/recherche?category=27&text={query_encoded}&price=max-{budget_max}&sort=time"
    
    message = (
        f"🎯 TON RADAR OPTIMISÉ EST PRÊT !\n\n"
        f"Ce lien filtre directement par catégorie 'Jeux vidéo' et trie par nouveauté :\n"
        f"- Critères : PS5 / Switch\n"
        f"- Budget max : {budget_max} €\n\n"
        f"👉 Clique ici pour voir les vraies nouveautés :\n"
        f"{lien_direct}\n\n"
        f"Teste ce lien depuis ton e-mail pour voir la différence !"
    )
    
    envoyer_alerte_email("🚨 Radar Opti : Jeux PS5/Switch à -15€", message)

if __name__ == "__main__":
    print("Démarrage du radar optimisé...")
    radar_jeux_video_opti()
    print("Exécution terminée.")
