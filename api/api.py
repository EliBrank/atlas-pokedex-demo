import json
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from repositories.pokemon_repository import PokemonRepository
from db.pokemon_db import PokemonDB
from models.pokemon import Pokemon

app = Flask(__name__, static_folder="../www", template_folder="../www")
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": "*"}})

db = PokemonDB()
repo = PokemonRepository()

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

@app.route('/pokemon/search/<name>', methods=['GET'], strict_slashes=False)
def search_pokemon(name):
    """
    Searches for a Pokemon by name.

    Args:
        name (str): The name of the Pokemon to search for.

    Returns:
        Pokemon: The Pokemon object if found, otherwise None.
    """
    my_pokemon = repo.get_pokemon(name)
    return jsonify({
        "capture_id": my_pokemon.capture_id,
        "name": my_pokemon.name,
        "type": my_pokemon.type,  # Deserialize JSON string to list
        "abilities": my_pokemon.abilities,  # Deserialize JSON string to list
        "height": my_pokemon.height,
        "weight": my_pokemon.weight,
        "image": my_pokemon.image
    })

@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
