# ISS_Trajectory
These are different ways of plotting the ISS-Trajectory over the earth

Dieses Skript enthält mehrere Programme zur Erstellung von Bildern und Visualisierungen der ISS-Trajektorie.
Jedes Programm hat eine eigene Funktion und wird nacheinander ausgefÃ¼hrt.

Programm 1:
Dieses Programm liest CSV-Dateien mit ISS-Bewegungsdaten ein und erstellt eine Karte der ISS-Trajektorien auf der Erde.
Die Daten sind schon in Polar-Koordinaten und werden auf der Karte gezeigt. Hier wird auch ersichtlich, wo wieviele Fotos gemacht wurden.

Programm 2:
Dieses Programm liest XML-Daten über die ISS-Spacestation ein und konvertiert die kartesischen Koordinaten in longitudinale und laterale Koordinaten.
Es werden die Längen- und Breitengrade der ISS-Trajektorie auf einer 2D-Karte der Welt dargestellt.

Programm 3:
Dieses Programm visualisiert die 3D-Trajektorie der ISS basierend auf XML-Daten.
Dies wird hier auf einer durchsichtigen Kugel gemacht, um die Umlaufbahn besser zu zeigen

Programm 4:
Dieses Programm visualisiert die Trajektorie der ISS auf einem rotierenden 3D-Globus in 2D.
Es wird ein GIF erstellt, welches die rotierende Erdkugel mit den ISS-Laufbahn darüber zeigt

Programm 5:
Dieses Programm visualisiert die Trajektorie der ISS auf einem 3D-Globus.
Die Daten können in der Grafik rotiert und somit von allen Seiten gesehen werden. 
Die ISS wird in der richtigen höhe über der Erde geplottet und es wird auch Ihre umlaufbahn sichtbar.

Programm 6:
Dieses Programm visualisiert die aktuelle Position der ISS auf einer Karte.
Es verwendet ein API um die Position der ISS zum Zeitpunkt des laufens des Programmes zu erhalten.
Diese Ortschaft wird dann für einen Zeitraum oder unendlich lange auf der Karte erneuert.

Programm 7:
Dieses Skript ruft den vorhergesagten Standort der Internationalen Raumstation (ISS) mithilfe der N2YO-API ab.
Es berechnet die Startzeit des nÃ¤chsten ISS-Ãberflugs für den automatisch erhaltenen Aufenthaltsorts des Nutzer zurück.
Es holt auch die höhe des Ortes, des Nutzers und gibt die Überflugszeit in der Zeitzone des Beobachters zurück.
Ausserdem werden auch noch die Wettervorhersagen in das Programm mit einbezogen, um ein genaueres Ergebniss zu erhalten.
Hier wird besonders auf die Wolken acht gegeben, wobei auch die Sicherheit für diese Aussage gegeben wird.
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
                
            Es werden folgende Librarys/Module verwendet (müssen installiert werden):
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
