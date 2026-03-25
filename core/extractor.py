import subprocess
import json
from config import EXIFTOOL_PATH


def extract_metadata(image_path):
    try:
        result = subprocess.run(
            [EXIFTOOL_PATH, "-json", "-fast", image_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=20
        )

        if result.returncode != 0:
            print(f"[ERROR][extractor] {result.stderr}")
            return None

        if not result.stdout.strip():
            print("[ERROR][extractor] salida vacía")
            return None

        data = json.loads(result.stdout)
        return data[0] if data else {}

    except subprocess.TimeoutExpired:
        print("[WARN][extractor] Timeout, reintentando...")

        try:
            result = subprocess.run(
                [EXIFTOOL_PATH, "-json", "-fast", image_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=30
            )

            data = json.loads(result.stdout)
            return data[0] if data else {}

        except Exception:
            print("[ERROR][extractor] fallo en reintento")
            return None

    except Exception as e:
        print(f"[ERROR][extractor] {e}")
        return None