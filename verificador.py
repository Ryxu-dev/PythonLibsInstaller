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