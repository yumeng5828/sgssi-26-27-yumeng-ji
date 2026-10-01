import string
from langdetect import detect_langs, DetectorFactory

DetectorFactory.seed = 0

mensaje = input("Mensaje: ")

alfabeto_mayus = string.ascii_uppercase
alfabeto_minus = string.ascii_lowercase

def descifrar(texto, clave):
    salida = []

    for ch in texto:
        if ch in alfabeto_mayus:
            i = alfabeto_mayus.index(ch)
            salida.append(alfabeto_mayus[(i - clave) % 26])
        elif ch in alfabeto_minus:
            i = alfabeto_minus.index(ch)
            salida.append(alfabeto_minus[(i - clave) % 26])
        else:
            salida.append(ch)

    return "".join(salida)

mejor_clave = None
mejor_texto = None
mejor_score = -1.0

for clave in range(26):
    candidato = descifrar(mensaje, clave)
    try:
        langs = detect_langs(candidato)
        score_es = next((l.prob for l in langs if l.lang == "es"), 0.0)
    except Exception:
        score_es = 0.0

    if score_es > mejor_score:
        mejor_score = score_es
        mejor_clave = clave
        mejor_texto = candidato

print("Clave encontrada:", mejor_clave)
print("Texto descifrado:", mejor_texto)

#Para ejecutar el script, primero crea un entorno virtual y activa el entorno virtual, 
#luego instala la biblioteca langdetect y finalmente ejecuta el script. Aquí están los comandos:
#python3 -m venv ~/venv-cifrado
#source ~/venv-cifrado/bin/activate
#pip install langdetect
#python "/home/yumeng-ji/Cifrado César.py"