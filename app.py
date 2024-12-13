import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from colorthief import ColorThief
import requests
from io import BytesIO
from urllib.parse import urlparse

app = Flask(__name__)
CORS(app)

# Ruta para obtener el color dominante de una imagen por URL
@app.route('/get_dominant_color', methods=['GET'])
def get_dominant_color():
    image_url = request.args.get('imageUrl')

    if not image_url:
        return jsonify({'error': 'imageUrl parameter is required'}), 400

    # Validación básica de la URL
    parsed_url = urlparse(image_url)
    if not parsed_url.scheme in ['http', 'https']:
        return jsonify({'error': 'Invalid URL format. Only HTTP and HTTPS URLs are allowed'}), 400

    try:
        # Realizamos la solicitud HTTP para obtener la imagen desde la URL
        response = requests.get(image_url)

        # Verificamos si la solicitud fue exitosa
        if response.status_code != 200:
            return jsonify({'error': f'Failed to fetch the image from the provided URL, status code: {response.status_code}'}), 400

        # Cargamos la imagen en ColorThief
        image_data = BytesIO(response.content)
        color_thief = ColorThief(image_data)

        # Obtenemos el color dominante
        dominant_color = color_thief.get_color(quality=1)  # Calidad del color dominante (puedes ajustarlo)
        palette = color_thief.get_palette(color_count=6)  # Opcional: obtener una paleta de colores

        # Devolvemos el color dominante en formato RGB y la paleta
        return jsonify({
            'dominantColor': dominant_color,
        })

    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Request error: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
