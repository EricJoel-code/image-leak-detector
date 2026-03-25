def calculate_risk(findings):
    score = 0
    
    for f in findings:
        if f["type"] == "CRITICAL":
            score += 5
        elif f["type"] == "MEDIUM":
            score += 3
        elif f["Type"] == "LOW":
            score +=1
            
    if score >= 7:
        return "HIGH"
    elif score >= 3:
        return "MEDIUM"
    else:
        return "LOW"