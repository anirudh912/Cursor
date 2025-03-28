# Cursor

# Screen Text Scanner

![Project Status](https://img.shields.io/badge/status-in%20progress-yellow)  
*A Python application that allows you to scan text from your screen using OCR (Optical Character Recognition) and use the extracted text on webservices like Google Search. The task results are displayed in a pop-up window.*

---

## 🚧 Project Status
This project is currently **in progress**. New webservice plugins, features and improvements are being actively worked on and will be added soon. Stay tuned for updates!

---

## Features
- **Text Scanning**: Select a region of your screen to extract text using EasyOCR. Possible to scan text in an image to be used for convenience.
- **Customizable Shortcut**: Set a custom shortcut key for scanning.
- **Customizable Use Cases**: Can be set to use any other webservice(by default it is Google Search with hyperlink results). Or also can be configured for other tasks using the scanned text.

---

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- `pip` (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/screen-text-scanner.git
   cd screen-text-scanner

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the application:
   ```bash
   python launcher.py

## 🖥️ Usage

1. When the application starts, you will be prompted to set a shortcut key (e.g., Ctrl+D).

2. Use the shortcut key to select a region of your screen for text extraction.

3. The extracted text will be used for Google Search or any other configured task.
