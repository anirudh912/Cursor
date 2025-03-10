from cursor import scan_text
from gsearch import search_google
import tkinter as tk
from tkinter import messagebox, scrolledtext
import webbrowser

def open_link(url):
    """Open the clicked link in the default web browser."""
    webbrowser.open(url)

def show_results_popup(results):
    """Display search results as clickable links in a pop-up window."""
    popup = tk.Tk()
    popup.title("Search Results")

    # Create a scrollable frame for the links
    canvas = tk.Canvas(popup)
    scrollbar = tk.Scrollbar(popup, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    # Configure the canvas to use scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Add links to scrollable frame
    if results:
        for result in results:
            link_label = tk.Label(scrollable_frame, text=result, fg="blue", cursor="hand2")
            link_label.pack(anchor="w", padx=10, pady=5)
            link_label.bind("<Button-1>", lambda e, url=result: open_link(url))
    else:
        no_results_label = tk.Label(scrollable_frame, text="No results found.")
        no_results_label.pack(anchor="w", padx=10, pady=5)

    scrollable_frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Run the popup
    popup.mainloop()

def main(shortcut='s'):
    while True:
        print(f"Press '{shortcut}' to start scanning text or 'q' to quit.")
        text = scan_text(shortcut)
        if text is None:
            break

        print("Searching Google for the extracted text...")
        search_results = search_google(text)

        # Show results in a pop-up window with clickable links
        show_results_popup(search_results)

if __name__ == "__main__":
    main()