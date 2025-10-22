from PIL import Image
import os
import pytesseract
import glob
import pyperclip
import keyboard

screenshot_folder = r"C:\Users\Sindre\Pictures\Screenshots"

def Copy_Screenshot():

    screenshots = glob.glob(os.path.join(screenshot_folder, "*.png"))

    if not screenshots:
        print("no screenshots found")
        return

    newest_screenshot = max(screenshots, key=os.path.getctime)

    image = Image.open(newest_screenshot)

    text = pytesseract.image_to_string(image)

    pyperclip.copy(text)

keyboard.add_hotkey("ctrl+shift+alt+p", Copy_Screenshot)

keyboard.wait()