
# 📊 Proyecto Final: Scraping de Comentarios de YouTube

Este proyecto implementa un pipeline reproducible y organizado para extraer comentarios de videos en YouTube utilizando la **YouTube Data API v3**. Los comentarios se guardan en un archivo `.csv` para su posterior análisis.

## 🚀 Descripción
- Utiliza el canal de **Morat** como ejemplo.
- Busca los videos más recientes y extrae hasta **500 comentarios por video**.
- Los comentarios incluyen: ID del comentario, texto, ID del video, y título del video.
- Los datos se guardan automáticamente en el archivo `data/dataset.csv`.

## 🗂️ Estructura del Proyecto
```

proyecto-final/
├── code/
│   └── scraper.py           # Script principal del scraper
├── data/
│   └── dataset.csv          # Archivo CSV generado con comentarios
├── .env                     # Archivo con tu API Key de YouTube
├── requirements.txt         # Dependencias necesarias
└── README.md                # Este archivo

```

## 🔐 Configuración Inicial
1️⃣ Crea un archivo `.env` en el directorio raíz y agrega tu API Key:
```

YOUTUBE\_API\_KEY=TU\_CLAVE\_API

````
2️⃣ Comparte el archivo `.env.example` sin tu clave para otros usuarios.

## ⚙️ Reproducir el Entorno
1️⃣ Crea y activa un entorno virtual:
```bash
python -m venv venv
venv\Scripts\activate     # En Windows
source venv/bin/activate  # En Mac/Linux
````

2️⃣ Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Ejecución del Script

Desde el directorio raíz:

```bash
python code/scraper.py
```

## 📈 Resultados

El archivo `data/dataset.csv` contendrá al menos 500 comentarios extraídos.
Cada fila incluye:

* `comment_id`: ID del comentario
* `comment`: Texto del comentario
* `video_id`: ID del video
* `video_title`: Título del video

## 📝 Notas

* Abre el CSV con Notepad++, VSCode, o Excel importando como **UTF-8**.
* Puedes cambiar el canal objetivo modificando el valor de `channel_query` en `scraper.py`.

## 👤 Autor

**Oswaldo Casillas**
GitHub: [@OswaldoCasillas](https://github.com/OswaldoCasillas)
