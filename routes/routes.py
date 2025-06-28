from flask import Blueprint, request, jsonify
from Models import Musica
from db import db

musica_bp = Blueprint('musica_bp', __name__)

@musica_bp.route('/api/spotify/canciones', methods=['GET'])
def obtener_canciones_activas():
    canciones = Musica.query.filter_by(activo=True).all()
    resultado = [{
        'id': c.id,
        'cancion': c.cancion,
        'artista': c.artista,
        'album': c.album,
        'anio': c.anio,
        'duracion': c.duracion,
        'fecha_lanzamiento': c.fecha_lanzamiento.isoformat() if c.fecha_lanzamiento else None,
        'hora_estreno': c.hora_estreno.isoformat() if c.hora_estreno else None,
        'descripcion': c.descripcion,
        'email_contacto': c.email_contacto
    } for c in canciones]
    return jsonify(resultado), 200

@musica_bp.route('/api/spotify/canciones/<int:id>', methods=['DELETE'])
def baja_logica_cancion(id):
    cancion = Musica.query.get(id)
    if not cancion or not cancion.activo:
        return jsonify({'mensaje': 'Canción no encontrada o ya inactiva'}), 404

    cancion.activo = False
    db.session.commit()
    return jsonify({'mensaje': 'Canción dada de baja correctamente'}), 200

@musica_bp.route('/api/spotify/canciones/clasificadas', methods=['GET'])
def clasificar_canciones():
    canciones = Musica.query.filter_by(activo=True).all()
    clasificacion = {
        'Corta': [],
        'Media': [],
        'Larga': []
    }

    for c in canciones:
        dur = c.duracion
        data = {
            'id': c.id,
            'cancion': c.cancion,
            'artista': c.artista,
            'duracion': dur
        }
        if dur < 180:
            clasificacion['Corta'].append(data)
        elif 180 <= dur <= 240:
            clasificacion['Media'].append(data)
        elif dur > 340:
            clasificacion['Larga'].append(data)

    return jsonify(clasificacion), 200
