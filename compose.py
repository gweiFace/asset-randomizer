from PIL import Image
from tqdm import trange
import random
import csv

# limit definitions
defs = {
    "Accessories": {
        "crown": {
            "path": "", "amt": 900, "encoding": "1"
        },
        "halo": {
            "path": "", "amt": 1300, "encoding": "2"
        },
        "headband": {
            "path": "", "amt": 1100, "encoding": "3"
        },
        "mask": {
            "path": "", "amt": 1200, "encoding": "4"
        },
        "necklace": {
            "path": "", "amt": 1000, "encoding": "5"
        },
        "sombrero": {
            "path": "", "amt": 950, "encoding": "6"
        },
        "unihorn": {
            "path": "", "amt": 499, "encoding": "7"
        },
        "viking": {
            "path": "", "amt": 950, "encoding": "8"
        },
        "none": {
            "path": "", "amt": 2100, "encoding": "9"
        }
    },
    "Hairs": {
        "mohawk": {
            "path": "", "amt": 900, "encoding": "1"
        },
        "long": {
            "path": "", "amt": 1400, "encoding": "2"
        },
        "afro": {
            "path": "", "amt": 1000, "encoding": "3"
        },
        "none": {
            "path": "", "amt": 2500, "encoding": "4"
        },
        "short": {
            "path": "", "amt": 1800, "encoding": "5"
        },
        "beard": {
            "path": "", "amt": 1000, "encoding": "6"
        },
        "stache": {
            "path": "", "amt": 800, "encoding": "7"
        },
        "clown": {
            "path": "", "amt": 599, "encoding": "8"
        },
    },
    "Shirts": {
        "suit": {
            "path": "", "amt": 499, "encoding": "1"
        },
        "tanktop": {
            "path": "", "amt": 800, "encoding": "2"
        },
        "chainmail": {
            "path": "", "amt": 700, "encoding": "3"
        },
        "suspenders": {
            "path": "", "amt": 600, "encoding": "4"
        },
        "jacket": {
            "path": "", "amt": 575, "encoding": "5"
        },
        "yellow-tee": {
            "path": "", "amt": 975, "encoding": "6"
        },
        "pink-tee": {
            "path": "", "amt": 975, "encoding": "7"
        },
        "red-tee": {
            "path": "", "amt": 975, "encoding": "8"
        },
        "orange-tee": {
            "path": "", "amt": 975, "encoding": "9"
        },
        "green-tee": {
            "path": "", "amt": 975, "encoding": "10"
        },
        "blue-tee": {
            "path": "", "amt": 975, "encoding": "11"
        },
        "purple-tee": {
            "path": "", "amt": 975, "encoding": "12"
        },
    },
    "Backgrounds": {
        "triangles": {
            "path": "", "amt": 1500, "encoding": "1"
        },
        "squares": {
            "path": "", "amt": 1500, "encoding": "2"
        },
        "circles": {
            "path": "", "amt": 1500, "encoding": "3"
        },
        "wings": {
            "path": "", "amt": 900, "encoding": "4"
        },
        "outer-space": {
            "path": "", "amt": 800, "encoding": "5"
        },
        "gwei-face": {
            "path": "", "amt": 499, "encoding": "6"
        },
        "sun-and-moon": {
            "path": "", "amt": 750, "encoding": "7"
        },
        "tiles": {
            "path": "", "amt": 900, "encoding": "8"
        },
        "coral": {
            "path": "", "amt": 750, "encoding": "9"
        },
        "snowed-in": {
            "path": "", "amt": 900, "encoding": "10"
        },
    },
    "Faces": {
        "demon": {
            "path": "", "amt": 698, "encoding": "1"
        },
        "alien": {
            "path": "", "amt": 798, "encoding": "2"
        },
        "zombo": {
            "path": "", "amt": 1198, "encoding": "3"
        },
        "skelly": {
            "path": "", "amt": 1298, "encoding": "4"
        },
        "hooman-1": {
            "path": "", "amt": 1999, "encoding": "5"
        },
        "hooman-2": {
            "path": "", "amt": 1999, "encoding": "6"
        },
        "hooman-3": {
            "path": "", "amt": 1999, "encoding": "7"
        },
        # "robo-san": {
        #    "path": "", "amt": 10, "encoding": "8"
        # },
    }
}

# path loader
for i in defs:
    for j in defs[i]:
        if i == "Hairs" and j == "long":
            defs[i][j]["path"] = ["artHandler/Pixels/Hairs/long2.png",
                                  "artHandler/Pixels/Hairs/long1.png"]
            continue
        if j != "none":
            defs[i][j]["path"] = "artHandler/Pixels/{category}/{item}.png".format(
                category=i, item=j)
            # bg = Image.open(defs[i][j]["path"])  # test path existance

# main
fields = ["Background", "Face", "Shirt", "Hair", "Accessories"]
combos = []

comp = []  # {file, combo}

for i in trange(9989, desc="Randomizing"):
    # count = "gweiFace #" + str(i + 1).zfill(4)
    combo = ""
    comborow = []

    while combo == "" or combo in combos:
        comborow = []
        background = random.choice(list(defs["Backgrounds"].values()))
        while background["amt"] == 0:
            background = random.choice(list(defs["Backgrounds"].values()))

        combo += background["encoding"]
        for j in defs["Backgrounds"]:
            if defs["Backgrounds"][j]["encoding"] == background["encoding"]:
                comborow.append(j)
                break

        face = random.choice(list(defs["Faces"].values()))
        while face["amt"] == 0:
            face = random.choice(list(defs["Faces"].values()))

        combo += face["encoding"]
        for j in defs["Faces"]:
            if defs["Faces"][j]["encoding"] == face["encoding"]:
                comborow.append(j)
                break

        shirt = random.choice(list(defs["Shirts"].values()))
        while shirt["amt"] == 0:
            shirt = random.choice(list(defs["Shirts"].values()))

        combo += shirt["encoding"]
        for j in defs["Shirts"]:
            if defs["Shirts"][j]["encoding"] == shirt["encoding"]:
                comborow.append(j)
                break

        if face["encoding"] != "1" and face["encoding"] != "2":
            hair = random.choice(list(defs["Hairs"].values()))
            while hair["amt"] == 0 or (hair["encoding"] == "5" and face["encoding"] == "3"):
                hair = random.choice(list(defs["Hairs"].values()))
        else:
            hair = defs["Hairs"]["none"]

        combo += hair["encoding"]
        for j in defs["Hairs"]:
            if defs["Hairs"][j]["encoding"] == hair["encoding"]:
                comborow.append(j)
                break

        accessory = random.choice(list(defs["Accessories"].values()))
        while accessory["amt"] == 0 or (face["encoding"] == "2" and accessory["encoding"] == "3") or ((hair["encoding"] == "1" or hair["encoding"] == "3") and (accessory["encoding"] == "2" or accessory["encoding"] == "6" or accessory["encoding"] == "7" or accessory["encoding"] == "8")):
            accessory = random.choice(list(defs["Accessories"].values()))

        combo += accessory["encoding"]
        for j in defs["Accessories"]:
            if defs["Accessories"][j]["encoding"] == accessory["encoding"]:
                comborow.append(j)
                break

    background["amt"] -= 1
    face["amt"] -= 1
    shirt["amt"] -= 1
    hair["amt"] -= 1
    accessory["amt"] -= 1

    combos.append(combo)
    # csvwriter.writerow(comborow)

    background = Image.open(background["path"])
    face = Image.open(face["path"])
    shirt = Image.open(shirt["path"])

    if isinstance(hair["path"], list):
        tempHair = Image.open(hair["path"][0])
        background.paste(tempHair, (0, 0), tempHair)

    background.paste(face, (0, 0), face)
    background.paste(shirt, (0, 0), shirt)

    if accessory["encoding"] == "3":
        tempAccessory = Image.open(accessory["path"])
        background.paste(tempAccessory, (0, 0), tempAccessory)

    if hair["encoding"] != "4":
        if isinstance(hair["path"], list):
            hair = Image.open(hair["path"][1])
        else:
            hair = Image.open(hair["path"])
        background.paste(hair, (0, 0), hair)

    if accessory["encoding"] != "3" and accessory["encoding"] != "9":
        accessory = Image.open(accessory["path"])
        background.paste(accessory, (0, 0), accessory)

    comp.append([background, comborow])

random.shuffle(comp)
with open("samples.csv",  'w', newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for i in trange(len(comp), desc="Saving"):
        count = "gweiFace #" + str(i + 1).zfill(4)
        comp[i][1].insert(0, count)
        csvwriter.writerow(comp[i][1])
        comp[i][0].save("artHandler/Composed/{count}.png".format(count=count))

        # background.save("artHandler/Composed/{count}.png".format(count=count))
"""
background = Image.open(
    "artHandler/Pixels/Backgrounds/sun-moon.png").convert("RGBA")
character = Image.open(
    "artHandler/Pixels/Characters/demon.png").convert("RGBA")
shirt = Image.open(
    "artHandler/Pixels/Shirts/suit.png").convert("RGBA")
hair = Image.open(
    "artHandler/Pixels/Hairs/stache.png").convert("RGBA")
accessory = Image.open(
    "artHandler/Pixels/Accessories/crown.png").convert("RGBA")

background.paste(character, (0, 0), character)
background.paste(shirt, (0, 0), shirt)
background.paste(hair, (0, 0), hair)
background.paste(accessory, (0, 0), accessory)
background.show()
"""
