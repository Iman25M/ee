import osmnx as ox
import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Définir la zone
place = "Paris, France"

# 2️⃣ Récupérer les entités 'waterway' (cours d’eau)
waterways = ox.features_from_place(place, tags={"waterway": "river"})

# 3️⃣ Filtrer uniquement la Seine
seine = waterways[waterways["name"].str.contains("Seine", case=False, na=False)]

if seine.empty:
    print("Aucune donnée trouvée pour la Seine.")
else:
    # 4️⃣ Extraire toutes les coordonnées GPS de tous les segments
    coords = []
    for geom in seine.geometry:
        coords.extend(list(geom.coords))

    # 5️⃣ Créer un DataFrame
    df = pd.DataFrame(coords, columns=["Longitude", "Latitude"])

    # 6️⃣ Afficher le tableau
    print(df)

    # 7️⃣ Sauvegarder en format Excel
    df.to_excel("seine_complete_coordinates.xlsx", index=False)
    print("✅ Toutes les coordonnées de la Seine ont été sauvegardées dans 'seine_complete_coordinates.xlsx'")

    # 8️⃣ Tracer la carte de Paris avec la Seine
    fig, ax = plt.subplots(figsize=(8, 8))

    # Afficher le fond de carte (réseau routier)
    graph = ox.graph_from_place(place, network_type="drive")
    ox.plot_graph(graph, ax=ax, show=False, close=False, node_size=0, edge_color="lightgray")

    # Tracer la Seine en bleu
    seine.plot(ax=ax, color="blue", linewidth=2)

    # Titre
    plt.title("La Seine à Paris (coordonnées GPS issues d'OpenStreetMap)")

    # Sauvegarder la figure en image
    plt.savefig("seine_map.png", dpi=300)
    print("✅ Carte sauvegardée dans 'seine_map.png'")

    # Afficher la carte
    plt.show()
