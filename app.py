from fastapi import FastAPI, HTTPException
import requests
import os
from dotenv import load_dotenv

# 1. Carregar les credencials segures del fitxer .env
load_dotenv()

# 2. Inicialitzar l'aplicació FastAPI
app = FastAPI(title="Amadeus Flight Search API", description="API pont cap a Amadeus")

# Variables globals llegides de l'entorn
API_KEY = os.getenv("AMADEUS_CLIENT_ID")
API_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")
AMADEUS_TEST_URL = "https://test.api.amadeus.com"

def get_amadeus_token():
    """Funció per obtenir el Token d'accés d'Amadeus """
    url = f"{AMADEUS_TEST_URL}/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
    
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise HTTPException(status_code=500, detail="Error d'autenticació amb Amadeus")

@app.get("/")
def home():
    """Endpoint arrel de comprovació"""
    return {"status": "Actiu", "missatge": "El motor de cerca de vols està funcionant!"}

@app.get("/api/flights")
def search_flights(origin: str = "BCN", destination: str = "JFK", date: str = "2026-06-01"):
    """Endpoint per buscar vols """
    token = get_amadeus_token() # Obtenim el token abans de fer la crida
    url = f"{AMADEUS_TEST_URL}/v2/shopping/flight-offers"
    
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "originLocationCode": origin,
        "destinationLocationCode": destination,
        "departureDate": date,
        "adults": 1,
        "max": 3 # Limitem a 3 resultats per fer-ho més llegible
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json() # Retorna les dades formatades en JSON 
    else:
        raise HTTPException(status_code=response.status_code, detail="Error buscant vols")