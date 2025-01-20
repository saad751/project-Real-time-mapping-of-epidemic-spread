import folium
import pandas as pd
import matplotlib.pyplot as plt

# Configure pandas display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def holder():
    # Load COVID-19 data and country codes
    try:
        data = pd.read_csv("C:/Users/sadiy/Downloads/COVID-19-HEAT-MAP-master/COVID-19-HEAT-MAP-master/covid.csv")
        ccode = pd.read_csv("C:/Users/sadiy/Downloads/COVID-19-HEAT-MAP-master/COVID-19-HEAT-MAP-master/CountryCodes.csv")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    df1 = pd.DataFrame(data)
    df2 = pd.DataFrame(ccode).set_index('alpha3')

    # Debug: Check columns
    print("Columns in the dataset:")
    print(df1.columns)

    # Debug: Check available dates
    print("Available dates in the dataset:")
    print(df1['date'].unique())

    # Lists to store latitude and longitude
    long = []
    lat = []

    # Add latitude and longitude to the data
    for x in df1['iso_code']:
        try:
            lat.append((df2.loc[x, 'latitude']))
            long.append((df2.loc[x, 'longitude']))
        except KeyError:
            print(f"Missing coordinates for {x}")
            lat.append(None)
            long.append(None)

    df1['Latitude'] = lat
    df1['Longitude'] = long

    # Debug: Check latitude and longitude mapping
    print("Latitude/Longitude Mapping:")
    print(df1[['iso_code', 'Latitude', 'Longitude']].head())

    # Filter data for a specific date
    selected_date = '2020-03-20'  # Adjust date to one available in your dataset
    test = df1.loc[df1['date'] == selected_date].fillna(0)
    
    if test.empty:
        print(f"No data found for the selected date: {selected_date}")
        return

    # Debug: Check data for the selected date
    print(f"Filtered Data for {selected_date}:")
    print(test.head())

    test2 = test.set_index('iso_code', drop=True)

    # Initialize the folium map
    map1 = folium.Map(location=[0, 0], max_bounds=True, zoom_start=3, min_zoom=2, tiles='OpenStreetMap')
    fg = folium.FeatureGroup(name='Current spread of Coronavirus')

    # Add a GeoJSON layer for visualization
    try:
        with open("C:/Users/sadiy/Downloads/COVID-19-HEAT-MAP-master/COVID-19-HEAT-MAP-master/world.json", 'r', encoding='utf-8-sig') as geojson_file:
            fg.add_child(folium.GeoJson(
                data=geojson_file.read(),
                style_function=lambda z: {
                    'fillColor': color(test2, z['properties']['ISO3']),
                    'color': 'black',
                    'weight': 0.5,
                    'fillOpacity': 0.7
                }
            ))
    except FileNotFoundError as e:
        print(f"Error loading GeoJSON file: {e}")
        return

    # Add markers for each country
    for i in test.index:
        latitude = test.loc[i, 'Latitude']
        longitude = test.loc[i, 'Longitude']
        if not pd.isna(latitude) and not pd.isna(longitude):
            fg.add_child(folium.Marker(
                location=[latitude, longitude],
                popup=graph(test, i),
                icon=folium.Icon(color='red')
            ))

    # Add the feature group to the map and save it
    map1.add_child(fg)
    map1.save('test1.html')

# Generates HTML for the popup
def graph(gdata, i):
    return (f"<b><font color='red'>Date:</font></b> {gdata.loc[i, 'date']}<br>"
            f"<b><font color='red'>Country:</font></b> {gdata.loc[i, 'location']}<br>"
            f"<b><font color='red'>Cases:</font></b> {gdata.loc[i, 'total_cases']}<br>"
            f"<b><font color='red'>Deaths:</font></b> {gdata.loc[i, 'total_deaths']}")

# Returns the case rate for coloring
def color(pdata, z):
    if z in pdata.index:
        value = pdata.loc[z, 'total_cases_per_million']
        if value == 0:
            return 'Red'
        elif value <= 200:
            return 'Blue'
        elif value > 200 and value < 1000:
            return 'Green'
        else:
            return 'Yellow'
    return 'White'

# Run the holder function
holder()
