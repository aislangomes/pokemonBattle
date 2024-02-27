import os
from selection import pokemonSelection, enemyPokemonSelection
from combat import combat

print("Bem vindo ao Pythonmon")
input("Pressione enter para continuar...")

os.system('clear')
print("Escolha seu pokemon")
myPokemon = pokemonSelection()
input()
os.system('clear')
enemyPokemon = enemyPokemonSelection()
input()
os.system('clear')
combat(myPokemon, enemyPokemon)
