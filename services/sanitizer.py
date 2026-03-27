import subprocess
from config import EXIFTOOL_PATH

def sanitizer_image(image_path):
    """
    Elimina todos los metadatos de una imagen.

    Esto es clave en DLP (Data Leakage Prevention).

    Parámetros:
    - image_path: ruta de la imagen
    """
    
    try:
        # ExifTool elimina metadata con -all=
        result = subprocess.run(
            [EXIFTOOL_PATH, "-all=", "-overwrite_original", image_path],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            text = True
        )
        
        if result.returncode == 0:
            print(f"[OK] Metadata eliminada: {image_path}")
        else:
            print(f"[ERROR] {result.stderr}")
    except Exception as e:
        print(f"[ERROR] Fallo al sanitizar: {e}")    