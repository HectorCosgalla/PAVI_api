import json

from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse, Api
from werkzeug.datastructures import FileStorage
from http import HTTPStatus

from pavi.config import Config
from pavi.util.process_video_utils import save_uploaded_video
from pavi.util.service_utils import send_to_service
from pavi.app import db_client

from bson import json_util

namespace = Namespace('videos', 'Video processing endpoint')

upload_parser = namespace.parser()
upload_parser.add_argument('video', location='files', type=FileStorage, required=True)
upload_parser.add_argument('algorithm', location='form', required=True, default='yolov4')

video_get = namespace.parser()
video_get.add_argument('video_id', required=True)

@namespace.route('')
class entities(Resource):
    '''Get entities list and create new entities'''

    @namespace.response(500, 'Internal Server error')
    @namespace.response(200, 'Get data sucessfully')
    @namespace.expect(video_get)
    #@namespace.marshal_list_with(video_list_model)
    def get(self):
        '''Regresa los videos procesados'''
        args = video_get.parse_args()
        result = db_client.get_by_field(Config.get('db_collection'), 'filename', args['video_id'])

        return json.loads(json_util.dumps(result))

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.response(201, 'Video uploaded sucessfully')
    @namespace.expect(upload_parser)
    def post(self):
        '''Añade y procesa un video en la plataforma'''
        args = upload_parser.parse_args()
        video_path = save_uploaded_video(args['video'], Config.get('upload_folder'))
        algo = args['algorithm']
        url = send_to_service(algo, video_path)
        return {'url': url}, 201