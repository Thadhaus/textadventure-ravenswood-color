# https://www.helloworld.cc - Heft 1 - Seite 52
# Scary cave game -- Original Version CC BY-NC-SA 3.0
# Diese modifizierte Version (C) 2022 Roland Härter r.haerter@wut.de

# mit Farbe wird es bunter - siehe https://pypi.org/project/colorama/
import colorama
#from colorama import Fore, Back, Style
Fore = colorama.Fore
Style = colorama.Style
colorama.init(autoreset=True)

# Mit Zufall wird es spannender
import time, random

random.seed(time.time())

# So funktioniert das Spiel: Alle Räume sind in Richtungs-Dictionaries.
# Diese Dictionaries 'north', 'south',... enthalten Schlüssel-Wert-Paare.
# Schlüssel ist der aktuelle Raum, Wert der Zielraum, in den ich gelange.
# Ein Wert 'None' bedeutet, das ich in dieser Richtung nirgendwo hin komme.
# Mit den 'go'-Kommandos im compass kann ich durch die Räume laufen
# Alle Befehlswörter müssen auch in allowed_commands stehen.
north = {
    'R0': None,
    'R1': None,
    'R2': 'R0',
    'R3': 'R1',
    'R4': None,
    'R5': None,
    'R6': 'R7',
    'R7': None,
    'R8': None,
    'R9': None,
    'R10': 'R9',
    'R11': 'R16',
    'R12': 'R11',
    'R13': None,
    'R14': None,
    'R15': 'R14',
    'R16': 'R10',
    'R17': None,
    'R18': None,
    'R19': None,
    'R20': 'R22',
    'R21': 'R12',
    'R22': 'R7'
}
south = {
    'R0': 'R2',
    'R1': 'R3',
    'R2': None,
    'R3': 'R9',
    'R4': None,
    'R5': None,
    'R6': None,
    'R7': 'R8',
    'R8': None,
    'R9': 'R10',
    'R10': 'R16',
    'R11': 'R12',
    'R12': 'R21',
    'R13': None,
    'R14': 'R15',
    'R15': None,
    'R16': 'R11',
    'R17': None,
    'R18': None,
    'R19': None,
    'R20': None,
    'R21': None
}
east = {
    'R0': 'R1',
    'R1': None,
    'R2': None,
    'R3': None,
    'R4': 'R5',
    'R5': None,
    'R6': None,
    'R7': None,
    'R8': None,
    'R9': None,
    'R10': None,
    'R11': None,
    'R12': None,
    'R13': 'R16',
    'R14': None,
    'R15': 'R17',
    'R16': 'R15',
    'R17': 'R18',
    'R18': 'R19',
    'R19': None,
    'R20': None,
    'R21': None,
    'R22': None
}
west = {
    'R0': 'R4',
    'R1': 'R0',
    'R2': None,
    'R3': None,
    'R4': None,
    'R5': None,
    'R6': None,
    'R7': None,
    'R8': None,
    'R9': None,
    'R10': None,
    'R11': None,
    'R12': None,
    'R13': None,
    'R14': 'R13',
    'R15': 'R16',
    'R16': 'R13',
    'R17': 'R15',
    'R18': 'R17',
    'R19': 'R18',
    'R20': None,
    'R21': None,
    'R22': None
}
downward = {
    'R0': None,
    'R1': None,
    'R2': None,
    'R3': None,
    'R4': None,
    'R5': 'R6',
    'R6': None,
    'R7': None,
    'R8': None,
    'R9': None,
    'R10': None,
    'R11': None,
    'R12': None,
    'R13': None,
    'R14': None,
    'R15': None,
    'R16': None,
    'R17': None,
    'R18': None,
    'R19': 'R20',
    'R20': None,
    'R21': None,
    'R22': None
}
upstairs = {
    'R0': None,
    'R1': None,
    'R2': None,
    'R3': None,
    'R4': None,
    'R5': None,
    'R6': None,
    'R7': None,
    'R8': 'R2',
    'R9': None,
    'R10': None,
    'R11': None,
    'R12': None,
    'R13': None,
    'R14': None,
    'R15': None,
    'R16': None,
    'R17': None,
    'R18': None,
    'R19': None,
    'R20': None,
    'R21': None,
    'R22': None
}
# 'compass' bildet die Richtungs-Befehle auf die Richtungs-Dictionaries ab
compass = {
    'go north': north,
    'w': north,
    'go south': south,
    's': south,
    'go east': east,
    'd': east,
    'go west': west,
    'a': west,
    'go up': upstairs,
    'up': upstairs,
    'go down': downward,
    'dn': downward
}
# Alle Befehlswörter des Spiels müssen in 'allowed_commands' stehen
allowed_commands = [
    'go north', 'go south', 'go east', 'go west', 'go up', 'go down', 'help',
    'quit', 'map', 'w', 'a', 's', 'd', 'up', 'dn'
]

# Jeder Raum hat eine Beschreibung. Die Beschreibung macht viel vom Spiel aus.
description = {
    'R0': 'You are in the kitchen. Seems to be abandonned.',
    'R1': 'You are in the living room. An old armor stands in one corner.',
    'R2': 'You are in a pantry. It is cold in here.',
    'R3': 'Hallway. Here is the exit from this house.',
    'R4': 'The beautiful garden with an apple tree.',
    'R5': 'A small cottage in the garden.',
    'R6': 'The cellar below the cottage.',
    'R7': 'A tunnel with low ceiling.',
    'R8': 'A cellar with shelves full of old onions.',
    'R9': 'A square in front of the house strewn with gravel.',
    'R10': 'A path strewn with gravel in front of the house.',
    'R11': 'A path strewn with gravel in front of the house.',
    'R12': 'A path strewn with gravel towards the road.',
    'R13': 'A gravel strewn path through the park.',
    'R14': 'A gravel strewn path through the park.',
    'R15': 'A gravel strewn path through the park.',
    'R16': 'A crossing of four paths in the park.',
    'R17': 'A small summer house with a blue door.',
    'R18': 'The kitchen living in the summer house.',
    'R19': 'The storage room in the summer house.',
    'R20': 'You crawl through a floor hatch under the carpet in a long tunnel.',
    'R21': 'The gates are closed and locked.',
    'R22': 'A winding narrow passage carved into the rough stone.'
}

# to play different sound indoor and outdoor
indoor_rooms = [
    'R0',
    'R1',
    'R2',
    'R3',
    'R5',
    'R6',
    'R7',
    'R8',
    'R17',
    'R18',
    'R19',
    'R20',
    'R22'
]

indoor_sounds = [
    'It crunches and scratches in the wall.',
    'It trips like rats under the floorboards.',
    'You hear a dripping water tap.',
    'You feel an opressive silence in the house.',
    'There is a whispering murmur around you.',
]

outdoor_sounds = [
    "The birds are singing loudly.", 
    "A dog is barking in the distance."
]


def random_sounds(room):
    zufall = random.randint(0, 100)
    if zufall < 11:
        if room in indoor_rooms:
            text = indoor_sounds[random.choice(indoor_sounds)]
        else:
            text = outdoor_sounds[random.choice(outdoor_sounds)]
        print(text)


def hilfe():
    print(Fore.CYAN + '\nYou may use the following commands:')
    for befehl in allowed_commands:
        if befehl == 'tp' or befehl == 'jump':
            pass
        else:
            print(Fore.BLUE + Style.BRIGHT + f"'{befehl}' ", end='')
    print('\n')

# Hier wird Start und Ziel festgelegt
current_room = 'R0'
final_room = 'R99'  # no final room so far ...
# Begrüßung
print(Fore.MAGENTA + '	*** Welcome to Ravenswood Manor ***')
hilfe()
# Ab hier folgt der Code, um im Spiel zu agieren
command = ''
# Das Spiel läuft in einer Endlos-Schleife
while (current_room is not None):
    # Die Beschreibung des aktuellen Raums ausgeben
    print(Fore.YELLOW + description[current_room])
    random_sounds(current_room)
    # Den Spieler nach seinem nächsten Kommando fragen
    command = input(Fore.GREEN + 'What do you want to do? ' +
                    Fore.RESET).lower()
    # Alle unbekannten Eingaben ignorieren
    while command not in allowed_commands:
        command = input(Fore.RED + 'No such command. ' + Fore.GREEN +
                        'What do you want to do? ' + Fore.RESET).lower()
    # alle Nicht-Richtungen müssen zuerst abgefangen werden
    if command == 'help':
        hilfe()
    elif command == 'quit':
        current_room = None  # Ohne Schmuck und ohne Sicherheitsfrage
    elif command == 'map':
        import sys
        import generiere_karte as map
        map.hauptprogramm(sys.argv[0])  # der Name dieses Skripts als Parameter
    # Gibt es einen Weg in die gefragte Richtung?
    elif compass[command][current_room] is not None:
        # Wenn es einen Weg gibt, gehe dorthin
        current_room = compass[command][current_room]
        # Wurde das Spielziel erreicht?
        if current_room == final_room:
            print(Fore.YELLOW + description[current_room])
            print(Fore.MAGENTA + 'You found the final room. Game Over.' +
                  Fore.RESET)
            current_room = None  # Die Abbruch-Bedingung für die Endlos-Schleife setzen
    else:
        print(Fore.RED + 'There is no path in that direction. ', end='')
