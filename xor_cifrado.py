#!/usr/bin/env python3

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """Aplica XOR byte a byte entre dos cadenas de bytes de igual longitud."""
    if len(a) != len(b):
        raise ValueError(
            f"Las cadenas deben tener la misma longitud: "
            f"{len(a)} != {len(b)}"
        )
    return bytes(x ^ y for x, y in zip(a, b))


def a_hex(b: bytes) -> str:
    """Devuelve una representación hexadecimal legible."""
    return ' '.join(f'{x:02x}' for x in b)


def a_ascii(b: bytes) -> str:
    """Devuelve la representación ASCII (para mostrar el texto)."""
    return b.decode('utf-8', errors='replace')


def main():
    # --- Datos de prueba ---
    mensaje_str = "ATAQUE AL AMANECER"
    clave_str   = "CLAVE12345678901"

    print(f"Longitud mensaje: {len(mensaje_str)}")
    print(f"Longitud clave:   {len(clave_str)}")

    # --- Ajustar longitudes (deben coincidir) ---
    if len(clave_str) < len(mensaje_str):
        # Repetir la clave hasta cubrir el mensaje (como en cifrado de flujo real)
        repeticiones = len(mensaje_str) // len(clave_str) + 1
        clave_str = (clave_str * repeticiones)[:len(mensaje_str)]
    elif len(clave_str) > len(mensaje_str):
        clave_str = clave_str[:len(mensaje_str)]

    # --- Convertir a bytes ---
    mensaje = mensaje_str.encode('utf-8')
    clave   = clave_str.encode('utf-8')

    print(f"\n{'='*70}")
    print(f"MENSAJE ORIGINAL")
    print(f"{'='*70}")
    print(f"Texto:  {mensaje_str}")
    print(f"Hex:    {a_hex(mensaje)}")
    print(f"Bytes:  {len(mensaje)}")

    print(f"\n{'='*70}")
    print(f"CLAVE")
    print(f"{'='*70}")
    print(f"Texto:  {clave_str}")
    print(f"Hex:    {a_hex(clave)}")
    print(f"Bytes:  {len(clave)}")

    # --- Cifrar ---
    criptograma = xor_bytes(mensaje, clave)

    print(f"\n{'='*70}")
    print(f"CRIPTOGRAMA (mensaje ⊕ clave)")
    print(f"{'='*70}")
    print(f"Hex:    {a_hex(criptograma)}")
    print(f"Bytes:  {len(criptograma)}")

    # --- Descifrar (misma operación) ---
    descifrado = xor_bytes(criptograma, clave)

    print(f"\n{'='*70}")
    print(f"DESCIFRADO (criptograma ⊕ clave)")
    print(f"{'='*70}")
    print(f"Texto:  {a_ascii(descifrado)}")
    print(f"Hex:    {a_hex(descifrado)}")

    # --- Comprobación ---
    print(f"\n{'='*70}")
    if descifrado == mensaje:
        print("✅ CORRECTO: el descifrado coincide con el mensaje original.")
    else:
        print("❌ ERROR: el descifrado NO coincide con el mensaje original.")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()