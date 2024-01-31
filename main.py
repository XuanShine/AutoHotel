import sys, os
C = os.path.abspath(os.path.dirname(__file__))

import time
import datetime
from datetime import timedelta

import pyautogui
from python_imagesearch.imagesearch import imagesearch

from utils_pyautogui import *

familyHotel = os.path.join(C, "pictures", "family.png")
utilisateur = os.path.join(C, "pictures", "utilisateur.png")
utilisateur2 = os.path.join(C, "pictures", "utilisateur2.png")
insee = os.path.join(C, "pictures", "insee.png")
date = os.path.join(C, "pictures", "date.png")
ok = os.path.join(C, "pictures", "ok.png")
mail = os.path.join(C, "pictures", "mail.png")
fermer = os.path.join(C, "pictures", "fermer.png")



# Retour au bureau
desktop()
clickOn(familyHotel)
if not clickOn(utilisateur):
    clickOn(utilisateur2)

clickOn(insee, double=True)

# mettre la dates
clickOn(date, under=True)
today = datetime.date.today()
dateMoisPrecedent = today - timedelta(days=28)
date1MoisPrecedent = datetime.date(dateMoisPrecedent.year, dateMoisPrecedent.month, 1)
pyautogui.write(date1MoisPrecedent.strftime("%d/%m/%Y"))
time.sleep(1)
clickOn(ok)
clickOn(mail)
clickOn(fermer)
# Maximiser
# Remplir le destinataire et message
"""
pyautogui.write()

# Clic Envoyer (pas obligatoire) -> minimiser puis réduire

# Tout fermer

# Remettre la page d’attente
"""