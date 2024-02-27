import os


def combat(myPokemon, enemyPokemon):
    myEscape = False
    enemyEscape = False
    enemyDefense = False
    mydoubleDefense = False
    while True:
        os.system('clear')
        while True:
            os.system('clear')
            print(
                f"""
            {myPokemon.name} Level {myPokemon.level}
            Vida: {myPokemon.currentLife} / {myPokemon.maxLife}
            Energia: {myPokemon.energy}
            Defesa: {myPokemon.defense}

            {enemyPokemon.name} Level {enemyPokemon.level}
            Vida: {enemyPokemon.currentLife} / {enemyPokemon.maxLife}
            Energia: {enemyPokemon.energy}
            Defesa: {enemyPokemon.defense}
            """)

            # turno do jogador
            print("""
            Sua vez:
            1. Atacar
            2. Defender
            3. Energia
            4. Fugir\n
            """)

            try:
                action = int(input())
            except:
                os.system('clear')
                print("Ação invalida \n")

            match action:
                case 1:
                    os.system('clear')
                    if myPokemon.energy < 3:
                        print("Sem energia")
                        input()
                        continue
                    atack = myPokemon.calcularAtaque(enemyPokemon)
                    enemyPokemon.currentLife -= atack
                    print(
                        f"""Seu {myPokemon.name} atacou {enemyPokemon.name} adversario\n
                        O dano foi de {atack}\n
                        {enemyPokemon.name}...LVL{enemyPokemon.level}
                        Vida: {enemyPokemon.currentLife} / {enemyPokemon.maxLife}
                        """)
                    input()
                    break
                case 2:
                    os.system('clear')
                    if myPokemon.energy < 3:
                        print("Sem energia")
                        input()
                        continue
                    myPokemon.increaseDefense()
                    print(
                        f"Seu {myPokemon.name} usou defesa (Defesa dobra por 1 turno)")
                    mydoubleDefense = True
                    input()
                    break

                case 3:
                    os.system('clear')
                    myPokemon.recoverEnergy()
                    print(f"Seu {myPokemon.name} recuperou energia")
                    input()
                    break

                case 4:
                    os.system('clear')
                    print("Você fugiu")
                    myEscape = True
                    input()
                    break

        # Checar vida e resetar status adversario
        if enemyDefense:
            enemyPokemon.defense /= 2
            enemyDefense = False
        if enemyPokemon.currentLife <= 0:
            print(f'{enemyPokemon.name} foi derrotado.')
            break
        if myEscape:
            break

        # turno do inimigo
        myDecision = enemyPokemon.decision(myPokemon)
        if enemyPokemon.energy < 3:
            enemyPokemon.recoverEnergy()
            print(f"O {enemyPokemon.name} recuperou enrgia")
            input()
            continue
        if myDecision >= 0.5:
            os.system('clear')
            atack = enemyPokemon.calcularAtaque(myPokemon)
            myPokemon.currentLife -= atack
            print(
                f"""O {enemyPokemon.name} atacou seu {myPokemon.name}\n
                O dano foi de {atack}\n
                {myPokemon.name}...LVL{myPokemon.level}
                Vida: {myPokemon.currentLife} / {myPokemon.maxLife}
                """)
            input()
        elif myDecision >= 0.2:
            enemyPokemon.increaseDefense()
            enemyDefense = True
            print(f"O {enemyPokemon.name} usou defesa (Defesa dobra por 1 turno)")
            input()
        elif myDecision >= 0.01:
            enemyPokemon.recoverEnergy()
            print(f"O {enemyPokemon.name} recuperou enrgia")
            input()
        else:
            enemyPokemon.currentLife = 0
            print(f"{enemyPokemon.name} fugiu da batalha")
            enemyEscape = True
            input()
            break

        # Checar vida e resetar status do jogador
        if mydoubleDefense:
            myPokemon.defense /= 2
            mydoubleDefense = False
        if myPokemon.currentLife <= 0:
            print(f'Seu {myPokemon.name} foi derrotado.')
            break
        if enemyEscape:
            break
