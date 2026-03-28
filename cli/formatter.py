def print_image_result(image_path, risk, findings):
    """
    Imprime el resultado de análisis de una imagen
    de forma estructurada y legible.
    """
    
    print("\n" + "=" * 50)
    print(f"[+] Imagen: {image_path}")
    print(f"[!] Riesgo: {risk}")
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