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
    "aiohttp[speedups]","httpcore", "trio", "starlette", "anyio", "quart", "h11", "uvicorn[standard]",
    "peewee", "pony", "asyncpg", "aiosqlite", "asyncmy", "databases",
    "requests-cache", "requests-html", "httpx[socks]",
    "flit", "poetry", "build", "twine", "setuptools", "wheel",
    "pytest", "hypothesis", "tox", "coverage", "nose2", "pytest-asyncio",
    "black", "flake8", "pylint", "isort", "mypy",
    "pyparsing", "lark", "parsimonious", "regex", "ply",
    "docutils", "sphinx", "mkdocs", "pdoc", "nbsphinx",
    "pyyaml", "toml", "configparser", "jsonschema", "cerberus",
    "plotnine", "seaborn", "bokeh", "altair", "holoviews", "dash-bootstrap-components",
    "pygwalker", "sweetviz", "dtale", "autoviz", "eda",
    "transformers[sentencepiece]", "sentence-transformers", "diffusers", "datasets", "peft",
    "deepspeed", "accelerate", "bitsandbytes", "huggingface-hub",
    "onnx", "onnxruntime", "onnxruntime-tools", "tensorflow-probability",
    "jax", "flax", "optax", "scvi-tools", "torchvision", "torchaudio",
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
    "starlette", "quart", "falcon", "responder", "hug", "tornado", "bottle", "fastapi-utils", "connexion", "sanic",
    "aiodns", "aiomysql", "aioredis", "aiobotocore", "aiopg", "asgi-lifespan", "async-lru",
    "dataset", "orm", "mongoengine", "py2neo", "redis", "arango", "couchdb", "influxdb", "pyrebase", "fireo",
    "bcrypt", "argon2-cffi", "passlib", "hashids", "keyring", "simple-crypt", "secure-smtplib",
    "scrapy", "mechanize", "grab", "robobrowser", "cloudscraper", "html5lib", "parsel",
    "invoke", "fabric", "click", "typer", "fire", "python-crontab", "pexpect",
    "datatable", "orange3", "feature-engine", "category_encoders", "imbalanced-learn", "patsy", "lifelines",
    "missingno", "pygal", "plotext", "bqplot", "hvplot", "vega-datasets", "altair-viewer",
    "lightgbm", "xgboost", "catboost", "mlxtend", "mlflow", "optuna", "shap", "lime", "autokeras", "darts", "neuralprophet", "pytorch-lightning",
    "spacy", "gensim", "sumy", "textstat", "pattern", "polyglot", "gTTS", "deep-translator", "newspaper3k",
    "albumentations", "imageio", "imgaug", "face-alignment", "scikit-video",
    "librosa", "audioread", "soundfile", "madmom", "moviepy-editor", "yt-dlp", "ytmusicapi", "spotipy",
    "RPi.GPIO", "gpiozero", "pyserial", "smbus", "adafruit-circuitpython-mcp9808", "pyfirmata",
    "arcade", "ursina", "pyglet", "pyxel", "tcod", "pursuedpybear",
    "factory_boy", "pytest-cov", "pytest-mock", "unittest-xml-reporting", "responses", "vcrpy",
    "camelot-py", "tabula-py", "textract", "docsplit", "pypdfium2", "pandocfilters",
    "email-validator", "validators", "blinker", "itsdangerous", "python-slugify", "humanize", "retry", "tenacity",
    "restless", "apistar", "python-socketio", "python-engineio", "python-sse", "requests-oauthlib",
    "websockets", "aiohttp-cors", "aiohttp-jinja2", "asyncssh", "aiocoap", "quart-cors", "quart-schema",
    "zodb", "elasticsearch", "pyArango", "hiredis", "sqlitedict", "txmongo", "rethinkdb", "apsw", "orator",
    "pyjwt", "python-jose", "secure", "flask-talisman", "python-pam", "ldap3", "cryptography_vectors",
    "html2data", "demjson", "xmltodict", "pyquery", "feedparser", "boilerpy3", "trafilatura", "newspaper",
    "automa", "autogui", "watchfiles", "pywinauto", "robotframework", "screeninfo", "pymsgbox", "pygetwindow",
    "python-cli-ui", "clint", "bullet", "prompt_toolkit", "pyinputplus", "inquirer", "python-box", "halo",
    "pymc3", "cmdstanpy", "bayespy", "heamy", "deepchem", "ramp-workflow", "mljar-supervised", "featuretools",
    "dtreeviz", "eli5", "yellowbrick", "auto-sklearn", "scikit-optimize", "ml-insights", "causalnex",
    "ctransformers", "deepface", "llama-cpp-python", "transformers[torch]", "sentencepiece", "vllm", "guidance",
    "langserve", "instructorembedding", "autogen", "openai-whisper", "whisperx", "audio-recorder-streamlit",
    "rembg", "clip", "dlib", "easyocr", "supervision", "imagehash", "blurhash", "imutils", "faceid", "mediapipe-silicon",
    "audiosegment", "aubio", "spleeter", "pyo", "sounddevice", "noisereduce", "pyroomacoustics", "praat-parselmouth",
    "imageio-ffmpeg", "opencv-contrib-python", "decord", "av", "vidstab", "vidgear",
    "arcade", "ursina", "manimce", "pyimgui", "dearpygui", "kivymd", "pyqtgraph", "pywebview", "cefpython3",
    "glumpy", "mayavi", "vispy", "plotly-express", "bokeh-server", "matplotlib-venn", "kaleido", "datashader",
    "pdfquery", "pdfminer3k", "pdfme", "reportlab-graphics", "python-docx-template", "docx2txt", "pandoc", "pytextrank",
    "inflect", "num2words", "prettytable", "tabulate", "deepdiff", "python-decouple", "fuzzywuzzy", "levenshtein",
    "shortuuid", "slugify", "python-fsutil", "oscrypto", "pyusb", "pynmea2", "pygtrie", "cachier", "retrying", "os"
]

print(f"Instalando {len(libraries)} librerías...")

for lib in libraries:
    os.system(f"pip install {lib}")

print("✅ Instalación completada.")
```

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

### 🛡️ Licencia

Este proyecto está bajo una licencia personalizada de uso **No Comercial**.  
Podés usarlo y modificarlo libremente, pero **no está permitido venderlo**.  
Consulta el archivo `LICENSE.txt` para más información.

---

## 👤 Autor

- 👨‍💻 Creador: **Ryxu**
- 📅 Proyecto iniciado: 25 de julio de 2025
- 📧 Contacto: **[Discord de Soporte](https://discord.gg/Fp8dWPBmKz)**

📫 ¿Necesitás ayuda?
Abrí un ticket directamente desde el servidor de Discord.

---

¡Gracias por usar y apoyar este proyecto! 🚀
