import requests
from config import GOOGLE_API_KEY

def find_doctors_nearby(city, specialization="Hematology"):
    """Mencari dokter terbaik di kota berdasarkan spesialisasi"""
    url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={specialization}+doctor+in+{city}&key={GOOGLE_API_KEY}"
    response = requests.get(url).json()
    
    doctors = []
    for place in response.get("results", [])[:5]:  # Ambil 5 hasil terbaik
        doctors.append(f"**{place['name']}** - {place['formatted_address']}")
    
    return "\n".join(doctors)
