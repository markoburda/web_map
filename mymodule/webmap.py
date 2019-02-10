import folium
from sort_copy import sort
import csv
from geopy import geocoders
from geopy.exc import GeocoderTimedOut


def locate(year):
    """
    Creates map with different layers and saves into html file
    """
    geolocator = geocoders.Bing("AvTwq-4RAgtYf7_QjeCylW_rnqmA_FLYOUte8pWYNK19EhWbAbve6A-FMvgDRL4t", timeout=None)
    map = folium.Map(location=[48.314775, 25.082925], zoom_start=2)
    fg_fs = folium.FeatureGroup(name = "Films in " + year)
    fg_pn = folium.FeatureGroup(name = "Population")
    fg_pn.add_child(folium.GeoJson(data=open('world.json', 'r',
                    encoding='utf-8-sig').read(),
                    style_function=lambda x: {'fillColor':'green'
                    if x['properties']['POP2005'] < 10000000
                    else 'orange' if 10000000 <=
                    x['properties']['POP2005'] < 20000000 else 'red'}))
    with open('locations.csv') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row[0], row[1])
            location = geolocator.geocode(row[2])
            fg_fs.add_child(folium.Marker(location=[location.latitude, location.longitude], popup=row[0]))
    map.add_child(fg_fs)
    map.add_child(fg_pn)
    map.add_child(folium.LayerControl())
    map.save('map.html')


try:
    year = input("Year: ")
    sort('locations.list', year)
    locate(year)
except GeocoderTimedOut as err:
    pass
except AttributeError as err:
    pass
except IndexError as err:
    pass
