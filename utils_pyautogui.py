import sys, os
C = os.path.abspath(os.path.dirname(__file__))

import time

import pyautogui
from python_imagesearch.imagesearch import imagesearch

from loguru import logger
format_log = format='<green>{time:ddd DD/MM/YY HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'
logger.add(os.path.join(C, "file.log"), retention="30 days", backtrace=True, diagnose=True, format=format_log)
logger.add(os.path.join(C, "trace.log"), level="TRACE", retention="30 days", backtrace=True, diagnose=True, format=format_log)


TIMEOUT = 5  # temps d’essai du click

def desktop():
    # Retour au bureau
    logger.debug("Afficher bureau")
    size = pyautogui.size()
    pyautogui.click(x=size[0]-2, y=size[1]-2)
    time.sleep(1)


def clickOn(picture, times=0, double=False, under=0):
    if isinstance(under, bool):
        under = 30
    clicks = 2 if double else 1
    interval = 0.25
    if times == 0:
        logger.debug(f"Click {picture}")
        
    x, y = imagesearch(picture, 0.8)
    
    if x == -1:
        if times > TIMEOUT:
            logger.error(f"NOT CLICK : {picture}")
            return False
        else:  # retry
            time.sleep(1)
            return clickOn(picture, times=times+1, double=double)
    else:
        y += under
        pyautogui.click(x, y, clicks=clicks, interval=interval)
        time.sleep(1)
        return True
