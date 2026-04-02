def print_image_result(image_path, risk, findings, file_hash=None):
    """
    Imprime el resultado de análisis de una imagen
    de forma estructurada y legible.
    """
    
    print("\n" + "=" * 50)
    print(f"[+] Imagen: {image_path}")
    print(f"[!] Riesgo: {risk}")
    
    if file_hash:
        print(f"[#] Hash SHA-256: {file_hash}")
    
    print("-" * 50)
    
    if findings:
        print("Hallazgos: ")
        for f in findings:
            print(f"   - [{f['type']}] {f['message']}")
    else:
        print("No se detectaron riesgos ni hallazgos")
        
    print("=" * 50)
    
    
def prin_scan_summary(results):
    """
    Imprime un resumen de los resultados del escaneo
    de todas las imágenes analizadas.
    """
    
    print("\n" + "=" * 50)
    print("RESUMEN DEL ESCANEO")
    print("=" * 50)
    
    # Contadores de riesgo
    high = 0
    medium = 0
    low = 0
    
    for res in results:
        if res["risk"] == "HIGH":
            high += 1
        elif res["risk"] == "MEDIUM":
            medium += 1
        else:
            low +=1
            
    total = len(results)
    
    print(f"Total de imágenes analizadas: {total}")
    print(f"Riesgo ALTO: {high}")
    print(f"Riesgo MEDIO: {medium}")
    print(f"Riesgo BAJO: {low}")
    
    print("\nDetalles: ")
    for res in results:
        print(f" - {res['file']} -> {res['risk']}")
    
    print("=" * 50)
    
def print_correlations(correlations):
    """
    Imprime relaciones detectadas entre imágenes
    """
    
    print("\n" + "=" * 50)
    print("CORRELACIONES DETECTADAS")
    print("=" * 50)

    # 📷 Dispositivos
    print("\n[Dispositivos]")
    for device, files in correlations["by_device"].items():
        if len(files) > 1:
            print(f"\n{device}:")
            for f in files:
                print(f"  - {f}")

    # 📍 GPS
    print("\n[Ubicación]")
    print(f"Con GPS: {len(correlations['by_location']['WITH_GPS'])}")
    print(f"Sin GPS: {len(correlations['by_location']['WITHOUT_GPS'])}")

    # 🔐 Duplicados
    print("\n[Duplicados]")
    duplicates = correlations["duplicates"]

    if not duplicates:
        print("No se detectaron duplicados")
    else:
        for h, files in duplicates.items():
            print(f"\nHash: {h}")
            for f in files:
                print(f"  - {f}")

    print("=" * 50)