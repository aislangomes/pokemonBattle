from typeAdvantages import advantages
import random


class Pokemon:
    def __init__(self, name, type, life, attack, defense, energy, level):
        self.name = name
        self.type = type
        self.maxLife = (life * 10) + level
        self.currentLife = self.maxLife
        self.attack = attack + level
        self.defense = defense + level
        self.energy = energy + level
        self.level = level

    def calcularAtaque(self, enemy):
        self.energy -= 3
        hasVantage = enemy.type in advantages[self.type]

        criticalType = 1
        criticalLife = 1
        criticalChance = 1

        if random.random() <= 0.2:
            criticalChance = 2
        if hasVantage:
            criticalType = 2
        if self.currentLife < self.maxLife * 0.1 and random.random() <= 0.75:
            criticalLife = 2

        criticalPower = criticalType * criticalLife * criticalChance
        atkPower = (self.attack + criticalPower) - enemy.defense

        if atkPower < 1:
            atkPower = 1

        return int(atkPower)

    def increaseDefense(self):
        self.energy -= 2
        self.defense *= 2

    def resetDefense(self):
        self.defense = self.defense - self.defense

    def recoverEnergy(self):
        self.energy = self.energy + 2

    def decision(self, enemy):
        myDecision = round(random.random(), 2)
        return myDecision
