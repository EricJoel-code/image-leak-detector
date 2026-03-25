from core.extractor import extract_metadata
from core.analyzer import analyze_metadata
from core.risk_engine import calculate_risk

import sys
import os


def check_image(image_path):
    metadata = extract_metadata(image_path)

    if not metadata:
        print("Error al extraer metadata")
        return

    findings = analyze_metadata(metadata)
    risk = calculate_risk(findings)

    print(f"\n[+] Imagen: {image_path}")
    print(f"[!] Riesgo: {risk}\n")

    if findings:
        print("Hallazgos:")
        for f in findings:
            print(f"- [{f['type']}] {f['message']}")
    else:
        print("No se detectaron riesgos")
        
    if not os.path.exists(image_path):
        print(f"[ERROR] La ruta no existe: {image_path}")
        return


if __name__ == "__main__":
    image_path = sys.argv[1]
    check_image(image_path)