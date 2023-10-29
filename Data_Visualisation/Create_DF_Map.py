# %%
import pandas as pd
import random

# List of USA states and their abbreviations
states = [
    {"State": "Alabama", "Abbreviation": "AL"},
    {"State": "Alaska", "Abbreviation": "AK"},
    {"State": "Arizona", "Abbreviation": "AZ"},
    {"State": "Arkansas", "Abbreviation": "AR"},
    {"State": "California", "Abbreviation": "CA"},
    {"State": "Colorado", "Abbreviation": "CO"},
    {"State": "Connecticut", "Abbreviation": "CT"},
    {"State": "Delaware", "Abbreviation": "DE"},
    {"State": "Florida", "Abbreviation": "FL"},
    {"State": "Georgia", "Abbreviation": "GA"},
    {"State": "Hawaii", "Abbreviation": "HI"},
    {"State": "Idaho", "Abbreviation": "ID"},
    {"State": "Illinois", "Abbreviation": "IL"},
    {"State": "Indiana", "Abbreviation": "IN"},
    {"State": "Iowa", "Abbreviation": "IA"},
    {"State": "Kansas", "Abbreviation": "KS"},
    {"State": "Kentucky", "Abbreviation": "KY"},
    {"State": "Louisiana", "Abbreviation": "LA"},
    {"State": "Maine", "Abbreviation": "ME"},
    {"State": "Maryland", "Abbreviation": "MD"},
    {"State": "Massachusetts", "Abbreviation": "MA"},
    {"State": "Michigan", "Abbreviation": "MI"},
    {"State": "Minnesota", "Abbreviation": "MN"},
    {"State": "Mississippi", "Abbreviation": "MS"},
    {"State": "Missouri", "Abbreviation": "MO"},
    {"State": "Montana", "Abbreviation": "MT"},
    {"State": "Nebraska", "Abbreviation": "NE"},
    {"State": "Nevada", "Abbreviation": "NV"},
    {"State": "New Hampshire", "Abbreviation": "NH"},
    {"State": "New Jersey", "Abbreviation": "NJ"},
    {"State": "New Mexico", "Abbreviation": "NM"},
    {"State": "New York", "Abbreviation": "NY"},
    {"State": "North Carolina", "Abbreviation": "NC"},
    {"State": "North Dakota", "Abbreviation": "ND"},
    {"State": "Ohio", "Abbreviation": "OH"},
    {"State": "Oklahoma", "Abbreviation": "OK"},
    {"State": "Oregon", "Abbreviation": "OR"},
    {"State": "Pennsylvania", "Abbreviation": "PA"},
    {"State": "Rhode Island", "Abbreviation": "RI"},
    {"State": "South Carolina", "Abbreviation": "SC"},
    {"State": "South Dakota", "Abbreviation": "SD"},
    {"State": "Tennessee", "Abbreviation": "TN"},
    {"State": "Texas", "Abbreviation": "TX"},
    {"State": "Utah", "Abbreviation": "UT"},
    {"State": "Vermont", "Abbreviation": "VT"},
    {"State": "Virginia", "Abbreviation": "VA"},
    {"State": "Washington", "Abbreviation": "WA"},
    {"State": "West Virginia", "Abbreviation": "WV"},
    {"State": "Wisconsin", "Abbreviation": "WI"},
    {"State": "Wyoming", "Abbreviation": "WY"},
]

# Create a DataFrame with random PM2.5 values between 50 and 100
import pandas as pd
import json

# Read the JSON file
with open('./us-states.json', 'r') as file:
    data = json.load(file)

# Initialize lists to store data
abbreviations = []
state_names = []
coordinates = []

# Extract data from JSON
for item in data['features']:
    abbreviation = item['id']
    name = item['properties']['name']
    coords = item['geometry']['coordinates']

    # Append data to lists
    abbreviations.append(abbreviation)
    state_names.append(name)
    coordinates.append(coords)    

# Create a DataFrame
df = pd.DataFrame({
    'State Abbreviation': abbreviations,
    'State Name': state_names,
    'Coordinates': coordinates,
})

 
df['PM2.5'] = [random.uniform(50, 100) for _ in range(len(df))]
df.head()

# %%
import folium
map = folium.Map(location=[45, -102], zoom_start=4)
folium.Choropleth(
    geo_data="./us-states.json",
    data=df,
    columns=["State Abbreviation", "PM2.5"],
    key_on="feature.id",
    fill_color="YlOrBr",
    fill_opacity=0.3,
    line_opacity=1.0,
    legend_name="PM2.5",
    highlight=True,
    name="PM2.5",
    tooltip=folium.GeoJsonTooltip(fields=["State Abbreviation", "PM2.5"], aliases=["State", "PM2.5"], localize=True, sticky=True)
).add_to(map)

# %%

for feature in folium.features.GeoJson("./us-states.json").data['features']:
    state_name = feature['properties']['name']
    pm25_value = df[df["State Name"] == state_name]["PM2.5"].values[0] if state_name in df["State Name"].values else "Data not available"
    folium.GeoJson(feature, 
                   style_function=lambda x: {'fillOpacity': 0.01, 'color': 'black', "weight": 0.1},
                   highlight_function=lambda x: {'fillOpacity': 0.4, 'color': 'black', "weight": 0.1 },
                   tooltip=f"{state_name}<br>PM2.5: {pm25_value}").add_to(map)
# %%
map

# %%
