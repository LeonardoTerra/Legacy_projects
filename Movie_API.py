import requests
import json

url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

movie = {"s": input("Qual Filme: "), "y": input("Lançamento: "), "page": "1", "r": "json"}

headers = {
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    'x-rapidapi-key': "f9522cd937msh8b6556fa112decbp10f28cjsna4274bbfd5be"
}

response = requests.get("https://movie-database-imdb-alternative.p.rapidapi.com/", headers=headers,
                        params=movie)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


jprint(response.json())
