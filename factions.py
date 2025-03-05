"""
factions.py - Defines different factions in Carbon Conflict.
"""

class Faction:
    def __init__(self, name, color):
        self.name = name
        self.color = color

factions = {
    "Green Order": Faction("Green Order", (34, 177, 76)),
    "Last Coalition": Faction("Last Coalition", (200, 0, 0)),
    "Aqua Pact": Faction("Aqua Pact", (0, 162, 232))
}
