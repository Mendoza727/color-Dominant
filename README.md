# Dominant Color API

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask Version](https://img.shields.io/badge/Flask-2.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Una API para obtener el color dominante de una imagen a partir de su URL, utilizando Flask y la librería `colorthief`. 

Esta API es útil para obtener el color principal de una imagen que se puede utilizar en interfaces de usuario, análisis de imágenes, o cualquier otro caso donde el color predominante sea necesario.

## Características

- Obtiene el color dominante de una imagen a partir de una URL.
- Responde con el color dominante en formato RGB.
- Valida la URL de la imagen y maneja errores comunes.
- Utiliza la librería [ColorThief](https://github.com/fengsp/color-thief-py) para analizar la imagen y extraer el color.

## Instalación

### Requisitos

Asegúrate de tener Python 3.8 o superior instalado. También necesitarás instalar las dependencias del proyecto.

### Clonando el Repositorio

```bash
git clone https://github.com/tuusuario/dominant-color-api.git
cd dominant-color-api
```

## Instala las dependencias utilizando pip:

```bash
pip install -r requirements.txt
```
### Para iniciar la aplicación, ejecuta el siguiente comando:

```bash
python app.py
```
Esto iniciará el servidor Flask en el puerto 5000 de manera predeterminada. Ahora puedes acceder a la API localmente.

### Endpoints
```bash
GET /get_dominant_color
```
Este endpoint recibe una URL de imagen y devuelve el color dominante de la imagen.

### Parámetros de Consulta:
- imageUrl (requerido): La URL de la imagen que deseas analizar.


### Ejemplo de Solicitud:

```bash
GET http://127.0.0.1:5000/get_dominant_color?imageUrl=https://example.com/image.jpg
```
Respuesta:

```json
{
  "dominantColor": [120, 150, 200]
}
```

Errores comunes:
Si la URL proporcionada no es válida o no se puede acceder a la imagen, recibirás un error con el código de estado 400.
Si hay un error de servidor o con la solicitud de la imagen, se devolverá un error con el código de estado 500.

### Ejemplo de uso con curl
```bash
curl "http://127.0.0.1:5000/get_dominant_color?imageUrl=https://example.com/image.jpg"
```
### Licencia
Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo LICENSE para más detalles.

### Tecnologías Utilizadas
- Flask
- ColorThief
- requests

### Contribuciones
Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

- Haz un fork del repositorio.
- Crea una nueva rama (git checkout -b feature-nueva-funcionalidad).
- Haz tus cambios y haz commit de ellos (git commit -am 'Agregando nueva funcionalidad').
- Empuja tu rama (git push origin feature-nueva-funcionalidad).
- Abre un pull request.
