"""
units.py - Defines basic unit types.
"""

class Unit:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

class Infantry(Unit):
    def __init__(self):
        super().__init__("Infantry", 100, 10, 5)

class Tank(Unit):
    def __init__(self):
        super().__init__("Tank", 200, 30, 15)
