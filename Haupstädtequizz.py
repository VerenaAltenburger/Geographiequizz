import random

def welcome_gamer():
    print("Willkommen zum Hauptstädtequizz - Errate die Hauptstädte der jeweiligen Länder!")

def couple_pays_capitale(content):
    return content[random.randint(1,len(content)-1)].split(",")

def question(content):
    pays_capitale = couple_pays_capitale(content)
    essay = 0
    while True:
        reponse = input(f"Was ist die Hauptstadt von {pays_capitale[0]}? ")
        if reponse.lower() == pays_capitale[1].lower():
            print("Richtig!")
            return
        else:
            essay += 1
            if essay == 3:
                print(f"Nein, die richtige Antwort ist: {pays_capitale[1]}")
                return
            print("Falsch! Probier' es noch einmal. ")



welcome_gamer()
with open("hauptstädte.csv", "r", encoding="utf-8") as hauptstädte_file:
    content = hauptstädte_file.read().splitlines()
    while True:
        question(content)
