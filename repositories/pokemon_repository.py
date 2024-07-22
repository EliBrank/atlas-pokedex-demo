import requests
from models.pokemon import Pokemon

class PokemonRepository:
    def __init__(self):
        self.base_url = "https://pokeapi.co/api/v2"

    def get_pokemon(self, pokemon_name) -> Pokemon:
        url = f"{self.base_url}/pokemon/{pokemon_name}"
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            name = pokemon_data["name"]
            type = [type["type"]["name"] for type in pokemon_data["types"]]
            abilities = [ability["ability"]["name"] for ability in pokemon_data["abilities"]]
            height = pokemon_data["height"]
            weight = pokemon_data["weight"]
            image = pokemon_data["sprites"]["front_default"]
            return Pokemon(name, type, abilities, height, weight, image)
        else:
            return None
