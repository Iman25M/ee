# Requirements: pip install folium geopy
import folium
from geopy.geocoders import Nominatim

# 1) obtenir coordonnées (ex : localisation "Seine, Paris" via Nominatim)
geolocator = Nominatim(user_agent="mon_app")
location = geolocator.geocode("Seine, Paris, France")  # parfois retourne un point représentatif

print("Coordonnées trouvées:", location.latitude, location.longitude)

# 2) créer carte centrée et ajouter un marqueur
m = folium.Map(location=[location.latitude, location.longitude], zoom_start=13)
folium.Marker([location.latitude, location.longitude], popup="Seine (approx.)").add_to(m)

# 3) sauvegarder en HTML
m.save("paris_seine_simple.html")
print("Carte sauvegardée dans paris_seine_simple.html — ouvre dans ton navigateur.")
