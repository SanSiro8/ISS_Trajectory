# ISS_Trajectory

These are different ways of plotting the ISS trajectory over the earth.

## The API keys are deleted in this script and should be included individually.

This script contains several programs for creating images and visualizations of the ISS trajectory. Each program has its own function and is executed sequentially.

### Program 1: This program reads CSV files with ISS motion data and creates a map of ISS trajectories on the Earth. The data is already in polar coordinates and is shown on the map. It also shows where and how many photos were taken.

### Program 2: This program reads XML data about the ISS space station and converts Cartesian coordinates into longitudinal and lateral coordinates. The longitude and latitude of the ISS trajectory are shown on a 2D map of the world.

### Program 3: This program visualizes the 3D trajectory of the ISS based on XML data. This is done on a transparent sphere to better show the orbit.

### Program 4: This program visualizes the trajectory of the ISS on a rotating 3D globe in 2D. It creates a GIF that shows the rotating Earth with the ISS orbit above it.

### Program 5: This program visualizes the trajectory of the ISS on a 3D globe. The data can be rotated in the graphic and seen from all sides. The ISS is plotted at the correct height above the Earth, and its orbit is also visible.

### Program 6: This program visualizes the current position of the ISS on a map. It uses an API to obtain the position of the ISS at the time the program is run. This location is then updated on the map for a period or indefinitely.

### Program 7: This script retrieves the predicted location of the International Space Station (ISS) using the N2YO API. It calculates the start time of the next ISS pass for the user's automatically obtained location. It also retrieves the altitude of the user's location and returns the pass time in the observer's time zone. Weather forecasts are also included in the program to obtain a more accurate result, with a particular focus on clouds, ensuring the safety of this statement. All this is output as text in a plot, with weather data shown on the maps.


            Hinweis:    
            Die XML-Daten werden von der offiziellen NASA-Website heruntergeladen: https://data.nasa.gov/browse?q=ISS+COORDS
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
