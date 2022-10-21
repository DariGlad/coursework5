from os import path


parent_dir = path.dirname(path.abspath(__file__))

# Путь к json данным экипировки
EQUIPMENT_DATA = path.join(parent_dir, "data", "equipment.json")

# print(parent_dir, EQUIPMENT_DATA, sep="\n")


