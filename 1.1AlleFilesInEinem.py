"""
Dieses Skript enthält mehrere Programme zur Erstellung von Bildern und Visualisierungen der ISS-Trajektorie.
Jedes Programm hat eine eigene Funktion und wird nacheinander ausgeführt.

Programm 1:
Dieses Programm liest CSV-Dateien mit ISS-Bewegungsdaten ein und erstellt eine Karte der ISS-Trajektorien auf der Erde.
Die Daten sind schon in Polar-Koordinaten und werden auf der Karte gezeigt. Hier wird auch ersichtlich, wo wieviele Fotos gemacht wurden.

Programm 2:
Dieses Programm liest XML-Daten �ber die ISS-Spacestation ein und konvertiert die kartesischen Koordinaten in longitudinale und laterale Koordinaten.
Es werden die L�ngen- und Breitengrade der ISS-Trajektorie auf einer 2D-Karte der Welt dargestellt.

Programm 3:
Dieses Programm visualisiert die 3D-Trajektorie der ISS basierend auf XML-Daten.
Dies wird hier auf einer durchsichtigen Kugel gemacht, um die Umlaufbahn besser zu zeigen

Programm 4:
Dieses Programm visualisiert die Trajektorie der ISS auf einem rotierenden 3D-Globus in 2D.
Es wird ein GIF erstellt, welches die rotierende Erdkugel mit den ISS-Laufbahn dar�ber zeigt

Programm 5:
Dieses Programm visualisiert die Trajektorie der ISS auf einem 3D-Globus.
Die Daten k�nnen in der Grafik rotiert und somit von allen Seiten gesehen werden. 
Die ISS wird in der richtigen h�he �ber der Erde geplottet und es wird auch Ihre umlaufbahn sichtbar.

Programm 6:
Dieses Programm visualisiert die aktuelle Position der ISS auf einer Karte.
Es verwendet ein API um die Position der ISS zum Zeitpunkt des laufens des Programmes zu erhalten.
Diese Ortschaft wird dann f�r einen Zeitraum oder unendlich lange auf der Karte erneuert.

Programm 7:
Dieses Skript ruft den vorhergesagten Standort der Internationalen Raumstation (ISS) mithilfe der N2YO-API ab.
Es berechnet die Startzeit des nächsten ISS-Überflugs f�r den automatisch erhaltenen Aufenthaltsorts des Nutzer zur�ck.
Es holt auch die h�he des Ortes, des Nutzers und gibt die �berflugszeit in der Zeitzone des Beobachters zur�ck.
Ausserdem werden auch noch die Wettervorhersagen in das Programm mit einbezogen, um ein genaueres Ergebniss zu erhalten.
Hier wird besonders auf die Wolken acht gegeben, wobei auch die Sicherheit f�r diese Aussage gegeben wird.
All dies wird in einem Plot als Text ausgegeben, wobei auf den Karten noch die Wetterdaten gezeigt werden.


Hinweis:    Die XML-Daten werden von der offiziellen NASA-Website heruntergeladen: https://data.nasa.gov/browse?q=ISS+COORDS
            Die CSV-Daten werden von einem Github-Projekt heruntergeladen: https://github.com/natronics/ISS-photo-locations/tree/master
            Es werden folgende API-Keys verwendet:
                Open Notify: http://open-notify.org
                N2YO-API: https://www.n2yo.com/api/
                GeoNames-API: http://api.geonames.org/
                IPInfo-API: https://ipinfo.io
                Open-Elevevation-API: https://api.open-elevation.com/api/v1/
                OpenWeatherAPI: https://api.openweathermap.org/data/2.5
                
            Es werden folgende Librarys/Module verwendet (m�ssen installiert werden):
                import pandas as pd
                import matplotlib.pyplot as plt
                import cartopy.crs as ccrs
                import glob
                import xml.etree.ElementTree as ET
                import math
                import os
                from mpl_toolkits.mplot3d import Axes3D
                import numpy as np
                from mpl_toolkits.basemap import Basemap
                import imageio
                from matplotlib.animation import FuncAnimation
                import PIL
                import requests 
                import time
                import datetime
                from pytz import timezone 
                import matplotlib.image as mpimg
                
            Um diese zu installieren sollte dieser Befehl gelaufen lassen werden:
                pip install -r requirements.txt

"""

"""
Die sind alle Programme, die ich für die Erstellung der Bilder verwendet habe.
Sie werden hier mit einführenden Kommentaren voneinander getrennt, jedoch werden die Module immer von neuem geladen.
Dies wird gemacht, um die einzelnen Programme einfacher zu verstehen und zu bearbeiten.

Die Programme sind in der Reihenfolge, wie ich sie verwendet habe, um die Bilder oder GIFS zu erstellen.
"""


"""
Erstellt am Mi Jan  3 19:26:06 2024

Dieses Skript liest CSV-Dateien mit ISS-Bewegungsdaten ein und erstellt eine Karte der ISS-Trajektorien auf der Erde.
Es verwendet die Module pandas, matplotlib und cartopy.

Das Skript durchläuft alle CSV-Dateien im angegebenen Verzeichnis und zeichnet die ISS-Trajektorien auf einer Karte der Erde.
Die Trajektorien werden als rote gestrichelte Linien dargestellt, wobei jeder Punkt durch einen roten Punkt markiert ist.

Die Karte wird mit der PlateCarree-Projektion erstellt und zeigt die Küstenlinien der Erde an.
Die Achsenbeschriftungen und der Titel werden festgelegt, und eine Legende wird für alle Dokumente erstellt.

Das Skript zeigt das fertige Plot an, bei dem alle Trajektorien übereinander gelegt werden.

Die Daten und die Idee wurde von https://github.com/natronics/ISS-photo-locations/tree/master bezogen

Hinweis: Das Skript erfordert, dass die Module pandas, matplotlib und cartopy installiert sind.
"""
print("----------------")
print("----------------")
print("Programm 1 Start")
print("----------------")
print("----------------")

# importieren der Module
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import glob
import os

# einen anderen Weg die verschiedenen Dokumente einzulesen
# der Weg zu den Daten
directory_path = 'Daten/PictureData/data/*.csv'

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

# eine Liste aller Dokumente erhalten
file_paths = glob.glob(directory_path)

# eine 2d Karte der Erde projezieren
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()

# durch jedes Dokument durch itterieren
for file_path in file_paths:
    # die CSV-Datei lesen
    df = pd.read_csv(file_path, names=['ID', 'Latitude', 'Longitude'])
    # die Bewegung der ISS ploten
    ax.plot(df['Longitude'], df['Latitude'], marker='o', markersize=0.01, linewidth=0.005, color='red', linestyle='dashed')

# die Labels und den Titel setzen
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('ISS Trajectories on Earth Map')
# optional: die ganze Weltkarte anzeigen
ax.set_global()

# eine einzige Legende für alle Dokumente haben
ax.legend(['ISS Trajectories'], loc='upper left')

# das Plot zeigen (alle Dokumente werden übereinander gelegt)
# plt.show()

output_path_final_picture = '1_Programm_ISS_CSV_Data.png'
output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)

# das Plot speichern
plt.savefig(output_path_final_picture)

print("----------------")
print("----------------")
print("Programm 1 Ende")
print("----------------")
print("----------------")

"""
Erstellt am Mi Jan  3 15:22:02 2024

Dieses Skript liest XML-Daten über die ISS-Spacestation ein und konvertiert die kartesischen Koordinaten in longitudinale und laterale Koordinaten.
Es werden die Längen- und Breitengrade der ISS-Trajektorie auf einer 2D-Karte der Welt dargestellt.

Die XML-Daten werden von der offiziellen NASA-Website heruntergeladen: https://data.nasa.gov/browse?q=ISS+COORDS

Das Skript verwendet die Bibliotheken xml.etree.ElementTree, matplotlib.pyplot, cartopy.crs und math.

Die Hauptfunktion des Skripts ist die Funktion plot_iss_trajectory, die die ISS-Trajektorie auf einer Karte plottet.

"""
print("----------------")
print("----------------")
print("Programm 2 Start")
print("----------------")
print("----------------")

import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import math
import os

# die Daten sind von der Offiziellen Nasa-Seite: https://data.nasa.gov/browse?q=ISS+COORDS
# der Datenweg für die XML Daten
xml_path = "Daten/XmlData"

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

# leere Listen für die Daten
lons = []
lats = []

# itterier durch alle Dokumente in dem Ordner
for file in os.listdir(xml_path):
    # gibt den vollständigen Datenweg an
    file_path = os.path.join(xml_path, file)
    # die Daten werden geöffnet
    root = ET.parse(file_path)

    # itteriert durch die Baumstrucktur der XML Daten
    for state_vector in root.findall(".//stateVector"):
        # sucht nach einem bestimmten Zeichen, um dieses als x,y,z Koordinate wiederzugeben
        x = float(state_vector.find("X").text)
        y = float(state_vector.find("Y").text)
        z = float(state_vector.find("Z").text)
    
        # konvertiert die cartesischen Koordinaten zu longitudinal und lateral Koordinaten
        # formel von https://studyflix.de/mathematik/kugelkoordinaten-1519
        r = math.sqrt(x * x + y * y + z * z)
        if x > 0 and y>=0:
            lon = math.atan(y/x)
        elif x > 0 and y < 0:
            lon = math.atan(y/x) + 2 * math.pi
        elif x < 0:
            lon = math.atan(y/x) + math.pi
        lat = math.acos(z / r)

        # von Radiant zu Gard umwandeln
        lon = math.degrees(lon)
        lat = math.degrees(lat)
        
        # die Daten waren nicht zentriert und mussten in die Mitte des Bildes gerückt werden
        lat -= 90
        lon -= 180
        
        # die Daten der Liste hinzufügen
        lons.append(lon)
        lats.append(lat)

# eine 2d Karte der Welt plotten
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
ax.coastlines()

# die Laufbahn der ISS plotten
ax.plot(lons, lats, label='ISS Trajectory', marker='o', markersize=0.01, linewidth=0.015, color='red', linestyle='dashed')

# Labels und Titel setzen
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('ISS Trajectory on Earth Map')

#optional: ganze Welkarte anzeigen
ax.set_global()

# Die Grafik anzeigen
plt.legend()
#plt.show()

output_path_final_picture = '2_Programm_ISS_XML_Data.png'
output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)

plt.savefig(output_path_final_picture)

print("----------------")
print("----------------")
print("Programm 2 Ende")
print("----------------")
print("----------------")

"""
Erstellt am Fri Jan 5 17:30:35 2024

Dieses Skript visualisiert die 3D-Trajektorie der ISS (International Space Station) basierend auf XML-Daten.
Es verwendet die ElementTree-Bibliothek, um XML-Daten zu analysieren, und die Matplotlib-Bibliothek, um die Trajektorie zu plotten.
"""
print("----------------")
print("----------------")
print("Programm 3 Start")
print("----------------")
print("----------------")

import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import imageio

# Pfad zum XML-Datenordner
xml_path = "Daten/XmlData"

output_path = 'ZwischenAblage'
os.makedirs(output_path, exist_ok=True)

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

images = []

# Listen zur Speicherung der Trajektoriedaten
x_values = []
y_values = []
z_values = []

i = 0
picture_i = 30
# Konstanten
earth_radius = 6371  # Erdradius in km

# Funktion zum Plotten der Erde als Kugel
def plot_earth(ax):
    phi = np.linspace(0, np.pi, 100)
    theta = np.linspace(0, 2 * np.pi, 100)
    phi, theta = np.meshgrid(phi, theta)

    x = earth_radius * np.sin(phi) * np.cos(theta)
    y = earth_radius * np.sin(phi) * np.sin(theta)
    z = earth_radius * np.cos(phi)
    
    ax.set_aspect('equal')
    ax.plot_surface(x, y, z, color='b', alpha=0.3)

# Funktion zum Plotten der 3D-Trajektorie
def plot_3d_trajectory(ax, x_values, y_values, z_values):
    ax.plot(x_values, y_values, z_values, markersize=0, linewidth=0.01, color='red', label='ISS Trajektorie')
    ax.set_aspect('equal')

# Funktion zum Plotten der 3D-Trajektorie
def plot_3d_trajectory_start(ax, x_values, y_values, z_values):
    ax.plot(x_values, y_values, z_values, markersize=0, linewidth=1, color='red', label='ISS Trajektorie')
    ax.set_aspect('equal')

# Iteriere durch alle XML-Dateien im Ordner
for file in os.listdir(xml_path):
    # Vollständiger Pfad zur Datei
    file_path = os.path.join(xml_path, file)

    # Analysiere die XML-Datei
    root = ET.parse(file_path)

    # Iteriere durch stateVector-Elemente in der XML-Datei
    for state_vector in root.findall(".//stateVector"):
        i += 1
        x = float(state_vector.find("X").text)
        y = float(state_vector.find("Y").text)
        z = float(state_vector.find("Z").text)

        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
        
        if i < 30:
            # Erstelle einen 3D-Plot
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
            # Plotte die Erde
            plot_earth(ax)
            
            # Plotte die Trajektorie
            plot_3d_trajectory_start(ax, x_values, y_values, z_values)
            
            # Setze Beschriftungen und Titel
            ax.set_xlabel('X (km)')
            ax.set_ylabel('Y (km)')
            ax.set_zlabel('Z (km)')
            ax.set_title('ISS Trajektorie')
            
            # Speichere die Abbildung
            image_path = os.path.join(output_path, f'{i}.png')
            plt.savefig(image_path)
            images.append(imageio.imread(image_path))

            plt.clf()
            plt.cla()
            plt.close()
            print(i)

        elif i-1300 == 0:
            i -= 1000
            picture_i += 1
            # Erstelle einen 3D-Plot
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            
            # Plotte die Erde
            # plot_earth(ax)
            
            # Plotte die Trajektorie
            plot_3d_trajectory(ax, x_values, y_values, z_values)
            
            # Setze Beschriftungen und Titel
            ax.set_xlabel('X (km)')
            ax.set_ylabel('Y (km)')
            ax.set_zlabel('Z (km)')
            ax.set_title('ISS Trajektorie')
            
            # Speichere die Abbildung
            image_path = os.path.join(output_path, f'{picture_i}.png')
            plt.savefig(image_path)
            images.append(imageio.imread(image_path))

            plt.clf()
            plt.cla()
            plt.close()
            print(picture_i)

        else:
            x += 1

output_path_final_picture = '3_Programm_ISS_Blue_Globe.gif'
output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)

# Erstelle ein GIF
imageio.mimsave(output_path_final_picture, images, duration=0.5)

print("----------------")
print("----------------")
print("Programm 3 Ende")
print("----------------")
print("----------------")
"""
Erstellt am Fri Jan 5 18:44:36 2024

Dieses Skript visualisiert die Trajektorie der Internationalen Raumstation (ISS) auf einem 3D-Globus.
Es verwendet XML-Daten, die die ISS-Koordinaten enthalten, und erstellt eine Animation der ISS-Trajektorie auf einem rotierenden Globus.

Das Skript verwendet die Basemap-Bibliothek, um den Globus zu erstellen, und die ElementTree-Bibliothek, um die XML-Daten zu analysieren.
Es erstellt eine Reihe von Bildern, die die ISS-Trajektorie auf dem Globus darstellen, und erstellt schließlich eine GIF-Animation.

Die XML-Daten werden von der offiziellen NASA-Website heruntergeladen: https://data.nasa.gov/browse?q=ISS+COORDS

Die erstellten Bilder und das GIF werden im angegebenen Ausgabeverzeichnis gespeichert.

Hinweis: Dieses Skript hatte einige abgeänderte Formeln von schon vorhandenem Code, der auf Stack Overflow verfügbar ist: https://stackoverflow.com/questions/30269099/how-to-plot-a-rotating-3d-earth
"""
print("----------------")
print("----------------")
print("Programm 4 Start")
print("----------------")
print("----------------")

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import os
import imageio
import xml.etree.ElementTree as ET
import cartopy.crs as ccrs
import math


def plot_iss_trajectory(ax, x, y, markersize, linewidth, color='red', label='ISS Trajectory'):
    """
    Plottet die ISS-Trajektorie auf den angegebenen Achsen.

    Parameter:
        ax (matplotlib.axes.Axes): Die Achsen, auf denen geplottet werden soll.
        x (list): Die x-Koordinaten der Trajektorie.
        y (list): Die y-Koordinaten der Trajektorie.
        markersize (float): Die Größe der Marker, die die Trajektoriepunkte darstellen.
        linewidth (float): Die Breite der Linie, die die Trajektorie darstellt.
        color (str, optional): Die Farbe der Trajektorie. Standardmäßig 'red'.
        label (str, optional): Das Label für die Trajektorie. Standardmäßig 'ISS Trajectory'.
    """
    ax.plot(x, y, markersize=markersize, linewidth=linewidth, color=color, label=label)

    
def plot_globe(turning, markersize, linewidth):
    """
    Plottet den Globus mit der ISS-Trajektorie bei dem angegebenen Drehwinkel.

    Parameter:
        turning (int): Der Drehwinkel des Globus.
        markersize (float): Die Größe der Marker, die die Trajektoriepunkte darstellen.
        linewidth (float): Die Breite der Linie, die die Trajektorie darstellt.
    """
    my_map = Basemap(projection='ortho', lat_0=0, lon_0=turning*20, resolution='l', area_thresh=1000.0)
    my_map.bluemarble()
    my_map.etopo()

    # Plotte die ISS-Trajektorie auf dem aktuellen Frame
    lon_values = lons
    lat_values = lats
    x, y = my_map(lon_values, lat_values)

    # Plotte die ISS-Trajektorie auf der Karte
    plot_iss_trajectory(plt.gca(), x, y, markersize, linewidth)

    # Speichere die Abbildung
    image_path = os.path.join(output_path, f'{turning}.png')
    plt.savefig(image_path)
    images.append(imageio.imread(image_path))

    plt.clf()
    plt.cla()
    plt.close()
        

# Der Datenpfad für die XML-Daten
xml_path = "Daten/XmlData"

output_path = 'ZwischenAblage'
os.makedirs(output_path, exist_ok=True)  # Erstelle das Ausgabeverzeichnis, falls es nicht existiert

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

# Leere Listen für die Daten
lons = []
lats = []

# Erstelle ein GIF mit ISS-Trajektorien
images = []

turning = 0
slow_turning = 0
picture = 0

globe_turning = 361/24/60  # Drehwinkel in Grad pro Minute
itterative_turning = 0

# Iteriere durch alle Dokumente in dem Ordner
for file in os.listdir(xml_path):
    # Gib den vollständigen Dateipfad an
    file_path = os.path.join(xml_path, file)
    # Öffne die Daten
    root = ET.parse(file_path)

    # Iteriere durch die Baumstruktur der XML-Daten
    for state_vector in root.findall(".//stateVector"):
        turning += 1
        picture += 1
        itterative_turning += 1

        # Suche nach bestimmten Zeichen, um diese als x-, y- und z-Koordinaten darzustellen
        x = float(state_vector.find("X").text)
        y = float(state_vector.find("Y").text)
        z = float(state_vector.find("Z").text)
    
        # Konvertiere die kartesischen Koordinaten in longitudinale und laterale Koordinaten
        # Formel von https://studyflix.de/mathematik/kugelkoordinaten-1519
        r = math.sqrt(x * x + y * y + z * z)
        if x > 0 and y>=0:
            lon = math.atan(y/x)
        elif x > 0 and y < 0:
            lon = math.atan(y/x) + 2 * math.pi
        elif x < 0:
            lon = math.atan(y/x) + math.pi
        lat = math.acos(z / r)

        # Von Radiant zu Grad umwandeln
        lon = math.degrees(lon)
        lat = math.degrees(lat)
        
        # Die Daten waren nicht zentriert und mussten in die Mitte des Bildes gerückt werden
        lat -= 90
        lon -= 180
        
        globe_itterative_turning = globe_turning*itterative_turning
        
        if globe_itterative_turning >= 360:
            itterative_turning = 0
        
        lon -= globe_itterative_turning
        
        # Füge die Daten der Liste hinzu
        lons.append(lon)
        lats.append(lat)

        if turning > 17:
            turning = 0
        
        if picture < 24:
            plot_globe(turning, markersize=2, linewidth=2)
            
        elif picture-1300 == 0:
            picture -= 1000
            slow_turning += 1
            if slow_turning > 17:
                slow_turning = 0
            plot_globe(turning = slow_turning, markersize=0.1, linewidth=0.1)

    # Erstelle ein zwischen GIF
    # imageio.mimsave(f'{turning}movie_with_trajectory.gif', images, duration=0.5)

    print("done")
    
output_path_final_picture = '4_Programm_ISS_GlobeTurning_2d.gif'
output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)

    
# Erstelle ein GIF
imageio.mimsave(output_path_final_picture, images, duration=0.5)

print("done")

print("----------------")
print("----------------")
print("Programm 4 Ende")
print("----------------")
print("----------------")
"""
Dieses Skript visualisiert die Trajektorie der Internationalen Raumstation (ISS) in 3D.
Es verwendet XML-Daten, um die Position der ISS zu jedem Zeitpunkt zu erhalten und zeichnet die Trajektorie auf einem Globus.
Das Skript erstellt auch eine Animation der Trajektorie als GIF-Datei.

Das Skript verwendet die folgenden Module:
- xml.etree.ElementTree: Zum Parsen der XML-Daten
- matplotlib.pyplot: Zum Erstellen von 3D-Plots
- numpy: Zum Erstellen von Arrays und Berechnungen
- os: Zum Durchsuchen des Dateisystems
- matplotlib.animation.FuncAnimation: Zum Erstellen der Animation
- PIL: Zum Laden und Bearbeiten von Bildern

Das Skript besteht aus den folgenden Hauptteilen:
1. Importieren der Module
2. Laden und Verarbeiten des Globus-Bildes
3. Definieren der Konstanten und Variablen
4. Definieren der Funktionen zum Plotten des Globus und der Trajektorie
5. Iterieren durch die XML-Dateien und Extrahieren der Trajektoriedaten
6. Erstellen des 3D-Plots und der Animation
"""
print("----------------")
print("----------------")
print("Programm 5 Start")
print("----------------")
print("----------------")
#importieren aller Module
import subprocess
subprocess.check_call(['pip', 'install', 'pillow', 'numpy', 'imageio'])
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os
import PIL
import imageio

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

# Das Bild f�r den Globus laden (entweder earthmap.jpg oder earthmap3.jpg)
bm = PIL.Image.open('Daten/BilderKreationGlobus/earthmap.jpg')
# Rescale, convert to array, and divide by 256 to get RGB values
# Gr�sse �ndern, zu einer array umwandeln und mit 256 dividieren um die RBG Werte zu erhalten
bm = np.array((np.array(bm.resize([int(round(d/1)) for d in bm.size])))/256)

# Koordinaten des Bildes
lons = np.linspace(-180, 180, bm.shape[1]) * np.pi/180 
lats = np.linspace(-90, 90, bm.shape[0])[::-1] * np.pi/180 

# Radius der Erde in KM
earth_radius = 6371
# F�r bessere Darstellung der Daten kleinere Erde
#earth_radius = 5000

# Variable i und gross_i definieren um itterieren zu k�nnen
i = 0
big_i = 0

# den Weg zu den XML-Daten angeben
xml_path = "Daten/XmlData"

# den Weg angeben, wo die erstellten Bilder abgelegt werden 
output_path = 'ZwischenAblage'
# den Ordner kreiren falls er nicht existiert
os.makedirs(output_path, exist_ok=True)

# Listen um die Umlaufbahn zu speichern
x_values = []
y_values = []
z_values = []

# Liste um die Bilder zu speichern
images = []

# Funktion um den Globus zu erstellen
def plot_earth_globe(ax):
    x = earth_radius * np.outer(np.cos(lons), np.cos(lats)).T
    y = earth_radius * np.outer(np.sin(lons), np.cos(lats)).T
    z = earth_radius * np.outer(np.ones(np.size(lons)), np.sin(lats)).T

    # Set transparency by adjusting the alpha channel of the facecolors
    facecolors = bm[:, :, :3]
    facecolors = np.concatenate([facecolors, np.full((facecolors.shape[0], facecolors.shape[1], 1), 0.13)], axis=2)

    ax.set_aspect('equal') 
    ax.plot_surface(x, y, z, rstride=4, cstride=4, facecolors=facecolors, shade=True)
    ax.set_aspect('equal') 


def plot_3d_trajectory(ax, x_values, y_values, z_values, markersize, linewidth):
    ax.set_aspect('equal')
    ax.plot(x_values, y_values, z_values, markersize=markersize, linewidth=linewidth, color='red', label='ISS Trajectory')
    ax.set_aspect('equal')


def plot_itteration(x_values, y_values, z_values, markersize, linewidth):
    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot the Earth
    plot_earth_globe(ax)
    
    # Plot the trajectory
    plot_3d_trajectory(ax, x_values=x_values, y_values=y_values, z_values=z_values, markersize=markersize, linewidth=linewidth)
    
    # Set labels and title
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('ISS Trajectory')
    # Save the figure
    image_path = os.path.join(output_path, f'{i}.png')
    plt.savefig(image_path)
    images.append(imageio.imread(image_path))

    plt.clf()
    plt.cla()
    plt.close()
        
    
    
    
# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Earth
# plot_earth_globe(ax)

# Iterate through all XML files in the folder
for file in os.listdir(xml_path):
    # Full path to the file
    file_path = os.path.join(xml_path, file)

    # Parse the XML file
    root = ET.parse(file_path)

    # Iterate through stateVector elements in the XML file
    for state_vector in root.findall(".//stateVector"):
        i += 1
        x = float(state_vector.find("X").text)
        y = float(state_vector.find("Y").text)
        z = float(state_vector.find("Z").text)

        x_values.append(x)
        y_values.append(y)
        z_values.append(z)
        
        if i < 30:
            plot_itteration(x_values, y_values, z_values, markersize=10, linewidth=10)
            print(i)
            
            
        elif i-8000 == 0:
            i -= 7969
            plot_itteration(x_values, y_values, z_values, markersize=0, linewidth=0.01)
            print(i)


output_path_final_picture = '5_Programm_ISS_Globe_HighRes_3d.gif'
output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)

# Create a GIF
imageio.mimsave(output_path_final_picture, images, duration=0.5)


print("----------------")
print("----------------")
print("Programm 5 Ende")
print("----------------")
print("----------------")

"""
Created on Sun Jan 10 15:08:16 2024

Dieses Skript verwendet die ISS-API, um die aktuelle Position der Internationalen Raumstation (ISS) abzurufen und auf einer Karte darzustellen.
Es werden die Module matplotlib, cartopy und requests verwendet.

Funktionen:
- get_iss_location(): Ruft die aktuelle Position der ISS über die ISS-API ab und gibt die Koordinaten zurück.
- plot_iss_trajectory(location, title): Plottet die aktuelle ISS-Position und die vorherigen Positionen auf einer Karte.
- update(): Aktualisiert die ISS-Position alle 5 Sekunden und zeigt den Plot an.

"""
print("----------------")
print("----------------")
print("Programm 6 Start")
print("----------------")
print("----------------")

#importieren der Module
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import requests 
import time
import os

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

# die Startzeit festsetzen, diese wird nicht überschrieben
start_time = time.time()
# diese Startzeit wird später überschrieben
start_time2 = time.time()

# Listen um die alten Kooridinaten zu speichern
x_values = []
y_values = [] 

# Funktion um die aktuelle Position zu erhalten
def get_iss_location():
    # Den ISS API verwenden um die aktuelle Position zu erhalten
    response = requests.get('http://api.open-notify.org/iss-now.json')
    # Die Daten in die "data" Variable zu packen
    data = response.json()

    # die Koordinate aus den Daten zurückgeben
    return {
        'latitude': float(data['iss_position']['latitude']),
        'longitude': float(data['iss_position']['longitude'])
    }

# Funktion um die ISS-Koordinate und die alten Date plotten
def plot_iss_trajectory(location, title):
    # Eine Karte erstellen
    fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    # Die aktuellen Koordinaten den Listen hinzufügen
    x_values.append(location['longitude'])
    y_values.append(location['latitude'])
    
    # optional: die Daten verschwinden nach gewisser Zeit wieder
    """if len(x_values) > 200:
        x_values.pop(0)
        y_values.pop(0)"""
    # Die neuen Punkte gross zu Plotten
    ax.plot(location['longitude'], location['latitude'], 'ro', label='ISS', alpha = 1)
    # Die alten Punkte durchsichtiger Plotten
    ax.plot(x_values, y_values, 'ro', label='ISS', alpha = 0.01)
    
    # Die Labels und den Titel setzten
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('ISS Trajectories on Earth Map')
    # optional: Die ganze Karte zeigen
    ax.set_global()
    # die Legende mit der aktuellen Position zeigen
    ax.legend([f'ISS Location (Real Time): ({location["latitude"]}, {location["longitude"]})'], loc='upper left', fontsize='small')
    # den Plot anzeigen
    # plt.show()
    output_path_final_picture = '6_Programm_ISS_CurrentLocation.png'
    output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)
    
    plt.savefig(output_path_final_picture)

# die Funktion um alles aufzuzeigen
def update():
    # die Variablen in der Funktion verfügbar machen
    global start_time, start_time2
    
    # die Funktion die unendlich Lange aufzeigen
    """while True:"""
    # optional: eine begrenzte Zeit die Funktion aufzeigen
    while time.time() - start_time < 100:

        # alle 5 Sekunden einen neuen Plot aufzeigen
        if time.time() - start_time2 >= 5:
            # die Zeit zur aktuellen setzten, damit es wieder 5 Sekunden sind
            start_time2 = time.time()
            # die aktuelle Position erhalten
            location = get_iss_location()
            # diese Position in die plotting Funktion geben
            plot_iss_trajectory(location, 'ISS Position')
            # ausgabe der Koordinaten in dem Terminal
            print(f'Updated ISS location: {location}')

# Die Plots anzeigen
update()

print("----------------")
print("----------------")
print("Programm 6 Ende")
print("----------------")
print("----------------")

"""
Erstellt am Mi Jan 18 13:48:16 2024

Dieses Skript ruft den vorhergesagten Standort der Internationalen Raumstation (ISS) mithilfe der N2YO-API ab.
Es berechnet die Startzeit des nächsten ISS-Überflugs f�r den automatisch erhaltenen Aufenthaltsorts des Nutzer zur�ck.
Es holt auch die h�he des Ortes, des Nutzers und gibt die �berflugszeit in der Zeitzone des Beobachters zur�ck.
Ausserdem werden auch noch die Wettervorhersagen in das Programm mit einbezogen, um ein genaueres Ergebniss zu erhalten.
Hier wird besonders auf die Wolken acht gegeben, wobei auch die Sicherheit f�r diese Aussage gegeben wird.
All dies wird in einem Plot als Text ausgegeben, wobei auf den Karten noch die Wetterdaten gezeigt werden.
Dies wird erreicht mit folgenden APIs:
                N2YO-API: https://www.n2yo.com/api/
                GeoNames-API: http://api.geonames.org/
                IPInfo-API: https://ipinfo.io
                Open-Elevevation-API: https://api.open-elevation.com/api/v1/
                OpenWeatherAPI: https://api.openweathermap.org/data/2.5

Autor: sirot
"""
print("----------------")
print("----------------")
print("Programm 7 Start")
print("----------------")
print("----------------")
# importieren der Module
import datetime
import requests
from pytz import timezone 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.image as mpimg
import os

# Die nächsten überflüge als Zahl, default = 0
# (falls man nicht die nächste, sondern irgend eine danach will, so muss man dies auswählen)
# (die Zahlen werden im Plot auch angezeigt)
next_pass_num = 0

# finale Bilder
output_path_final = 'Finale_Bilder'
os.makedirs(output_path_final, exist_ok=True)

def get_iss_position_data(observer_latitude, observer_longitude, observer_altitude, observable_days, observable_seconds):
    """
    Ruft den vorhergesagten Standort der ISS ab und berechnet die Startzeit des nächsten ISS-Überflugs.

    Parameter:
    observer_latitude (float): Die Breitengrad des Beobachtungsortes.
    observer_longitude (float): Die Längengrad des Beobachtungsortes.
    observer_altitude (int): Die Höhe des Beobachtungsortes in Metern.
    observable_days (int): Die Anzahl der Tage, für die die ISS-Überflugvorhersagen abgerufen werden sollen (maximal 10).
    observable_seconds (int): Die Anzahl der Sekunden, die für jeden ISS-Überflug berücksichtigt werden sollen.
    seconds_in_future (int): Die Anzahl der Sekunden in der Zukunft, um die Startzeit des ISS-Überflugs vorherzusagen (Standardwert ist 0).

    Rückgabe:
    datetime.datetime: Die Startzeit des nächsten ISS-Überflugs in der Zeitzone des Beobachters.
    """
    # leere Listen erstellen
    start_time_gmt_list = []
    start_time_utc_list = []
    start_compass_list = []
    end_compass_list = []
    iss_mag_list = []
    iss_duration_list = []

    # Verwenden Sie die N2YO-API, um den Standort der ISS zu einem zukünftigen Zeitpunkt zu erhalten
    iss_position_url = f"https://api.n2yo.com/rest/v1/satellite/visualpasses/25544/{observer_latitude}/{observer_longitude}/{observer_altitude}/{observable_days}/{observable_seconds}/&apiKey=NJDDHW-KZPFKB-XTCUM9-56XH"
    response = requests.get(iss_position_url)
    iss_data = response.json()
    
    # Anzahl Sichtungen
    passescount = iss_data['info']['passescount']

    i = 0
    for i in range (0, passescount):
        # Holen der Startzeit und weiteren Faktoren des nächsten ISS-Überflugs
        start_utc = iss_data['passes'][i]['startUTC']
        start_compass = iss_data['passes'][i]['startAzCompass']
        end_compass = iss_data['passes'][i]['endAzCompass']
        iss_mag = iss_data['passes'][i]['mag']
        iss_duration = iss_data['passes'][i]['duration']

        start_time_utc_list.append(start_utc)
        start_compass_list.append(start_compass)
        end_compass_list.append(end_compass)
        iss_mag_list.append(iss_mag)
        iss_duration_list.append(iss_duration)


        # Konvertieren Sie den Unix-Zeitstempel in ein datetime-Objekt
        start_time = datetime.datetime.fromtimestamp(start_utc)

        # Holen die Zeitzone für den Beobachtungsort
        geonames_username = "sansiro8"  # GeoNames-Benutzernamen
        timezone_url = f"http://api.geonames.org/timezoneJSON?lat={observer_latitude}&lng={observer_longitude}&username={geonames_username}"
        response = requests.get(timezone_url)
        timezone_data = response.json()
        # Wenn die Zeitzone-ID verfügbar ist, wird eine Zeitzone damit erstellt
        if 'timezoneId' in timezone_data:
            observer_timezone = timezone(timezone_data['timezoneId'])
        # Andernfalls verwenden man den GMT-Offset, um eine Zeitzone zu erstellen
        else:
            gmt_offset = timezone_data['gmtOffset']
            observer_timezone = timezone(f"Etc/GMT{'+' if gmt_offset < 0 else '-'}{abs(gmt_offset)}")

        start_time_gmt = start_time.astimezone(observer_timezone)
        start_time_gmt_list.append(start_time_gmt)

    return start_time_gmt_list, start_compass_list, end_compass_list, iss_mag_list, iss_duration_list, passescount, start_time_utc_list


def get_location():
    response = requests.get('https://ipinfo.io')
    data = response.json()
    return data

def get_elevation(lat, lon):
    url = f"https://api.open-elevation.com/api/v1/lookup?locations={lat},{lon}"
    response = requests.get(url)
    data = response.json()
    if 'results' in data:
        return data['results'][0]['elevation']
    return elevation == 0


location_data = get_location()
#print(location_data['loc'])

loc = location_data['loc']
lat, lon = map(float, loc.split(','))

elevation = get_elevation(lat, lon)
# Ersetzen Sie die Beobachterkoordinaten durch Ihren gewünschten Standort
observer_latitude = lat  #kann auch manuell gesetzt werden. Zum Beispiel 47.36667
observer_longitude = lon
observer_altitude = elevation


observer_city = location_data['city']

# Anzahl der vorhergesagten Tage (maximal 10)
observable_days = 10

# Anzhal sichtbarer Sekunden
observable_seconds = 300

# Die Rechnung
next_visibility_time = get_iss_position_data(observer_latitude, observer_longitude, observer_altitude, observable_days, observable_seconds)


"""
Von hier werden die Wetterdaten abgerufen
"""


def get_weather_data(lat, lon):
    api_key = "390f981cb9c1c7b65ad370164ffdb47a"
    base_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={observer_latitude}&lon={observer_longitude}&appid={api_key}"
    map_url_precipitation = f"https://tile.openweathermap.org/map/precipitation/0/0/0.png?appid=390f981cb9c1c7b65ad370164ffdb47a"
    map_url_wind = f"https://tile.openweathermap.org/map/wind/0/0/0.png?appid=390f981cb9c1c7b65ad370164ffdb47a"

    # parameters for the API request
    params = {
        "lat": observer_latitude,
        "lon": observer_longitude,
        "appid": api_key
    }

    # send the API request
    response = requests.get(base_url, params=params)
    response_map_pre = requests.get(map_url_precipitation, stream=True)
    response_map_wind = requests.get(map_url_wind, stream=True)

    # parse the response as JSON
    weather_data = response.json()

    if response_map_pre.status_code == 200:
        with open("weather_map_pre.png", "wb") as file:
            file.write(response_map_pre.content) 
    else:
        print("Error Map Rain")


    if response_map_wind.status_code == 200:
        with open("weather_map_wind.png", "wb") as file:
            file.write(response_map_wind.content)
    else:
        print("Error Map Temp")

    return weather_data

# get the weather data for the observer's location
weather_data = get_weather_data(observer_latitude, observer_longitude)

weather_part = weather_data['cnt']
city_name = weather_data['city']['name']
weather_step = 3*60*60 # 3 Stunden = Zeit zwischen Wettervorhersagen

weather_next_visibility_clouds_list = []
weather_next_visibility_clouds = 0
weather_next_visibility_prob_list = []
weather_next_visibility_prob = 0
weather_next_visibility_weather_list = []

# Die Daten in Listen einlesen
for i in range(0, weather_part):
    if abs(next_visibility_time[6][next_pass_num] - weather_data['list'][i]['dt']) <= weather_step:
        weather_next_visibility_clouds_list.append(weather_data['list'][i]['clouds']['all'])
        weather_next_visibility_prob_list.append(weather_data['list'][i]['pop'])
        weather_next_visibility_weather_list.append(weather_data['list'][i]['weather'][0]['description'])

weather_next_visibility_coulds_average = sum(weather_next_visibility_clouds_list) / len(weather_next_visibility_clouds_list)
weather_next_visibility_prob_average = sum(weather_next_visibility_prob_list) / len(weather_next_visibility_prob_list)
weather_next_visibility_weather_list_unique = list(set(weather_next_visibility_weather_list))

weather_next_visibility_prob_average = round(100*weather_next_visibility_prob_average)

if weather_next_visibility_coulds_average > 80:
    message_clouds = "very poorly"
elif weather_next_visibility_coulds_average > 60:
    message_clouds = "badly"
elif weather_next_visibility_coulds_average > 40:
    message_clouds = "decently"
elif weather_next_visibility_coulds_average > 20:
    message_clouds = "good"
else:
    message_clouds = "very good"

print(message_clouds)
print(weather_next_visibility_coulds_average, weather_next_visibility_prob_average)
print(weather_next_visibility_weather_list_unique)

if next_pass_num == 0:
    next_pass_num_message = "first"
elif next_pass_num == 1:
    next_pass_num_message = "second"
elif next_pass_num == 2:
    next_pass_num_message = "third"
else:
    next_pass_num_message = "(next_pass_num + 1)"+"th"
"""
Von hier an werden die wichtigen Daten auf einem Plot dargestellt
"""
# Erstellen Sie eine Figure und zwei Subplots nebeneinander
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'projection': ccrs.PlateCarree()})

# Zeichnen Sie die Küstenlinien auf beiden Subplots
ax1.coastlines(alpha=1)
ax2.coastlines(alpha=1)

# Laden Sie das Wetterkartenbild
weather_map_img_pre = mpimg.imread('weather_map_pre.png')
weather_map_img_temp = mpimg.imread('weather_map_wind.png')

# Überlagern Sie das Wetterkartenbild auf beiden Karten
ax1.imshow(weather_map_img_pre, extent=[-180, 180, -90, 90], alpha=1)
ax2.imshow(weather_map_img_temp, extent=[-180, 180, -90, 90], alpha=1)


# die Laufbahn der ISS plotten
ax1.plot(observer_longitude, observer_latitude, label='ISS Passing at your Location', marker='o', markersize=5, linewidth=1, color='red', linestyle='dashed')
ax2.legend(loc='lower left')
# Labels und Titel setzen
ax1.set_xlabel('Longitude')
ax1.set_ylabel('Latitude')
ax1.set_title('ISS Passing Rain Map')

# die Laufbahn der ISS plotten
ax2.plot(observer_longitude, observer_latitude, label='ISS Passing at your Location', marker='o', markersize=5, linewidth=1, color='red', linestyle='dashed')
ax2.legend(loc='lower left')
# Labels und Titel setzen
ax2.set_xlabel('Longitude')
ax2.set_ylabel('Latitude')
ax2.set_title('ISS Passing Wind Map')

# Das Plot nach unten erweitern
fig.subplots_adjust(bottom=0.52)
# Den Text in der Karte platzieren
fig.text(0.02, 0.5, f'This predicts the ISS passing at your Location ({observer_latitude}, {observer_longitude}) in the city of {observer_city}')
fig.text(0.02, 0.46, f'In the next {observable_days} days, the ISS will be visible {next_visibility_time[5]} times for longer than {observable_seconds} seconds', transform=fig.transFigure)
fig.text(0.05, 0.42, f'The {next_pass_num_message} pass of the ISS will be visible on the {next_visibility_time[0][next_pass_num].strftime("%d.%m.%Y")} at {next_visibility_time[0][next_pass_num].strftime("%H:%M:%S")} for {next_visibility_time[4][next_pass_num]} seconds.', transform=fig.transFigure)
fig.text(0.05, 0.38, f'It will be visible whilst flying from {next_visibility_time[1][next_pass_num]} to {next_visibility_time[2][next_pass_num]} with a magnitude of {next_visibility_time[3][next_pass_num]}.', transform=fig.transFigure)
fig.text(0.05, 0.34, f'There is a cloud coverage of {weather_next_visibility_coulds_average} %, which means you can see the ISS {message_clouds}.', transform=fig.transFigure)
fig.text(0.05, 0.30, f'The probability of the weather predicitons being correct is {weather_next_visibility_prob_average} %.', transform=fig.transFigure)
fig.text(0.05, 0.26, f'The weather predictions is {weather_next_visibility_weather_list_unique[0]}', transform=fig.transFigure)

fig.text(0.03, 0.17, f'Other times for the passing of the ISS are (Number for more detailed prediction):', transform=fig.transFigure)

for i in range(0, next_visibility_time[5], 3):
    if i+2 < next_visibility_time[5]:
        fig.text(0.05, 0.13 - 0.01*i, f'({i}) {next_visibility_time[0][i].strftime("%d.%m.%Y %H:%M:%S")} // ({i+1}) {next_visibility_time[0][i+1].strftime("%d.%m.%Y %H:%M:%S")} // ({i+2}) {next_visibility_time[0][i+2].strftime("%d.%m.%Y %H:%M:%S")}', transform=fig.transFigure)
    elif i+1 < next_visibility_time[5]:
        fig.text(0.05, 0.13 - 0.01*i, f'({i}) {next_visibility_time[0][i].strftime("%d.%m.%Y %H:%M:%S")} // ({i+1}) {next_visibility_time[0][i+1].strftime("%d.%m.%Y %H:%M:%S")}', transform=fig.transFigure)
    else:
        fig.text(0.05, 0.13 - 0.01*i, f'({i}) {next_visibility_time[0][i].strftime("%d.%m.%Y %H:%M:%S")}', transform=fig.transFigure)

#optional: ganze Welkarte anzeigen
ax1.set_global()
ax2.set_global()
 
plt.subplots_adjust(wspace=0.01, right=0.95, left=0.05, top = 0.95)
# Die Grafik anzeigen
# plt.legend()
# plt.show()
output_path_final_picture = '7_Programm_ISS_Prediction.png'
output_path_final_picture = os.path.join(output_path_final, output_path_final_picture)

plt.savefig(output_path_final_picture)

print("done")

print("----------------")
print("----------------")
print("Programm 7 Ende")
print("----------------")
print("----------------")




print("***************************")
print("***************************")
print("***************************")
print("Alle Programme sind beendet")
print("***************************")
print("***************************")
print("***************************")
