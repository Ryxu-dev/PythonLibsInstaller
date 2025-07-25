# PythonLibsInstaller
# Instalador y Descripción de Librerías Python

🔍 **Descripción**  
Este proyecto contiene dos scripts principales:  
1. **Listado y descripción de librerías instaladas:** Obtiene la lista de librerías Python instaladas en el entorno y busca sus descripciones desde PyPI, para generar un archivo de texto con esta información.  
2. **Instalador masivo de librerías:** Instala automáticamente una lista extensa de librerías populares y útiles para diferentes ámbitos (web, ciencia de datos, multimedia, automatización, etc.) usando `pip`.

---

## Uso

### 1. Listar librerías instaladas con descripción

El script escanea todas las librerías instaladas y consulta PyPI para obtener una breve descripción de cada una. Genera un archivo `installed_libraries_info.txt` con los resultados y también los imprime en consola.

```python
import pkg_resources
import requests

def get_description(lib_name):
    try:
        resp = requests.get(f"https://pypi.org/pypi/{lib_name}/json", timeout=5)
        if resp.ok:
            return resp.json()["info"]["summary"]
    except:
        return "Descripción no encontrada"
    return "No disponible"

installed = sorted(["%s" % i.key for i in pkg_resources.working_set])
print(f"🔍 Encontradas {len(installed)} librerías instaladas.\n")

with open("installed_libraries_info.txt", "w", encoding="utf-8") as file:
    for lib in installed:
        desc = get_description(lib)
        file.write(f"{lib}: {desc}\n")
        print(f"{lib}: {desc}")
````

### 2. Instalación automática de librerías

Este script instala una gran lista de librerías Python usando el comando `pip install`.

```python
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
```

---

## Lista de Dependencias a Instalar

* requests
* flask
* django
* numpy
* pandas
* matplotlib
* scipy
* sklearn
* beautifulsoup4
* lxml
* selenium
* pyautogui
* opencv-python
* pillow
* pygame
* pyqt6
* tk
* kivy
* sqlalchemy
* psycopg2
* mysql-connector-python
* boto3
* twilio
* pytube
* moviepy
* scikit-image
* nltk
* textblob
* transformers
* torch
* tensorflow
* keras
* pyaudio
* speechrecognition
* pyttsx3
* face\_recognition
* fastapi
* uvicorn
* tqdm
* rich
* loguru
* cryptography
* pycryptodome
* pyinstaller
* pyarmor
* pywin32
* notebook
* jupyter
* ipython
* pydub
* pyperclip
* pyshorteners
* pyzbar
* pynput
* pywhatkit
* keyboard
* pikepdf
* fpdf
* openpyxl
* xlrd
* xlwt
* reportlab
* faker
* colorama
* termcolor
* pandas-profiling
* yfinance
* streamlit
* dash
* plotly
* pyfiglet
* schedule
* py-cpuinfo
* psutil
* watchdog
* auto-py-to-exe
* asyncio
* aiohttp
* flask-login
* flask-cors
* python-dotenv
* dotenv
* pymongo
* pymysql
* sqlite3
* tinydb
* whois
* dnspython
* httpx
* bs4
* pyOpenSSL
* certifi
* pydantic
* jinja2
* markdown2
* markdownify
* pygments
* weasyprint
* markdown
* html2text
* pytelegrambotapi
* telebot
* discord.py
* nextcord
* pycord
* aiofiles
* fastapi-users
* fastapi-jwt-auth
* authlib
* itsdangerous
* werkzeug
* flask\_sqlalchemy
* flask\_marshmallow
* marshmallow
* sqlmodel
* uvloop
* python-multipart
* qrcode
* pdf2image
* pdfminer.six
* pdfplumber
* fitz
* pdf2docx
* docx
* python-docx
* python-pptx
* python-barcode
* pyglet
* manim
* sympy
* pycalc
* tkcalendar
* google-api-python-client
* google-auth
* gspread
* openai
* langchain
* llama-index
* chromadb
* faiss-cpu
* open3d
* mediapipe
* cvzone
* ultralytics
* tqdm
* aiohttp\[speedups]

---

## Otros Proyectos

Si te interesa, también desarrollé otros proyectos, puedes fijarte en mi **[DISCORD](https://discord.gg/Fp8dWPBmKz)** o en mi **[GITHUB](https://github.com/Ryxu-dev)**
---

## Discord

Para soporte, sugerencias o reportar bugs, podés unirte a nuestro **[Discord oficial](https://discord.gg/Fp8dWPBmKz)**

---

## 💵 Donaciones

Si te gustó este proyecto y querés apoyar mi trabajo, podés donar a través de mi servidor de Discord!

¡Muchas gracias! 🙌

---

## Licencia

Este proyecto está bajo la licencia MIT.
Puedes usar, modificar y distribuir libremente el código, siempre y cuando mantengas la atribución original.

---

## 👤 Autor

- 👨‍💻 Creador: **Ryxu**
- 📅 Proyecto iniciado: 25 de julio de 2025
- 📧 Contacto: **[Discord de Soporte](https://discord.gg/Fp8dWPBmKz)**

📫 ¿Necesitás ayuda?
Abrí un ticket directamente desde el servidor de Discord.

---

¡Gracias por usar y apoyar este proyecto! 🚀
