import sys
import os

# Importamos servicios
from services.scanner import scan_folder
from services.sanitizer import sanitizer_image 

# Importamos core para check individual
from core.extractor import extract_metadata
from core.analyzer import analyze_metadata
from core.risk_engine import calculate_risk

# Importamos formatter para imprimir resultados
from .formatter import print_image_result, prin_scan_summary, print_correlations

# Importamos utils para hashing
from utils.hashing import calculate_sha256



def handle_check(image_path):
    """
    Analiza una sola imagen
    """

    if not os.path.exists(image_path):
        print("[ERROR] La ruta no existe")
        return

    metadata = extract_metadata(image_path)

    if not metadata:
        print("[ERROR] No se pudo extraer metadata")
        return

    findings = analyze_metadata(metadata)
    risk = calculate_risk(findings)
    file_hash = calculate_sha256(image_path)

    # Usamos el formatter para imprimir resultados
    print_image_result(image_path, risk, findings, file_hash)


def handle_scan(folder_path):
    """
    Analiza una carpeta completa
    """

    if not os.path.exists(folder_path):
        print("[ERROR] La carpeta no existe")
        return

    results, correlations = scan_folder(folder_path)

    # Usamos el formatter para imprimir el resumen del escaneo y las correlaciones
    prin_scan_summary(results)
    print_correlations(correlations)


def handle_sanitize(image_path):
    """
    Elimina metadata de una imagen
    """

    if not os.path.exists(image_path):
        print("[ERROR] La ruta no existe")
        return

    sanitizer_image(image_path)


def run():
    """
    Punto de entrada principal del CLI
    """

    if len(sys.argv) < 3:
        print("Uso:")
        print("  check <imagen>")
        print("  scan <carpeta>")
        print("  sanitize <imagen>")
        return

    command = sys.argv[1]
    path = sys.argv[2]

    if command == "check":
        handle_check(path)

    elif command == "scan":
        handle_scan(path)

    elif command == "sanitize":
        handle_sanitize(path)

    else:
        print("[ERROR] Comando no reconocido")