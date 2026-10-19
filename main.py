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
        print("[SUCCÈS] E-mail d'alerte de radar envoyé avec succès !")
    except Exception as e:
        print(f"[ERREUR] Échec de l'envoi de l'e-mail : {e}")

def radar_jeux_video():
    print("--- Lancement du Radar : Jeux PS5 & Switch (< 15€) ---")
    
    # Paramètres de ta recherche
    mots_cles = "jeu ps5 switch"
    budget_max = 15
    
    # Création automatique du lien direct de recherche LeBonCoin
    query_encoded = urllib.parse.quote(mots_cles)
    lien_direct = f"https://www.leboncoin.fr/recherche?text={query_encoded}&price=max-{budget_max}"
    
    # Construction du message avec le vrai lien cliquable
    message = (
        f"🎯 TON RADAR DE RECHERCHE EST PRÊT !\n\n"
        f"Voici ton lien direct personnalisé pour voir les offres en temps réel :\n"
        f"- Critères : Jeux PS5 / Switch\n"
        f"- Budget max : {budget_max} €\n\n"
        f"👉 Clique sur ce lien pour voir les annonces :\n"
        f"{lien_direct}\n\n"
        f"Il te suffit de cliquer pour consulter les nouveautés instantanément !"
    )
    
    envoyer_alerte_email("🚨 Radar Bon Plan : Voir les annonces PS5/Switch", message)

if __name__ == "__main__":
    print("Démarrage du radar de bonnes affaires...")
    radar_jeux_video()
    print("Exécution du radar terminée.")
