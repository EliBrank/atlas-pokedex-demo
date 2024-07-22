import sqlite3
from models.pokemon import Pokemon

class PokemonDB:
    def __init__(self):
        self.connection = sqlite3.connect("db/pokemon.db", check_same_thread=False)
        self.cursor = self.connection.cursor()

        # Create the table if it doesn't exist
        query = "CREATE TABLE IF NOT EXISTS pokemon (capture_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, type TEXT, abilities TEXT, height INTEGER, weight INTEGER, image TEXT)"
        self.cursor.execute(query)

    def get_caught_pokemon(self) -> list[Pokemon]:
        query = "SELECT * FROM pokemon"
        self.cursor.execute(query)
        pokemon_data = self.cursor.fetchall()
        caught_pokemon = []
        for pokemon in pokemon_data:
            capture_id, name, type, abilities, height, weight, image = pokemon
            caught_pokemon.append(Pokemon(name, type, abilities, height, weight, image, capture_id))
        return caught_pokemon

    def catch_pokemon(self, pokemon: Pokemon):
        query = "INSERT INTO pokemon (name, type, abilities, height, weight, image) VALUES (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (pokemon.name, pokemon.type, pokemon.abilities, pokemon.height, pokemon.weight, pokemon.image))
        self.connection.commit()

    def release_pokemon(self, capture_id: int):
        query = "DELETE FROM pokemon WHERE capture_id = ?"
        self.cursor.execute(query, (capture_id,))
        self.connection.commit()

    def close(self):
        self.connection.close()

