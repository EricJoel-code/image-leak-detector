import os

from core.extractor import extract_metadata
from core.analyzer import analyze_metadata
from core.risk_engine import calculate_risk
from utils.hashing import calculate_sha256
from .correlator import group_by_device, group_by_location, detect_duplicates

# Extenciones validas de las imagenes
VALID_EXTENSIONS = (".jpg", ".jpeg", ".png", ".tiff")

def scan_folder(folder_path):
    """
    Recorre una carpeta y analiza todas las imagenes validas.
    
    Parámetros:
    - folder_path: ruta de la carpeta a analizar 
    
    Retorna:
    - lista de resultados (uno por imagen)
    """
    
    results = []
    
    # Recorremos todos los archivos de la carpeta
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        #Validamos que sea archivo y que sea imagen
        if os.path.isfile(file_path) and filename.lower().endswith(VALID_EXTENSIONS):
            
            print(f"\n[+] Analizando: {filename}")
            
            # 1. Extraer metadata
            metadata = extract_metadata(file_path)
            
            if not metadata:
                print("[ERROR] No se pudo extraer metadata")
                continue
            
            # 2. Analizar metadata
            findings = analyze_metadata(metadata)
            
            # 3. Calcular riesgo
            risk = calculate_risk(findings)
            
            # Calculamos hash para identificar archivos únicos (opcional pero útil para grandes carpetas)
            file_hash = calculate_sha256(file_path)
            
            # 4. Guardamos resultado estructurado
            result = {
                "file": filename,
                "path": file_path,
                "risk": risk,
                "findings": findings,
                "hash": file_hash
            }
            
            results.append(result)
            
            # Output básico
            print(f"[!] Riesgo: {risk}")
            
    # 5. Correlacionar resultados
    correlations = {
        "by_device": group_by_device(results),
        "by_location": group_by_location(results),
        "duplicates": detect_duplicates(results)
    }
            
    return results, correlations