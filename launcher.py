import os
from config_gui import main as config_gui
from app import main as app_main

def load_shortcut():
    if os.path.exists("config.txt"):
        with open("config.txt", "r") as f:
            for line in f:
                if line.startswith("shortcut="):
                    return line.split("=")[1].strip()
    return 's'  # Default shortcut

if __name__ == "__main__":
    if not os.path.exists("config.txt"):
        print("Running configuration GUI for the first time...")
        config_gui()  # Call the config_gui main function

    shortcut = load_shortcut()
    print(f"Using shortcut: '{shortcut}'")
    app_main(shortcut)  # Pass the shortcut to app_main