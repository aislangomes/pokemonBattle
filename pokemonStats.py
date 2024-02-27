from pokedex import pokedex


def pokemonStats(pokemon):
    for key, value in vars(pokemon).items():
        print(key + ":", value)
    print("\n")
