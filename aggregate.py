"""
["0001"]: {
    "attributes": [
        {
            "trait_type": "Face",
            "value": "",
        },
        {
            "trait_type": "Hair",
            "value": "",
        },
        {
            "trait_type": "Shirt",
            "value": "",
        },
        {
            "trait_type": "Accessory",
            "value": "",
        },
        {
            "trait_type": "Background",
            "value": "",
        },
    ]
    "description": "#1 of 9999",
    "external_url": "https://heroku/1"
    "image": "https://storage.googleapis.com/gwei-faces/gweiFace%20%230001.png",
    "name": "gweiFace #0001"
}

"""
import csv
import json

aggregated = {}

# Renaming
backgrounds = {
    "outer-space": "Outer Space",
    "wings": "Wings",
    "sun-and-moon": "Sun and Moon",
    "triangles": "Triangles",
    "tiles": "Tiles",
    "snowed-in": "Snowed In",
    "coral": "Coral Reef",
    "squares": "Squares",
    "circles": "Circles",
    "gwei-face": "gweiFace",
}

faces = {
    "demon": "Demon",
    "skelly": "Skelly",
    "alien": "Alien",
    "zombo": "Zombo",
    "hooman-1": "Hooman 1",
    "hooman-2": "Hooman 2",
    "hooman-3": "Hooman 3",
    "robo-san": "Robo-San"
}

hairs = {
    "none": "None",
    "short": "Short",
    "long": "Long",
    "mohawk": "Mohawk",
    "beard": "Beard",
    "afro": "Afro",
    "stache": "Stache",
    "clown": "Clown"
}

accessories = {
    "mask": "Mask",
    "halo": "Halo",
    "sombrero": "Sombrero",
    "viking": "Viking",
    "none": "None",
    "unihorn": "Unihorn",
    "headband": "Headband",
    "crown": "Crown",
    "necklace": "Necklace"
}

shirts = {
    "suit": "Suit",
    "tanktop": "Tank Top",
    "chainmail": "Chain Mail",
    "suspenders": "Suspenders",
    "jacket": "Jacket",
    "yellow-tee": "Yellow",
    "pink-tee": "Pink",
    "red-tee": "Red",
    "orange-tee": "Orange",
    "green-tee": "Green",
    "blue-tee": "Blue",
    "purple-tee": "Purple"
}

with open("../samples.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    start = False
    for i in csv_reader:
        if not start:
            start = True
            continue
        pos = i[0].split(" ")[1]
        num = int(pos[1:])
        aggregated[str(num)] = {
            "name": i[0],
            # "description": "#{num} of 9999".format(num=str(num)),
            "external_url": "https://gweiface.com/{num}".format(num=str(num)),
            "image": "https://storage.googleapis.com/gwei-faces/gweiFace%20%23{pos}.png".format(pos=pos[1:]),
            "attributes": [
                {
                    "trait_type": "Face",
                    "value": faces[i[2]]
                },
                {
                    "trait_type": "Hair",
                    "value": hairs[i[4]]
                },
                {
                    "trait_type": "Shirt",
                    "value": shirts[i[3]]
                },
                {
                    "trait_type": "Accessory",
                    "value": accessories[i[5]]
                },
                {
                    "trait_type": "Background",
                    "value": backgrounds[i[1]]
                },
                {
                    "display_type": "number",
                    "trait_type": "Token ID",
                    "value": num
                }
            ],
        }

with open("../aggregate.json", "w") as file:
    json.dump(aggregated, file)
