"""
Removes greenscreen from an image.
Usage: python greenscreen_remove.py image.jpg
"""

from PIL import Image
import sys
import os
from os.path import exists

masini = [
    # "bmwe38", 
    # "m3e46", 
    # "bmwm6", 
    # "bmwm4",
    # "f10m5",
    # "rmodx6",
    # "bmwi8",
    # "m2g87",
    # "22m5",
    # "745le",
    # "bmwg07",
    # "17m760i",
    # "bmw8mm",
    # "m4f82",
    # "e92dy",
    # "m330i21",
    # "X6M2022",
    # "m422",
    # "km1000rr",
    # "22m4bb",
    # "g700brabusretuned",
    # "g650",
    # "rmodgt63",
    # "s600w220",
    # "AMGCE",
    # "cls",
    # "gxg63",
    # "gle21",
    # "s500",
    # "dacia1310",
    # "logan",
    # "sandero",
    # "sanderos2",
    # "daduster",
    # "prius",
    # "xp210",
    # "a80",
    # "tsgr2",
    # "307cc",
    # "seatleon",
    # "smart",
    # "ren_clio_5",
    # "mr53",
    # "skodaoctavia",
    # "vwtoua19cf",
    # "zc31s",
    # "miata",
    # "RS3",
    # "RS5",
    # "evoque",
    # "rmodrs6",
    # "aaq4",
    # "21sierra",
    # "czr2",
    # "Q7",
    # "h3",
    # "GhibliS",
    # "kiastinger",
    # "camaro",
    # "xc90",
    # "2022kiak5gt",
    # "a6",
    # "ram22trx",
    # "a8l",
    # "escalade21",
    # "sq72016",
    # "22caygt",
    # "r820",
    # "tr22",
    # "teslax",
    # "c8p1",
    # "ferporto",
    # "lhuracant",
    # "gcm992gt3",
    # "rmodbentleygt",
    # "lp700",
    # "ferrari812",
    # "wraith",
    # "urus2",
    # "P1",
    # "sf90s",
    # "maj350z",
    # "r33ptnc",
    # "evo9mr",
    # "bnr34",
    # "22b",
    # "nis13",
    "nismo20",
    "rmodmustang",
    "africat",
    "wrangler22",
    "mlnovitec",
    "RS7C8",
    "nh2r",
    "BENTAYGAM",
    "hevo",
    "765lt",
    "bugsupers",
    "panigale",
    "foxharley1",
    "foxharley2",
    "r6",
    "fcr",
    "bros60",
    "gsxr1000",
    "goldwing",
    "19ranger",
    "ambulance",
    "nswsorento",
    "mansoryescalade",
    "motor2pol",
    "polopolitie",
    "skodabreckpolitie",
    "ACTRPavant",
    "21rav4",
    "xc60",
    "23ramtrx",
    "508bana",
    "ACTGDiload",
    "audia4police",
    "SMALLBOAT"]

def rgb_to_hsv(r, g, b):
    maxc = max(r, g, b)
    minc = min(r, g, b)
    v = maxc
    if minc == maxc:
        return 0.0, 0.0, v
    s = (maxc-minc) / maxc
    rc = (maxc-r) / (maxc-minc)
    gc = (maxc-g) / (maxc-minc)
    bc = (maxc-b) / (maxc-minc)
    if r == maxc:
        h = bc-gc
    elif g == maxc:
        h = 2.0+rc-bc
    else:
        h = 4.0+gc-rc
    h = (h/6.0) % 1.0
    return h, s, v


GREEN_RANGE_MIN_HSV = (100, 80, 70)
GREEN_RANGE_MAX_HSV = (185, 255, 255)

def main():
    for car in masini:
        if exists(car + ".jpg"):
            print("remove bg la masina " + car)
            im = Image.open(car + ".jpg")
            im = im.convert('RGBA')

            pix = im.load()
            width, height = im.size
            for x in range(width):
                for y in range(height):
                    r, g, b, a = pix[x, y]
                    h_ratio, s_ratio, v_ratio = rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)
                    h, s, v = (h_ratio * 360, s_ratio * 255, v_ratio * 255)

                    min_h, min_s, min_v = GREEN_RANGE_MIN_HSV
                    max_h, max_s, max_v = GREEN_RANGE_MAX_HSV
                    if min_h <= h <= max_h and min_s <= s <= max_s and min_v <= v <= max_v:
                        pix[x, y] = (0, 0, 0, 0)


            im.save(car + '.png')
        else: 
            print("masina " + car + " nu exista")


if __name__ == '__main__':
    main()