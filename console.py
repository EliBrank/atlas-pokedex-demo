#!/usr/bin/python3
import cmd
from models.pokemon import Pokemon
from repositories.pokemon_repository import PokemonRepository
from repositories.caught_pokemon_repository import CaughtPokemonRepository



class PokemonConsole(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.pokemon_repository = PokemonRepository()
        self.caught_pokemon_repository = CaughtPokemonRepository()

    prompt = 'pokemon> '
    intro = 'Welcome to the Pokemon console! Type help or ? to list commands.\n'

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_exit(self, arg):
        """Exit command to exit the program"""
        return True

    def emptyline(self):
        """ overwriting the emptyline method """
        return False

    def do_clear(self, arg):
        """Clear the screen"""
        print("\033c", end="")

    def do_search(self, arg):
        """Search for a Pokemon by name"""
        ars = arg.split()
        if len(ars) == 0:
            print("Please provide a Pokemon name.")
            return
        pokemon_name = ars[0]
        pokemon = self.pokemon_repository.get_pokemon(pokemon_name)
        print(pokemon)

    def do_catch(self, arg):
        """Catch a Pokemon"""
        ars = arg.split()
        if len(ars) == 0:
            print("Please provide a Pokemon name.")
            return
        pokemon_name = ars[0]
        pokemon = self.pokemon_repository.get_pokemon(pokemon_name)
        if pokemon is None:
            print(f"Pokemon {pokemon_name} not found.")
            return
        caught = self.caught_pokemon_repository.catch_pokemon(pokemon)
        if caught:
            print(f"Pokemon {pokemon_name} caught successfully.")
        else:
            print(f"Failed to catch Pokemon {pokemon_name}")

    def do_caught(self, arg):
        """List all caught Pokemon"""
        caught_pokemon = self.caught_pokemon_repository.get_caught_pokemon()
        for pokemon in caught_pokemon:
            print(pokemon)

    def do_release(self, arg):
        """Release a caught Pokemon"""
        ars = arg.split()
        if len(ars) == 0:
            print("Please provide a Pokemon ID.")
            return
        capture_id = int(ars[0])
        released = self.caught_pokemon_repository.release_pokemon(capture_id)
        if released:
            print(f"Pokemon with id of {capture_id} was released successfully.")
        else:
            print(f"Failed to release Pokemon id number {capture_id}")

if __name__ == '__main__':
    PokemonConsole().cmdloop()
