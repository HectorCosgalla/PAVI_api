# blueprints/documented_endpoints/__init__.py
from flask import Blueprint
from flask_restplus import Api

from pavi.blueprints.documented_endpoints.videos import namespace as videos_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='PAVI',
    version='0.1.0',
    description='La Plataforma de Análisis de Video Inteligente (PAVI) es un sistema utilizado para detección, clasificación y conteo de objetos en videos.\nFunciones principales:\n- Procesar videos utilizando alguno de los algoritmos soportados.* \n- Mantener una base de datos con los resultados del procesamiento de los videos. \n- Mostrar los resultados de los videos procesados en una interfaz amigable.\n\n*Algoritmos soportados al momento: YOLOv3, OpenVINO Pedestrian Tracker.',
    doc='/doc'
)

api_extension.add_namespace(videos_ns)