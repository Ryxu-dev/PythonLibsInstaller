# PythonLibsInstaller
# Instalador y Descripción de Librerías Python

🔍 **Descripción**  
Este proyecto contiene 1 script:
1. **Listado y descripción de librerías instaladas:** Obtiene la lista de librerías Python instaladas en el entorno y busca sus descripciones desde PyPI, para generar un archivo de texto con esta información.  
2. **Instalador masivo de librerías:** Instala automáticamente una lista extensa de librerías populares y útiles para diferentes ámbitos (web, ciencia de datos, multimedia, automatización, etc.) usando `pip`.

---

## Uso

### 1. Listar librerías instaladas con descripción

El script escanea todas las librerías instaladas y consulta PyPI para obtener una breve descripción de cada una. Genera un archivo `libreriasinstaladas.txt` con los resultados y también los imprime en consola.

### 2. Instalación automática de librerías

Este script instala una gran lista `(170 librerías)` de librerías Python usando el comando `pip install`.

```python
import subprocess
import sys
import pkg_resources
import requests

### CONTROL DE LIBRERIAS ###

def get_description(lib_name):
    try:
        resp = requests.get(f"https://pypi.org/pypi/{lib_name}/json", timeout=5)
        if resp.ok:
            return resp.json()["info"]["summary"]
    except requests.RequestException:
        return "Descripción no encontrada"
    return "No disponible"

def get_installed_libraries():
    installed = sorted([i.key for i in pkg_resources.working_set])
    print(f"🔍 Encontradas {len(installed)} librerías instaladas.\n")
    return installed

def save_library_descriptions(libraries, filename="libreriasinstaladas.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for lib in libraries:
            desc = get_description(lib)
            file.write(f"{lib}: {desc}\n")
            print(f"{lib}: {desc}")

### INSTALACION DE LIBRERIAS ###

def install_libraries(libraries):
    for lib in libraries:
        print(f"Instalando {lib}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
        except subprocess.CalledProcessError:
            print(f"⚠️ Error instalando {lib} (NO LO FRENES, SEGUIRÁ CON LA SIGUIENTE)")

### SEGUNDO CONTROL DEL LIBRERIAS INSTALADAS ###
#     installed = get_installed_libraries()
def main():
    installed = get_installed_libraries()
    save_library_descriptions(installed)

### INSTALADOR ###

    # Lista de librerías para instalar
    libraries = sorted(set([
        "requests", "flask", "django", "numpy", "pandas", "matplotlib", "scipy", "scikit-learn",
        "beautifulsoup4", "lxml", "selenium", "pyautogui", "opencv-python", "pillow",
        "pygame", "pyqt6", "kivy", "sqlalchemy", "psycopg2", "mysql-connector-python",
        "aiohttp[speedups]", "httpcore", "trio", "starlette", "anyio", "quart", "h11", "uvicorn[standard]",
        "peewee", "pony", "asyncpg", "aiosqlite", "asyncmy", "databases",
        "requests-cache", "requests-html", "httpx[socks]",
        "flit", "poetry", "build", "twine", "setuptools", "wheel",
        "pytest", "hypothesis", "tox", "coverage", "nose2", "pytest-asyncio",
        "black", "flake8", "pylint", "isort", "mypy",
        "pyyaml", "toml", "configparser", "jsonschema", "cerberus",
        "plotnine", "seaborn", "bokeh", "altair", "dash-bootstrap-components",
        "transformers[sentencepiece]", "sentence-transformers", "diffusers", "datasets", "peft",
        "deepspeed", "accelerate", "bitsandbytes", "huggingface-hub",
        "onnx", "onnxruntime", "tensorflow-probability",
        "jax", "flax", "optax", "torchvision", "torchaudio",
        "boto3", "twilio", "pytube", "moviepy", "scikit-image", "nltk", "textblob",
        "torch", "tensorflow", "keras", "pyaudio", "speechrecognition",
        "pyttsx3", "face_recognition", "fastapi", "tqdm", "rich", "loguru",
        "cryptography", "pycryptodome", "pyinstaller", "pyarmor", "pywin32", "notebook",
        "jupyter", "ipython", "pydub", "pyperclip", "pyshorteners", "pyzbar", "pynput",
        "pywhatkit", "keyboard", "pikepdf", "fpdf", "openpyxl", "xlrd", "xlwt", "reportlab",
        "faker", "colorama", "termcolor", "pandas-profiling", "yfinance", "streamlit",
        "dash", "plotly", "pyfiglet", "schedule", "psutil", "watchdog",
        "auto-py-to-exe", "flask-login", "flask-cors",
        "python-dotenv", "pymongo", "pymysql", "tinydb", "whois",
        "dnspython", "bs4", "pyOpenSSL", "certifi", "pydantic", "jinja2",
        "markdown2", "markdownify", "pygments", "weasyprint", "markdown", "html2text",
        "pytelegrambotapi", "telebot", "discord.py", "nextcord", "pycord", "aiofiles",
        "fastapi-users", "fastapi-jwt-auth", "authlib", "itsdangerous", "werkzeug",
        "flask_sqlalchemy", "flask_marshmallow", "marshmallow", "sqlmodel", "uvloop",
        "python-multipart", "qrcode", "pdf2image", "pdfminer.six", "pdfplumber", "fitz",
        "pdf2docx", "docx", "python-docx", "python-pptx", "python-barcode", "pyglet",
        "manim", "sympy", "pycalc", "tkcalendar", "google-api-python-client", "google-auth",
        "gspread", "openai", "langchain", "llama-index", "chromadb", "faiss-cpu",
        "open3d", "mediapipe", "cvzone", "ultralytics",
    ]))

### CONFIRMACION DEL PARA INSTALAR ###

    respuesta = input("\n¿Querés continuar con la instalación de las librerías listadas? (s/n): ").strip().lower()
    if respuesta == "s":
        install_libraries(libraries)
        print("\n✅ Instalación completada.")
    else:
        print("\nInstalaccion cancelada, cerrando programa...")

if __name__ == "__main__":
    main()
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
