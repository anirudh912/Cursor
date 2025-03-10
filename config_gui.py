import tkinter as tk
from tkinter import messagebox

def save_settings(shortcut_entry, root):
    shortcut = shortcut_entry.get()
    if not shortcut:
        messagebox.showerror("Error", "Please enter a shortcut key.")
        return

    # Save shortcut to config file
    with open("config.txt", "w") as f:
        f.write(f"shortcut={shortcut}\n")

    messagebox.showinfo("Success", f"Shortcut '{shortcut}' saved successfully!")
    root.destroy()

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Configure Shortcuts")

    # Shortcut input
    tk.Label(root, text="Enter shortcut key (e.g., 's' or 'Ctrl+D'):").grid(row=0, column=0, padx=10, pady=10)
    shortcut_entry = tk.Entry(root)
    shortcut_entry.grid(row=0, column=1, padx=10, pady=10)

    # Save button
    tk.Button(root, text="Save", command=lambda: save_settings(shortcut_entry, root)).grid(row=1, column=0, columnspan=2, pady=10)

    # Run GUI
    root.mainloop()

if __name__ == "__main__":
    main()