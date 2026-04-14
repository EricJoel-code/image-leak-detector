import sys
import os

# Importamos servicios
from services.scanner import scan_folder
from services.sanitizer import sanitizer_image
from services.reporter import genertate_report, save_json_report 
from services.dlp import evaluate_dlp

# Importamos core para check individual
from core.extractor import extract_metadata
from core.analyzer import analyze_metadata
from core.risk_engine import calculate_risk

# Importamos formatter para imprimir resultados
from .formatter import print_image_result, prin_scan_summary, print_correlations, print_dlp_result

# Importamos utils para hashing
from utils.hashing import calculate_sha256



def handle_check(image_path, dlp_mode=False, auto_sanitize=False):
    """
    Analiza una imagen con soporte DLP y auto-sanitización
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

    # Usamos el formatter para imprimir resultados de forma legible
    print_image_result(image_path, risk, findings, file_hash)
    
    # 🔥 Si estamos en modo DLP, evaluamos la decisión y la imprimimos
    if dlp_mode:
        decision = evaluate_dlp(risk, findings)
        print_dlp_result(decision)
        
        # Si se recomienda auto-sanitización y el usuario lo ha solicitado, procedemos a sanitizar
        if auto_sanitize:
            
            if decision["auto_sanitize_recommended"]:
                print("\n[INFO] Ejecutando sanitización automatizada...")
                sanitizer_image(image_path)
            else:
                print("\n[INFO] No se recomienda sanitización automática para esta imagen según la evaluación DLP.")


def handle_scan(folder_path, json_output=None):
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
    
    # Exportar JSON si se solicita
    if json_output:
        report = genertate_report(results, correlations)
        save_json_report(report, json_output)


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
        print("  scan <carpeta> [--json output.json]")
        print("  sanitize <imagen>")
        return

    command = sys.argv[1]
    path = sys.argv[2]
    dlp_mode = "--dlp" in sys.argv
    auto_sanitize = "--auto-sanitize" in sys.argv
    
    # Opcional: manejo de argumento para exportar JSON
    json_output = None
    
    if "--json" in sys.argv:
        try:
            json_index = sys.argv.index("--json")
            json_output = sys.argv[json_index + 1]
        except IndexError:
            print("[ERROR] Debes especificar un archivo para exportar el JSON (--json)")
            return
            
    if command == "check":
        handle_check(path, dlp_mode, auto_sanitize)

    elif command == "scan":
        handle_scan(path, json_output)

    elif command == "sanitize":
        handle_sanitize(path)

    else:
        print("[ERROR] Comando no reconocido")