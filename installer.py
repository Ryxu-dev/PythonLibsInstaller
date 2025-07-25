import os

libraries = [
    "requests", "flask", "django", "numpy", "pandas", "matplotlib", "scipy", "sklearn",
    "beautifulsoup4", "lxml", "selenium", "pyautogui", "opencv-python", "pillow",
    "pygame", "pyqt6", "tk", "kivy", "sqlalchemy", "psycopg2", "mysql-connector-python",
    "boto3", "twilio", "pytube", "moviepy", "scikit-image", "nltk", "textblob",
    "transformers", "torch", "tensorflow", "keras", "pyaudio", "speechrecognition",
    "pyttsx3", "face_recognition", "fastapi", "uvicorn", "tqdm", "rich", "loguru",
    "cryptography", "pycryptodome", "pyinstaller", "pyarmor", "pywin32", "notebook",
    "jupyter", "ipython", "pydub", "pyperclip", "pyshorteners", "pyzbar", "pynput",
    "pywhatkit", "keyboard", "pikepdf", "fpdf", "openpyxl", "xlrd", "xlwt", "reportlab",
    "faker", "colorama", "termcolor", "pandas-profiling", "yfinance", "streamlit",
    "dash", "plotly", "pyfiglet", "schedule", "py-cpuinfo", "psutil", "watchdog",
    "auto-py-to-exe", "asyncio", "aiohttp", "flask-login", "flask-cors",
    "python-dotenv", "dotenv", "pymongo", "pymysql", "sqlite3", "tinydb", "whois",
    "dnspython", "httpx", "bs4", "pyOpenSSL", "certifi", "pydantic", "jinja2",
    "markdown2", "markdownify", "pygments", "weasyprint", "markdown", "html2text",
    "pytelegrambotapi", "telebot", "discord.py", "nextcord", "pycord", "aiofiles",
    "fastapi-users", "fastapi-jwt-auth", "authlib", "itsdangerous", "werkzeug",
    "flask_sqlalchemy", "flask_marshmallow", "marshmallow", "sqlmodel", "uvloop",
    "python-multipart", "qrcode", "pdf2image", "pdfminer.six", "pdfplumber", "fitz",
    "pdf2docx", "docx", "python-docx", "python-pptx", "python-barcode", "pyglet",
    "manim", "sympy", "pycalc", "tkcalendar", "google-api-python-client", "google-auth",
    "gspread", "openai", "langchain", "llama-index", "chromadb", "faiss-cpu",
    "open3d", "mediapipe", "cvzone", "ultralytics", "tqdm", "aiohttp[speedups]"
]

print(f"Instalando {len(libraries)} librerías...")

for lib in libraries:
    os.system(f"pip install {lib}")

print("✅ Instalación completada.")