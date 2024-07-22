import json
from flask import Flask, request, jsonify
from db.pokemon_db import PokemonDB
from models.pokemon import Pokemon

app = Flask(__name__)

db = PokemonDB()

@app.route('/pokemon', methods=['POST'], strict_slashes=False)
def catch_pokemon():
    """
    Endpoint to catch a Pokémon and add it to the database.

    Example request payload:
    {
        "name": "pikachu",
        "type": "Electric",
        "abilities": ["Static", "Lightning Rod"],
        "height": 0.4,
        "weight": 6.0,
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    }

    Returns:
    A JSON response indicating the success of the operation.
    """

    data = request.get_json()
    name = data['name']
    type_json = json.dumps(data['type'])  # Serialize list to JSON string
    abilities_json = json.dumps(data['abilities'])  # Serialize list to JSON string
    height = data['height']
    weight = data['weight']
    image = data['image']

    db.catch_pokemon(Pokemon(name, type_json, abilities_json, height, weight, image))
    return jsonify("Pokemon caught successfully")

@app.route('/pokemon', methods=['GET'], strict_slashes=False)
def get_caught_pokemon():
    """
    Retrieves the data of all the caught Pokemon.

    Returns:
        A JSON response containing the data of all the caught Pokemon.
    """
    caught_pokemon = db.get_caught_pokemon()
    caught_pokemon_data = []
    for pokemon in caught_pokemon:
        caught_pokemon_data.append({
            "capture_id": pokemon.capture_id,
            "name": pokemon.name,
            "type": json.loads(pokemon.type),  # Deserialize JSON string to list
            "abilities": json.loads(pokemon.abilities),  # Deserialize JSON string to list
            "height": pokemon.height,
            "weight": pokemon.weight,
            "image": pokemon.image
        })
    return jsonify(caught_pokemon_data)

@app.route('/pokemon/release/<int:capture_id>', methods=['DELETE'], strict_slashes=False)
def release_pokemon(capture_id):
    """
    Releases a caught Pokemon from the database.

    Args:
        capture_id (int): The ID of the Pokemon to be released.

    Returns:
        str: A message indicating the success of the operation.
    """
    db.release_pokemon(capture_id)
    return "Pokemon released successfully"

if __name__ == '__main__':
    app.run(port=5000)
