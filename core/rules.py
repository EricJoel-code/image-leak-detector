def detect_gps(metadata):
    if metadata.get("GPSLatitude") and metadata.get("GPSLongitude"):
        return {
            "type": "CRITICAL",
            "type": "GPS_DATA",
            "message": "La imagen contiene coordenadas GPS (posible fuga de ubicacion)"
        }
    return None

def detect_software(metadata):
    software = metadata.get("Software", "")
    suspicious = ["Photoshop", "GIMP", "Lightroom"] 
    
    for s in suspicious:
        if s.lower() in software.lower():
            return {
                "type": "MEDIUM",
                "type": "EDITING_SOFTWARE",
                "message": f"Imagen editada con {s}"
            }
    return None

def detect_timestamp(metadata):
    if metadata.get("CreateDate"):
        return {
            "type": "LOW",
            "rule": "TIMESTAMP",
            "message": "La imagen contiene fecha de creación"
        }
    return None   


RULES = [
    detect_gps,
    detect_software,
    detect_timestamp
]