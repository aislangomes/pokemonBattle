from pokedex import pokedex
import os
import random
# Selecionar o pokemon


def pokemonSelection():
    while True:
        for pokemon in pokedex:
            print(f'{pokemon}. {pokedex[pokemon].name}')

        try:
            pokemonNumber = int(input('\n'))
            print("\nVoce escolheu " + pokedex[pokemonNumber].name)
            myPokemon = pokedex[pokemonNumber]
            break
        except:
            os.system('clear')
            print("Selecione um Pokemon valido\n")

    return myPokemon


def enemyPokemonSelection():
    enemyPokemon = pokedex[random.randrange(1, len(pokedex) + 1)]
    print("O seu oponente será " + enemyPokemon.name)
    return enemyPokemon
