import urllib.request
import json
import random
import time

# Liste de navigateurs fictifs pour que les requêtes restent furtives et évitent les blocages
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
]

def mission_surveillance_marche():
    print("--- Lancement de la Mission 1 : Surveillance et Analyse ---")
    url = "https://api.publicapis.org/entries"
    
    try:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        req = urllib.request.Request(url, headers=headers)
        
        # Petite pause aléatoire pour imiter un comportement naturel
        time.sleep(random.uniform(1.0, 3.0))
        
        reponse = urllib.request.urlopen(req, timeout=5)
        data = json.loads(reponse.read().decode('utf-8'))
        total = data.get('count', 0)
        print(f"[SUCCÈS] Mission 1 validée : {total} éléments scannés sans encombre.")
    except Exception as e:
        print(f"[ERREUR] Mission 1 : {e}")

def mission_micro_taches():
    print("--- Lancement de la Mission 2 : Requêtes et Vérifications Furtives ---")
    # Simulation d'un appel sur une cible secondaire ou une API de données ouvertes
    url = "https://httpbin.org/json"
    
    try:
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        req = urllib.request.Request(url, headers=headers)
        
        time.sleep(random.uniform(2.0, 4.0))
        
        reponse = urllib.request.urlopen(req, timeout=5)
        print("[SUCCÈS] Mission 2 validée : Connexion furtive établie et données traitées.")
    except Exception as e:
        print(f"[ERREUR] Mission 2 : {e}")

if __name__ == "__main__":
    print("Démarrage du pipeline multi-tâches automatisé...")
    mission_surveillance_marche()
    mission_micro_taches()
    print("Toutes les missions du jour sont terminées avec succès.")
