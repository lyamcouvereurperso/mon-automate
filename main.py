import urllib.request
import json

def executer_tache_automatisee():
    url = "https://api.publicapis.org/entries"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        reponse = urllib.request.urlopen(req, timeout=5)
        data = json.loads(reponse.read().decode('utf-8'))
        total_entrees = data.get('count', 0)
        print(f"[SUCCÈS] Connexion établie. {total_entrees} éléments analysés.")
    except Exception as e:
        print(f"[ERREUR] : {e}")

if __name__ == "__main__":
    executer_tache_automatisee()
