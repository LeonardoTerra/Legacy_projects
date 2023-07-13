# Packages

import requests
import json

# Latitude and Longitude data
city_data = {
    "latitude": input("Latitude: "),
    "longitude": input("Longitude: "),
}

# Access data. Without it, it's not possible to access the API
headers = {
    'x-rapidapi-host': "countries-cities.p.rapidapi.com",
    'x-rapidapi-key': "f9522cd937msh8b6556fa112decbp10f28cjsna4274bbfd5be"
}

response = requests.get("https://countries-cities.p.rapidapi.com/location/city/nearby", headers=headers,
                        params=city_data)


# Json dictionary format

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


# Printing city and population, regardless of other keys.
for i in response.json()["cities"]:
    print(f"City: {i['name']}")
    print(f"Population: {i['population']}")
