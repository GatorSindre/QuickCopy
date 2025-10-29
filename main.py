from PIL import Image
import os
import pytesseract
import glob
import pyperclip
import keyboard
from notifypy import Notify
from pathlib import Path
import sys
import pyautogui
import time

## Used to access temporary files from .exe cache
base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
## Get direct file path's
icon_path = os.path.join(base_path, "notification_media", "checkmark.png")
audio_path = os.path.join(base_path, "notification_media", "sound_cue.wav")
tesseract_path = os.path.join(base_path, "Tesseract-OCR", "tesseract.exe")


## Get folder for screenshots
screenshots_folder = str(Path.home() / "Pictures" / "Screenshots")

## Notifications Setup    :TD: Make audio cue for it
notification = Notify()
notification.title = "ImageToText"
notification.message = "Finished copying image text"
notification.icon = icon_path
notification.audio = audio_path

## Embed tesseract executable in folder
pytesseract.pytesseract.tesseract_cmd = tesseract_path

## Copy Screenshot Event
def Copy_Screenshot():

    ## Gets folder of screenshots
    screenshots = glob.glob(os.path.join(screenshots_folder, "*.png"))

    if not screenshots:
        print("no screenshots found")
        return

    ## Returns the newest screenshot
    newest_screenshot = max(screenshots, key=os.path.getctime)

    ## Convert it to text
    image = Image.open(newest_screenshot)
    text = pytesseract.image_to_string(image)
    
    if text:
        ## Put it onto the clipboard
        pyperclip.copy(text)

        ## Send a notification to let them know
        notification.send()

## Run in background with low cpu using an event

def Write_Bypass():
    time.sleep(1)

    copied_text = pyperclip.paste()

    pyautogui.write(copied_text, interval=0.02)

keyboard.add_hotkey("ctrl+shift+alt+p", Copy_Screenshot)
keyboard.add_hotkey("ctrl+shift+alt+o", Write_Bypass)

print("CopyPy Initialized")

keyboard.wait()