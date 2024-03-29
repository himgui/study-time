#!/usr/bin/env python

"""
Print a doc about school activities
"""

__version__ = "0.2.0"

room_one = ["Veiga", "Dudu", "Endrick","Gomez","Ze","Weverton"]
room_two = ["Jhon Jhon","L. Guilherme", "Breno Lopes","Rios"]

english_class = ["Dudu", "Endrick","Gomez", "Jhon Jhon","L. Guilherme"]
music_class = ["Veiga", "Dudu", "Rios"]
dance_class = ["Ze","Weverton" "Jhon Jhon","L. Guilherme","Breno Lopes"]

activities = [
    ("English:",english_class),
    ("Music:",music_class),
    ("Dance:",dance_class)
]

for activitie_name, activitie in activities:

    print("-" * 25)
    
    activitie_class_1 = set(room_one) & set(activitie)
    activitie_class_2 = set(room_two).intersection(activitie)
    
    print(f"{activitie_name} Class 1:",activitie_class_1)
    print(f"{activitie_name} Class 2:",activitie_class_2)
    print()
    print("-" * 25)