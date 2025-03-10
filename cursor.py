import numpy as np
import pyautogui
import easyocr
import time
import keyboard

reader = easyocr.Reader(['en'])

def capture_region(start_pos, end_pos):
    x1, y1 = start_pos
    x2, y2 = end_pos

    left = min(x1, x2)
    top = min(y1, y2)
    width = abs(x2 - x1)
    height = abs(y2 - y1)

    if width == 0 or height == 0:
        print("Error: Invalid selection region. Try again.")
        return None

    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

def extract_text(image):
    image_np = np.array(image)
    results = reader.readtext(image_np)
    extracted_text = " ".join([result[1] for result in results])
    return extracted_text

def scan_text(shortcut='s'):
    print(f"Press '{shortcut}' to start scanning text or 'q' to quit.")

    while True:
        # Check for multi-key shortcuts (e.g., Ctrl+D)
        if '+' in shortcut:
            keys = shortcut.split('+')
            if all(keyboard.is_pressed(key.strip()) for key in keys):
                print("Selection started. Move the mouse to define the region.")
                start_pos = pyautogui.position()
                time.sleep(0.2)  # Prevent immediate second detection

                while all(keyboard.is_pressed(key.strip()) for key in keys):
                    pass

                end_pos = pyautogui.position()
                screenshot = capture_region(start_pos, end_pos)

                if screenshot is not None:
                    e_text = extract_text(screenshot)
                    print("Extracted Text:", e_text)
                    return e_text
                else:
                    print("Skipping OCR due to invalid screenshot.")
                    return None
        # Check for single-key shortcuts (e.g., 's')
        elif keyboard.is_pressed(shortcut):
            print("Selection started. Move the mouse to define the region.")
            start_pos = pyautogui.position()
            time.sleep(0.2)

            while not keyboard.is_pressed(shortcut):
                pass

            end_pos = pyautogui.position()
            screenshot = capture_region(start_pos, end_pos)

            if screenshot is not None:
                e_text = extract_text(screenshot)
                print("Extracted Text:", e_text)
                return e_text
            else:
                print("Skipping OCR due to invalid screenshot.")
                return None

        if keyboard.is_pressed('q'):
            print("Exiting...")
            return None

        time.sleep(0.1)  # Prevent high CPU usage