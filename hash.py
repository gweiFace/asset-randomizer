from PIL import Image
from tqdm import trange
from random import randrange
import os

SIZE = 9989
WIDTH, HEIGHT = 1000, 1000


def composite():
    FACTOR = 2.4
    comp_img = Image.new("RGBA", (int(WIDTH*FACTOR), int(HEIGHT*FACTOR)))

    for i in trange(SIZE, desc="Composing"):
        img = Image.open("artHandler/Composed/gweiFace #" +
                         str(i + 1).zfill(4) + ".png")
        curr = img.resize((int(10*FACTOR), int(10*FACTOR)), Image.ANTIALIAS)
        comp_img.paste(curr, (int((i % (WIDTH // 10)) * 10 * FACTOR),
                              int((i // (WIDTH // 10)) * 10 * FACTOR)))

    comp_img.show()
    comp_img.save("artHandler/composite.png")


def hash():
    pass


def compose_banner():
    comp_img = Image.new("RGBA", (1500, 500))
    DIM = 100
    #rands = []
    for i in trange(150, desc="Composing"):
        #rando = randrange(9990)
        # while rando in rands:
        #    rando = randrangE(9990)
        # rands.append(rando)

        img = Image.open("artHandler/Composed/gweiFace #" +
                         str(i + 1).zfill(4) + ".png")

        curr = img.resize((DIM, DIM), Image.ANTIALIAS)
        comp_img.paste(curr, ((i % (1500 // DIM) * DIM),
                              (i // (1500 // DIM) * DIM)))

    comp_img.show()
    comp_img.save("artHandler/compositeBanner.png")


# composite()
compose_banner()
