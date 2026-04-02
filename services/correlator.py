def group_by_device(results):
    """
    Agrupa imágenes por dispositivo (Make + Model)

    Parámetros:
    - results: lista de resultados del scanner

    Retorna:
    - diccionario {device: [imagenes]}
    """
    
    device_groups = {}
    
    for r in results:
        # Buscamos información de dispositivos dentro de los hallazgos
        device_info = None
        
        for f in r["findings"]:
            if f["rule"] == "DEVICE_INFO":
                device_info = f["message"]
                break
            
        if not device_info:
            device_info = "UNKNOWN_DEVICE"
            
        # Agrupamos por dispositivo
        if device_info not in device_groups:
            device_groups[device_info] = []
            
        device_groups[device_info].append(r["file"])
        
    return device_groups


def group_by_location(results):
    """
    Agrupa imágenes por presencia de GPS
    (puedes mejorar luego con coordenadas exactas)
    """
    
    location_groups = {
        "WITH_GPS": [],
        "WITHOUT_GPS": []
    }
    
    for r in results:
        has_gps = any(f["rule"] == "GPS_DATA" for f in r["findings"])
        
        if has_gps:
            location_groups["WITH_GPS"].append(r["file"])
        else:
            location_groups["WITHOUT_GPS"].append(r["file"])

    return location_groups

def detect_duplicates(results):
    """
    Detecta imágenes duplicadas basándose en el hash de su contenido
    (puedes mejorar luego con técnicas de similitud visual)
    """
    
    hash_map = {}
    duplicates = {}
    
    for r in results:
        file_hash = r.get("hash")
        
        if not file_hash:
            continue
        
        if file_hash not in hash_map:
            hash_map[file_hash] = []
            
    # Filtrar solo hashes con mas de un archivo asociado
    for h, files in hash_map.items():
        if len(files) > 1:
            duplicates[h] = files
            
    return duplicates