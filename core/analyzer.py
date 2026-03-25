from core.rules import RULES

def analyze_metadata(metadata):
    findings = []
    
    for rule in RULES:
        result = rule(metadata)
        if result:
            findings.append(result)
            
    return findings