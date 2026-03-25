import os
import re

# Ustawienia
folder = "history/states"
Minimum_manpower = 10000

pattern = re.compile(r"^\s*manpower\s*=\s*(\d+)", re.MULTILINE)

print("------------------ HOI4 ----------------")
print("Narzędzie do zmieniania populacji świata\n")
print("Wybierz: ")
print("0 - Zmniejszanie")
print("1 - Zwiększanie\n")
Tryb = input(">")
Procent = int(input("\nProcent (np. 50% - 50) : "))/100
if Tryb=="1":
    Procent+=1
else:
    Procent = 1-Procent

scale = Procent
print(f"Skala: {scale}\n")
total_old = 0
small = 0

for file in os.listdir(folder):
    path = os.path.join(folder, file)

    if not file.endswith(".txt"):
        continue

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    def repl(match):
        global total_old, small
        value = int(match.group(1))
        if value < Minimum_manpower:
            small += 1
        total_old += value
        return f"\tmanpower = {value}"

    text = re.sub(pattern, repl, text)

print(f"Stany poniżej {Minimum_manpower}: {small}")
print(f"Manpower przed: {total_old}")
print(f"Manpower po (szacowane): ~{int(total_old*scale)}")

# Funkcja
def Zmienianie():
    total_new = 0
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if not file.endswith(".txt"):
            continue

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        def repl(match):
            global total_new
            value = int(match.group(1))
            new = int(value * scale)
            if new < Minimum_manpower:
                new = Minimum_manpower
            total_new += new
            return f"manpower = {new}"

        text = re.sub(pattern, repl, text)

        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    print(f"nowy manpower: {total_new}")

if input("kontynuować? [Y/n]") == "Y":
    Zmienianie()

exit(0)