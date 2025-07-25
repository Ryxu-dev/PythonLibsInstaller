# 📦 Python Library Scanner & Installer

Este proyecto incluye dos scripts:

1. **Lector de librerías instaladas:** escanea tu entorno de Python, lista todas las librerías instaladas y busca su descripción en PyPI.
2. **Instalador masivo de librerías:** instala automáticamente una lista extensa de librerías populares de Python.

## 🚀 Funcionalidades

- Escaneo y descripción de paquetes instalados.
- Generación de un archivo `installed_libraries_info.txt` con la información.
- Instalación automática de más de 150 librerías comunes de Python para desarrollo, ciencia de datos, web, automatización y más.

## 📂 Archivos incluidos

- `scanner.py`: escanea librerías y guarda sus descripciones.
- `installer.py`: instala automáticamente todas las librerías listadas.
- `requirements.txt`: contiene todas las librerías listadas.
- `LICENSE`: licencia MIT.

## ⚙️ Requisitos

- Python 3.7+
- Conexión a internet
- `pip` funcionando correctamente

## ✅ Uso

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/python-library-scanner.git
cd python-library-scanner
```

2. Ejecuta el escáner:

python scanner.py

3. Para instalar todas las librerías de requirements.txt:
pip install -r requirements.txt

O, para usar el instalador personalizado:

python installer.py

