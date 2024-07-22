import requests
from models.pokemon import Pokemon

class CaughtPokemonRepository:
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000/pokemon"

    def get_caught_pokemon(self) -> list[Pokemon]:
        # This method should return a list of caught Pokemon from the database.
        response = requests.get(self.base_url)
        caught_pokemon = []
        if response.status_code == 200:
            pokemon_data = response.json()
            for pokemon in pokemon_data:
                capture_id = pokemon["capture_id"]
                name = pokemon["name"]
                type = pokemon["type"]
                abilities = pokemon["abilities"]
                height = pokemon["height"]
                weight = pokemon["weight"]
                image = pokemon["image"]
                caught_pokemon.append(Pokemon(name, type, abilities, height, weight, image, capture_id))
        return caught_pokemon

    def catch_pokemon(self, pokemon: Pokemon):
        # This method should add a caught Pokemon to the database.
        data = {
            "name": pokemon.name,
            "type": pokemon.type,
            "abilities": pokemon.abilities,
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image": pokemon.image
        }
        response = requests.post(self.base_url, json=data)
        return response.status_code == 200

    def release_pokemon(self, capture_id: int):
        # This method should remove a caught Pokemon from the database.
        url = f"{self.base_url}/release/{capture_id}"
        response = requests.delete(url)
        return response.status_code == 200
