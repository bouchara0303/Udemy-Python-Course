import folium
import pandas
from jedi.api import names
coordinatesList = [
   [39.37020, -94.78178, 'Platte City', 'This is a town near my home town'],
   [39.09895, -94.57253, 'Kansas City', 'This is one of the largest cities in Missouri'],
   [36.08412, -94.17344, 'Fayetteville', 'This is the home of the Razorbacks'],
   [39.57956, -105.93441, 'Keystone', 'This is one of my favorite ski resorts']
   ]
volcanoes = pandas.read_csv('volcanoes.txt')

def getColor(elevation):
    if elevation < 1000.0:
        return 'green'
    elif (elevation >= 1000.0) and (elevation < 2000.0):
        return 'orange'
    elif (elevation >= 2000.0) and (elevation < 3000.0):
        return 'red'
    else:
        return 'purple'
    
austinMap = folium.Map(location=[39.33643711766414, -94.56801585902234], zoom_start=5)
for lat, long, names, elev in zip(volcanoes['LAT'], volcanoes['LON'], volcanoes['NAME'], volcanoes['ELEV']):
    austinMap.add_child(folium.Marker(location=[lat, long], popup = names + ' - Elevation: ' + str(elev), icon = folium.Icon(color = getColor(elev))))
layer = folium.FeatureGroup(name='Average Temp.')

for locs in coordinatesList:
    austinMap.add_child(folium.Marker(location=[locs[0], locs[1]], popup= locs[3], icon=folium.Icon(color='blue')), name=locs[2])
    


austinMap.add_child(layer)

austinMap.save('AustinMap.html')
