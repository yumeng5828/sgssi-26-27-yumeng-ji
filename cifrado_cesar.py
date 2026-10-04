import string  
# Importa el módulo 'string', que contiene constantes como ascii_uppercase y ascii_lowercase
from langdetect import detect_langs, DetectorFactory
# Importa 'detect_langs' (devuelve idiomas con probabilidades) y 'DetectorFactory' (para fijar la semilla)

DetectorFactory.seed = 0
# Fija la semilla del detector → resultados reproducibles (siempre los mismos ante la misma entrada)

mensaje = input("Mensaje: ")

alfabeto_mayus = string.ascii_uppercase # Guarda "ABCDEFGHIJKLMNOPQRSTUVWXYZ" en 'alfabeto_mayus'
alfabeto_minus = string.ascii_lowercase # Guarda "abcdefghijklmnopqrstuvwxyz" en 'alfabeto_minus'

def descifrar(texto, clave): # Define una función que descifra 'texto' con un desplazamiento 'clave'
    salida = []

    for ch in texto:
        if ch in alfabeto_mayus:
            i = alfabeto_mayus.index(ch) # obtiene su posición en el alfabeto (0-25)
            salida.append(alfabeto_mayus[(i - clave) % 26]) 
            # Resta la clave, aplica módulo 26 (para dar la vuelta Z→A) y añade la letra resultante
        elif ch in alfabeto_minus:
            i = alfabeto_minus.index(ch)
            salida.append(alfabeto_minus[(i - clave) % 26])
        else: # Si NO es una letra (espacio, coma, punto, etc.)...
            salida.append(ch) # ...lo deja tal cual, sin modificarlo

    return "".join(salida) # Une todos los caracteres de la lista en una sola cadena y la devuelve

mejor_clave = None
mejor_texto = None
mejor_score = -1.0

for clave in range(26):
    candidato = descifrar(mensaje, clave)
    try: # Intenta (puede fallar con textos muy cortos o sin letras)
        langs = detect_langs(candidato) # Detecta los idiomas del candidato → lista de idiomas con probabilidades
        score_es = next((l.prob for l in langs if l.lang == "es"), 0.0) # Busca la probabilidad de que sea español; si no está, 0.0
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
#python "/home/yumeng-ji/sgssi-26-27-yumeng-ji/cifrado_cesar.py"