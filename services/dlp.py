def evaluate_dlp(risk, findings):
    """
    Evalúa acción DLP y si debe sanitizar automáticamente
    """
    
    decision = {
        "action": "ALLOW", 
        "reasons": [],
        "requires_sanitization": False,
        "auto_sanitize_recommended": False
    }
    
    # 🔴 Riesgo alto → bloquear
    if risk == "HIGH":
        decision["action"] = "BLOCK"
        decision["requires_sanitization"] = True
        decision["auto_sanitize_recommended"] = True
    
    # 🟡 Riesgo medio → advertir
    elif risk == "MEDIUM":
        decision["action"] = "WARN"
        decision["auto_sanitize_recommended"] = True
        
    # 🟢 Riesgo bajo → permitir
    else:
        decision["action"] = "ALLOW"
        
    # Agregar razones basadas en hallazgos específicos
    for f in findings:
        if f["rule"] == "GPS_DATA":
            decision["reasons"].append("Contiene datos de ubicación (GPS)")
        
        if f["rule"] == "DEVICE_INFO":
            decision["reasons"].append("Contiene información del dispositivo")
            
        if f["rule"] == "TIME_INCONSISTENCY":
            decision["reasons"].append("Posible edición detectada")
            
    return decision