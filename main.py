from PIL import Image
import os
import pytesseract
import glob
import pyperclip
import keyboard
from notifypy import Notify
from pathlib import Path

## Get folder for screenshots
screenshots_folder = str(Path.home() / "Pictures" / "Screenshots")

## Notifications Setup    :TD: Make audio cue for it
notification = Notify()
notification.title = "ImageToText"
notification.message = "Finished copying image text"
notification.icon = r"notification_media\checkmark.png"
notification.audio = r"notification_media\sound_cue.wav"

## Embed tesseract executable in folder
pytesseract.pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"

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

keyboard.add_hotkey("ctrl+shift+alt+p", Copy_Screenshot)

print("CopyPy Initialized")

keyboard.wait()