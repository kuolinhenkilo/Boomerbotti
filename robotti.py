"""Autoklikkeri, joka kirjautuu ja kirjoittaa tilapäivityksen Facebook-profiiliin"""


# https://pyautogui.readthedocs.io/en/latest/quickstart.html

import pyautogui
import random
import sys
import time


def klikkibotti(viesti: str):

    print("Boomer-botti alkaa")
    print(viesti)
    breakpoint()
    # Selaimen avaaminen

    firefox = pyautogui.locateCenterOnScreen(
        "kuvat/Firefox_osittainen.png", 
        confidence=0.8,
        grayscale=True
    )
    pyautogui.click(firefox.x/2, firefox.y/2)


    hätäjarru = 0
    while True:
        print("Odotetaan selaimen avautumista")
        if hätäjarru > 15: break
        if pyautogui.locateCenterOnScreen("kuvat/Selain.png"):
            break
        hätäjarru += 1
        time.sleep(1)

    # Facebookin avaaminen

    facebook = pyautogui.locateCenterOnScreen(
        "kuvat/Facebook.png", 
        confidence=0.9, 
        grayscale=True
    )
    pyautogui.click(facebook.x/2, facebook.y/2)
    print(facebook)
    time.sleep(2)

    # Sisäänkirjautuminen

    pyautogui.click(312, 473)
    time.sleep(1)
    pyautogui.click(572, 476)
    pyautogui.write("sirkka-parhaat-54", interval=0.1)
    pyautogui.click(714, 585)
    time.sleep(6)

    # Omaan profiiliin siirtyminen

    pyautogui.click(1311, 151)
    time.sleep(1)
    pyautogui.click(1023, 221)
    time.sleep(4)

    # Tilapäivityksen tekeminen

    mitamietit = pyautogui.locateCenterOnScreen(
        "kuvat/Mitä mietit.png", 
        confidence=0.8, 
        grayscale=True
    )
    pyautogui.click(mitamietit.x/2, mitamietit.y/2)
    time.sleep(2)

    lista = [
        "Pöyristys", 
        "Kauhistus", 
        "Ihastus", 
        "Harmistus", 
        "Hätäännys", 
        "Tuhahdus", 
        "Kohahdus", 
    ]

    rnd = random.randint(0, 6)

    pyautogui.write(lista[rnd], interval=0.2)
    pyautogui.click(718, 634)
    time.sleep(4)

    # Uloskirjautuminen

    pyautogui.click(1311, 151)
    time.sleep(1)
    pyautogui.click(1071, 548)


    print("Boomer-botti päättyy")


if __name__ == "__main__":
    viesti = sys.argv[1]
    klikkibotti(viesti)