#!/usr/bin/env python3
import subprocess


def test_integracion():
    # 1. Definir el comando como una lista de argumentos
    # (Usamos python -c para que funcione igual en Windows, Linux y Mac)
    comando = ["python3", "-m", "calculadora", "2+2", "10*2"]
    salida_esperada = ("2+2 = 4\n10*2 = 20")

    # 2. Ejecutar el comando y capturar la salida
    resultado = subprocess.run(
        comando,
        capture_output=True,  # Captura stdout y stderr
        text=True,  # Convierte la salida de bytes a string (UTF-8)
        check=True,  # Lanza excepción si el comando falla (código != 0)
    )

    # 3. Limpiar saltos de línea extra y comparar con el valor esperado
    salida_actual = resultado.stdout.strip()
    assert salida_actual in salida_esperada
