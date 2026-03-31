import os
import re

root = "common"
country_tags = os.path.join(root, "country_tags/02_countries.txt")
if (not os.path.exists(country_tags)):
    print(f"Nie ma ścieżki: {country_tags}")
    exit(0)

print("przykład: ABC = \"countries/Moskwa.txt\" na KOB = \"countries/Kobylniki.txt\"")
old_tag = input("Podaj stary TAG (ABC): ")
new_tag = input("Podaj nowy TAG (KOB): ")
old_file = input("Podaj starą nazwe pliku (Moskwa.txt): ")
new_file = input("Podaj nową nazwe pliku (Kobylniki.txt): ")
print("\n")


# common/country_tags
pattern = pattern = re.compile(rf"^(\s*){old_tag}(\s*=\s*)\"countries/{old_file}\"", re.MULTILINE | re.IGNORECASE)
with open(country_tags, "r", encoding="utf-8") as f:
    text = f.read()
    
text = pattern.sub(r'\1' + new_tag + r'\2"countries/' + new_file + r'"', text)

with open(country_tags, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: common/country_tags")


# common/countries
countries = os.path.join(root, f"countries/{old_file}")
new_countries = os.path.join(root, f"countries/{new_file}")
if not os.path.exists(countries):
    print(f"Nie ma ścieżki: {countries}")
    exit(0)

os.rename(countries, new_countries)
print("Zakończono: common/countries")


# common/ideas
ideas = os.path.join(root, f"ideas/{old_file}")
new_ideas = os.path.join(root, f"ideas/{new_file}")
if not os.path.exists(ideas):
    print(f"Nie ma ścieżki: {ideas}")
    exit(0)

os.rename(ideas, new_ideas)
print("Zakończono: common/ideas")


# common/characters
characters = os.path.join(root, f"characters/{old_tag}.txt")
new_characters = os.path.join(root, f"characters/{new_tag}.txt")
if not os.path.exists(characters):
    print(f"Nie ma ścieżki: {characters}")
    exit(0)

os.rename(characters, new_characters)
pattern = re.compile(rf"{old_tag}_")
with open(new_characters, "r", encoding="utf-8") as f:
    text = f.read()

text = pattern.sub(f"{new_tag}_", text)

with open(new_characters, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: common/characters")


# common/countries/colors.txt
countries = os.path.join(root, f"countries/colors.txt")
if not os.path.exists(countries):
    print(f"Nie ma ścieżki: {countries}")
    exit(0)

pattern = re.compile(rf"^(\s*){old_tag}(\s*=)", re.MULTILINE)
with open(countries, "r", encoding="utf-8") as f:
    text = f.read()

text = pattern.sub(rf"\1{new_tag}\2", text)

with open(countries, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: common/countries/colors.txt")


# common/names/00_names.txt
names = os.path.join(root, f"names/00_names.txt")
if not os.path.exists(names):
    print(f"Nie ma ścieżki: {names}")
    exit(0)

pattern = re.compile(rf"^(\s*){old_tag}(\s*=)", re.MULTILINE)
with open(names, "r", encoding="utf-8") as f:
    text = f.read()

text = pattern.sub(rf"\1{new_tag}\2", text)

with open(names, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: common/names/00_names.txt")



gfx_folder = "gfx/flags"
folders = [
    gfx_folder, 
    os.path.join(gfx_folder, "small"), 
    os.path.join(gfx_folder, "medium")
]

for folder in folders:
    if not os.path.isdir(folder):
        print(f"Brak folderu: {folder}")
        continue

    for file in os.listdir(folder):
        if file.lower() != f"{old_tag.lower()}.tga":
            continue

        old_path = os.path.join(folder, file)
        new_path = os.path.join(folder, f"{new_tag}.tga")

        os.rename(old_path, new_path)
print("Zakończono: gfx/flags")


# portraits/00_portraits.txt
portraits = "portraits/00_portraits.txt"
if not os.path.exists(portraits):
    print(f"Nie ma ścieżki: {portraits}")
    exit(0)

pattern = re.compile(rf"^(\s*){old_tag}(\s*=)", re.MULTILINE)
with open(portraits, "r", encoding="utf-8") as f:
    text = f.read()

text = pattern.sub(rf"\1{new_tag}\2", text)

with open(portraits, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: portraits/00_portraits.txt")


# portraits/998_scientist_portraits.txt
portraits = "portraits/998_scientist_portraits.txt"
if not os.path.exists(portraits):
    print(f"Nie ma ścieżki: {portraits}")
    exit(0)

pattern = re.compile(rf"^(\s*){old_tag}(\s*=)", re.MULTILINE)
with open(portraits, "r", encoding="utf-8") as f:
    text = f.read()

text = pattern.sub(rf"\1{new_tag}\2", text)

with open(portraits, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: portraits/998_scientist_portraits.txt")



folder = "history/units"
if not os.path.isdir(folder):
    print(f"Brak folderu: {folder}")
else:
    for file in os.listdir(folder):

        if not file.lower().endswith(".txt"):
            continue

        if file.startswith(f"{old_tag}_"):
            new_file2 = file.replace(f"{old_tag}_", f"{new_tag}_", 1)
            old_path = os.path.join(folder, file)
            new_path = os.path.join(folder, new_file2)

            os.rename(old_path, new_path)

            pattern = re.compile(rf"{old_tag}")
            with open(new_path, "r", encoding="utf-8") as f:
                text = f.read()

            text = pattern.sub(new_tag, text)

            with open(new_path, "w", encoding="utf-8") as f:
                f.write(text)
print("Zakończono: history/units")


# history/countries
folder = "history/countries"
history_countries = os.path.join(folder, f"{old_tag} - {old_file}")
new_history_countries = os.path.join(folder, f"{new_tag} - {new_file}")
if not os.path.exists(history_countries):
    print(f"Nie ma ścieżki: {history_countries}")
    exit(0)

os.rename(history_countries, new_history_countries)
pattern = re.compile(rf"{old_tag}_")
with open(new_history_countries, "r", encoding="utf-8") as f:
    text = f.read()

text = pattern.sub(f"{new_tag}_", text)

with open(new_history_countries, "w", encoding="utf-8") as f:
    f.write(text)
print("Zakończono: history/countries")


# localisation/english/countries_l_english.yml
folder = "localisation"
laguages = ["english/countries_l_english.yml", "polish/countries_l_polish.yml"]
for lan in laguages:
    localisation = os.path.join(folder, lan)
    if not os.path.exists(localisation):
        print(f"Nie ma ścieżki: {localisation}")
        exit(0)

    pattern = re.compile(rf"{old_tag}_")
    with open(localisation, "r", encoding="utf-8") as f:
        text = f.read()

    text = pattern.sub(f"{new_tag}_", text)

    with open(localisation, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Zakończono: {localisation}")


# history/states
folder = "history/states"
if not os.path.exists(folder):
    print(f"Nie ma ścieżki: {folder}")
    exit(0)

pattern = re.compile(rf"(?<=\=\s){old_tag}\b")
for state in os.listdir(folder):
    if not file.endswith(".txt"):
        continue

    path = os.path.join(folder, state)

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    text = pattern.sub(new_tag, text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
print(f"Zakończono: {folder}")