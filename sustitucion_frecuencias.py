#!/usr/bin/env python3

import string
from collections import Counter

CRIPTOGRAMA = """RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.

AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJEKCI, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."""

# Frecuencias del español (según la tabla que te han dado)
FREC_ES = [
    ('e', 16.78), ('a', 11.96), ('o', 8.69), ('l', 8.37), ('s', 7.88),
    ('n', 7.01),  ('d', 6.87),  ('r', 4.94), ('u', 4.80), ('i', 4.15),
    ('t', 3.31),  ('c', 2.92),  ('p', 2.776),('m', 2.12), ('y', 1.54),
    ('q', 1.53),  ('b', 0.92),  ('h', 0.89), ('g', 0.73), ('f', 0.52),
    ('v', 0.39),  ('j', 0.30),  ('ñ', 0.29), ('z', 0.15), ('x', 0.06),
    ('k', 0.00),  ('w', 0.00),
]


def frecuencia_criptograma(texto):
    """Cuenta la frecuencia de cada letra del criptograma (solo A-Z)."""
    letras = [c for c in texto.upper() if c in string.ascii_uppercase]
    contador = Counter(letras)
    total = sum(contador.values())
    return [(letra, (n / total) * 100) for letra, n in contador.most_common()], total


def proponer_mapeo(frec_cripto):
    """Propone un mapeo automático: ordena el criptograma por frecuencia
    y lo empareja con las letras del español ordenadas por frecuencia."""
    cripto_orden = [l for l, _ in frec_cripto]
    es_orden = [l for l, _ in FREC_ES]
    mapeo = {}
    for c_cripto, c_es in zip(cripto_orden, es_orden):
        mapeo[c_cripto] = c_es
    return mapeo


def aplicar_mapeo(texto, mapeo):
    """Sustituye cada letra del texto según el mapeo dado."""
    return ''.join(mapeo.get(c.upper(), c) if c.isalpha() else c for c in texto)


def mostrar_estado(texto, mapeo):
    """Muestra el texto descifrado con el mapeo actual."""
    print("\n" + "=" * 70)
    print(aplicar_mapeo(texto, mapeo))
    print("=" * 70)


def mostrar_mapeo(mapeo):
    print("\nMapeo actual (criptograma → español):")
    for k in sorted(mapeo):
        print(f"  {k} → {mapeo[k]}", end="   ")
    print()


def main():
    # 1. Calcular frecuencias del criptograma
    frec_cripto, total = frecuencia_criptograma(CRIPTOGRAMA)

    print(f"Total de letras en el criptograma: {total}\n")
    print(f"{'Letra':>5} | {'Frecuencia':>10}")
    print("-" * 25)
    for letra, f in frec_cripto:
        print(f"{letra:>5} | {f:>9.2f}%")

    # 2. Proponer mapeo automático
    mapeo = proponer_mapeo(frec_cripto)

    # 3. Bucle interactivo
    print("\n--- Mapeo inicial automático ---")
    mostrar_estado(CRIPTOGRAMA, mapeo)
    mostrar_mapeo(mapeo)

    print("\nComandos:")
    print("  <c> <p>   → asignar letra del criptograma a letra del español")
    print("  <c> ?     → borrar la asignación de esa letra del criptograma")
    print("  m         → mostrar el mapeo actual")
    print("  q         → terminar")

    while True:
        cmd = input("\n> ").strip().lower().split()
        if not cmd:
            continue
        if cmd[0] == 'q':
            print("\n=== Resultado final ===")
            mostrar_estado(CRIPTOGRAMA, mapeo)
            break
        if cmd[0] == 'm':
            mostrar_mapeo(mapeo)
            continue
        if len(cmd) == 2:
            c_cripto = cmd[0].upper()
            c_es = cmd[1]
            if c_es == '?':
                mapeo.pop(c_cripto, None)
            else:
                mapeo[c_cripto] = c_es
            mostrar_estado(CRIPTOGRAMA, mapeo)
        else:
            print("Comando no reconocido.")


if __name__ == "__main__":
    main()