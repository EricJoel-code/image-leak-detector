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
* 🧠 Motor de análisis basado en reglas
* ⚠️ Detección de:

  * Coordenadas GPS
  * Software de edición
  * Timestamps
* ⚖️ Clasificación de riesgo:

  * LOW
  * MEDIUM
  * HIGH

* 📁 Análisis individual y masivo (carpetas completas)
* 🧼 Eliminación de metadatos (sanitización - DLP)

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

```
[+] Imagen: image.jpg
[!] Riesgo: HIGH

Hallazgos:
- [CRITICAL] La imagen contiene coordenadas GPS (posible fuga de ubicación) 
- [MEDIUM] Imagen editada con Photoshop 
- [LOW] La imagen contiene fecha de creación
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
│
├── cli/
│   └── cli.py            # Punto de entrada 
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
* [ ] Manejo de errores mejorado y mensajes consistentes

---

### 🔧 Fase 3 — Análisis avanzado de seguridad

* [ ] Detección de inconsistencias temporales:

  * CreateDate vs ModifyDate
* [ ] Fingerprinting de dispositivo (Make, Model)
* [ ] Identificación de patrones entre imágenes
* [ ] Generación de hashes (SHA-256) para integridad
* [ ] Detección de metadata sospechosa o incompleta

---

### 📊 Fase 4 — Reportes y análisis forense

* [ ] Generación de reportes:

  * [ ] JSON
  * [ ] HTML estructurado
* [ ] Resumen de riesgos por lote de imágenes
* [ ] Identificación de imágenes críticas
* [ ] Exportación de hallazgos para auditoría

---

### 🛡️ Fase 5 — Enfoque DLP (Data Leakage Prevention)

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
