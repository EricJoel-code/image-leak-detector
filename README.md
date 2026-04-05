# 🛡️ ImageLeak Detector

**ImageLeak Detector** es una herramienta de seguridad enfocada en la **detección de fuga de información en imágenes digitales**, mediante el análisis de metadatos (EXIF).

Permite identificar exposición de información sensible como ubicación (GPS), dispositivos, timestamps y posibles signos de manipulación antes de compartir imágenes.

---

## 🎯 Problema que resuelve

Las imágenes contienen metadatos ocultos que pueden revelar:

* 📍 Ubicación exacta (coordenadas GPS)
* 🕒 Fecha y hora de captura
* 📷 Dispositivo utilizado
* 🛠️ Software de edición

Esto representa un riesgo real de **fuga de información (Data Leakage)** en contextos personales, corporativos y OSINT.

---

## 🚀 Características actuales

* 🔍 Extracción de metadatos usando ExifTool
* 🧠 Motor de análisis basado en reglas (rule-based detection)
* ⚠️ Detección de exposición de información sensible:

  * Coordenadas GPS (ubicación)
  * Software de edición (Photoshop, GIMP, etc.)
  * Timestamps (fecha de creación)
* 🔬 Análisis forense básico:
  
  * 🕒 Detección de inconsistencias temporales (CreateDate vs ModifyDate)
  * 📷 Identificación de dispositivo (Make / Model)
  * ⚠️ Detección de metadata ausente (posible sanitización)
* 🔐 Verificación de integridad:
  
  * Generación de hash SHA-256 por imagen
* 🔗 Correlación de imágenes:

  * 📷 Agrupación por dispositivo (misma cámara)
  * 📍 Identificación de imágenes con/sin GPS
  * 🔐 Detección de duplicados mediante hash
* ⚖️ Clasificación de riesgo:

  * LOW
  * MEDIUM
  * HIGH
* 📊 Reportes y exportación

  * Generación de reportes en formato JSON
  * Exportación de resultados de análisis y correlación
  * Estructura lista para integración con herramientas externas (SIEM, pipelines)
* 🛡️ Data Leakage Prevention (DLP)

  * Evaluación automática de riesgo antes de compartir imágenes
  * Clasificación de acciones:
    
    * ✅ ALLOW → Imagen segura
    * ⚠️ WARN → Riesgo moderado
    * ❌ BLOCK → Riesgo alto (posible fuga de información)
  * Identificación de razones de riesgo:
    
    * Exposición de ubicación (GPS)
    * Información de dispositivo
    * Posible edición de la imagen
  * Recomendación de sanitización de metadatos

* 📁 Análisis individual y masivo (carpetas completas)
* 🖥️ Output estructurado en consola (formato claro y legible)
* 📊 Resumen de análisis en escaneo masivo (conteo por nivel de riesgo)
* 🧼 Eliminación de metadatos (sanitización - DLP)
* 🔗 Visualización de correlaciones entre imágenes

---

## 🧪 Ejemplo de uso

### 🔍 Analizar una imagen

```bash
python main.py check path/to/image.jpg
```

### 📁 Analizar una carpeta completa

```bash
python main.py scan path/to/folder
```

### 🧼 Eliminar metadatos (prevención de fuga)

```bash
python main.py sanitize path/to/image.jpg
```

### 📊 Ejemplo de salida:

🔍 Análisis individual
```
================================================== 
[+] Imagen: image.jpg 
[!] Riesgo: HIGH 
[#] SHA-256: a3f5c9e1b7c...
-------------------------------------------------- 
Hallazgos: 
    - [CRITICAL] La imagen contiene coordenadas GPS (posible fuga de ubicación) 
    - [MEDIUM] Imagen editada con Photoshop
    - [LOW] Dispositivo detectado: Canon EOS
==================================================
```

📁 Escaneo de carpeta
```
================================================== 
RESUMEN DE ESCANEO 
================================================== 
Total de imágenes analizadas: 6 
HIGH : 2 
MEDIUM : 2 
LOW : 2 

================================================== 
CORRELACIONES DETECTADAS 
==================================================

[Dispositivos]

Canon EOS: 
  - img1.jpg 
  - img3.jpg

[Ubicación]

  - Con GPS: 3 
  - Sin GPS: 3

[Duplicados]

Hash: a3f5c9e1... 
  - img2.jpg 
  - img5.jpg
==================================================
```

📁 Escaneo con exportación JSON
```
python main.py scan path/to/folder --json report.json
```
Esto generará un archivo estructurado con:

  - Resultados por imagen
  - Clasificación de riesgo
  - Correlaciones detectadas
  - Resumen del análisis

Ejemplo de estructura:
```
{
  "generated_at": "2026-04-04T23:10:00",
  "summary": {
  "total": 3,
  "HIGH": 1,
  "MEDIUM": 1,
  "LOW": 1
 },
 "images": [...],
 "correlations": {...}
}
```
Este formato permite integrar la herramienta con sistemas externos de análisis o monitoreo.

---

🛡️ Evaluación de seguridad (modo DLP)
```
python main.py check path/to/image.jpg --dlp
```
Este modo analiza la imagen y determina si es segura para ser compartida.

🛡️ Resultado DLP
```
==================================================
EVALUACIÓN DLP
==================================================
Acción: BLOCK

Razones:
- Contiene datos de ubicación (GPS)

[!] Se recomienda eliminar metadata antes de compartir
==================================================
```

---

## 🏗️ Arquitectura

El proyecto está diseñado con separación de responsabilidades:

```
image_analysis_project/
│
├── core/
│   └── extractor.py      # Extracción de metadata (ExifTool)
│   └── analyzer.py       # Orquestación del análisis
│   └── rules.py          # Reglas de detección
│   └── risk_engine.py    # Clasificación de riesgo
│
├── services/
│   └── scanner.py        # Lógica para el escaneo de imagenes
│   └── sanitizer.py      # Eliminar los metadatos sensibles de las imagenes
│   └── correlator.py     # Correlación de las imágenes
│   └── exporter.py       # Exportación a JSON
│   └── dlp.py            # Evalución de riesgo de una imágen 
│
├── cli/
│   └── cli.py            # Linea de comandos
│   └── formatter.py.py   # Fomato en consola
│
├── utils/
│   └── hashing.py        # Calculo del hash de un archivo
│
├── venv/                 # Entorno virtual
├── main.py               # Archivo Principal
├── requirements.txt      # Dependencias
└── README.md

```

---

## ⚙️ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/tu-usuario/image-leak-detector.git
cd image-leak-detector
```

---

### 2. Crear entorno virtual

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 4. Configurar ExifTool

Descargar e instalar ExifTool y configurar la ruta en `.env`:

```
EXIFTOOL_PATH=C:\ExifTool\exiftool.exe
```

---

## 🔧 Configuración

El proyecto utiliza variables de entorno para evitar hardcoding:

* `EXIFTOOL_PATH` → ruta al ejecutable de ExifTool

---

## 🛡️ Casos de uso

* Prevención de fuga de información en imágenes
* Auditoría de archivos multimedia
* Análisis OSINT
* Concienciación en seguridad digital

### Práctico:

Antes de compartir una imagen:

```bash
python main.py check foto.jpg
```

Si el riesgo es alto:

```bash
python main.py sanitize foto.jpg
```

→ Se eliminan metadatos sensibles antes de su distribución.

---

## 🚧 Roadmap

El desarrollo de **ImageLeak Detector** está organizado en fases progresivas, enfocadas en evolucionar desde un motor de análisis básico hacia una herramienta completa de seguridad (DLP).

---

### ✅ Fase 1 — Núcleo de análisis 

* [x] Extracción de metadatos con ExifTool (JSON)
* [x] Integración robusta con subprocess (manejo de errores y timeout)
* [x] Motor de detección basado en reglas
* [x] Reglas implementadas:

  * [x] Detección de coordenadas GPS
  * [x] Detección de software de edición
  * [x] Detección de timestamps
* [x] Motor de clasificación de riesgo (LOW / MEDIUM / HIGH)
* [x] Ejecución básica desde CLI (`main.py`)
* [x] Validación de rutas de entrada

---

### 🚧 Fase 2 — Usabilidad como herramienta 

* [x] CLI profesional:

  * [x] `check` → analizar una imagen
  * [x] `scan` → analizar carpeta completa
  * [x] `sanitize` → eliminar metadata sensible
* [x] Módulo `scanner.py` para análisis masivo
* [x] Módulo `sanitizer.py` para limpieza de metadatos
* [x] Output estructurado en consola (formato claro y legible)
* [x] Manejo de errores mejorado y mensajes consistentes

---

### 🔧 Fase 3 — Análisis avanzado de seguridad

* [x] Detección de inconsistencias temporales:

  * CreateDate vs ModifyDate
* [x] Fingerprinting de dispositivo (Make, Model)
* [x] Generación de hashes (SHA-256) para integridad
* [x] Detección de metadata sospechosa o incompleta
* [x] Correlación de imágenes:

  * [x] Agrupación por dispositivo (Make, Model)
  * [x] Identificación de imágenes con/sin GPS
  * [x] Detección de duplicados por hash (SHA-256)


---

### 📊 Fase 4 — Reportes y análisis forense

* [ ] Generación de reportes:

  * [x] JSON
  * [ ] HTML estructurado
* [x] Resumen de riesgos por lote de imágenes
* [x] Generación de correlaciones para análisis forense
* [ ] Identificación de imágenes críticas
* [ ] Exportación de hallazgos para auditoría

---

### 🛡️ Fase 5 — Enfoque DLP (Data Leakage Prevention)

* [x] Evaluación DLP (ALLOW / WARN / BLOCK)
* [x] Recomendación de sanitización basada en riesgo
* [ ] Modo “pre-compartir”:

  * Validación antes de subir imágenes
* [ ] Sanitización automática de metadata
* [ ] Configuración de políticas de seguridad:

  * Bloquear imágenes con GPS
* [ ] Sistema de reglas configurable

---

### 🔮 Fase 6 — Funcionalidades avanzadas (futuro)

* [ ] Detección de esteganografía (integración con herramientas externas)
* [ ] Visualización de coordenadas en mapa
* [ ] Integración con pipelines (CI/CD)
* [ ] API REST para integración con otros sistemas
* [ ] Interfaz gráfica avanzada (opcional)

---

## 🎯 Objetivo final

Convertir ImageLeak Detector en una herramienta de seguridad capaz de:

* Detectar fugas de información en imágenes
* Clasificar automáticamente el nivel de riesgo
* Prevenir la exposición de datos sensibles antes de compartir archivos


---

## ⚠️ Limitaciones

* No detecta aún esteganografía
* No analiza contenido visual (solo metadata)
* Dependencia externa de ExifTool

---

## 🧠 Enfoque de seguridad

Esta herramienta se enfoca en:

* Data Leakage Prevention (DLP)
* Análisis forense básico
* Seguridad de la información

---


## ⚡ Nota

Este proyecto está en evolución activa hacia una herramienta completa de seguridad enfocada en análisis de imágenes.
