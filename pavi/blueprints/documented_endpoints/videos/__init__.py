from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse, Api
from werkzeug.datastructures import FileStorage
from http import HTTPStatus
from pavi.util.service_utils import send_to_service

namespace = Namespace('videos', 'Video processing endpoint')

upload_parser = namespace.parser()
upload_parser.add_argument('algorithm', location='form', type='string', required=True, default='yolov4')
upload_parser.add_argument('video', location='files', type=FileStorage, required=True)
                           
video_model = namespace.model('videoid', {
    'id': fields.String(
        readonly=True,
        description='Video identifier'
    )
})

video_list_model = namespace.model('VideoList', {
    'video_list': fields.Nested(
        video_model,
        description='Lista de videos',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Numero total de videos',
    ),
})

@namespace.route('')
class entities(Resource):
    '''Get entities list and create new entities'''

    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(video_list_model)
    def get(self):
        '''Regresa los videos procesados'''
        #entity_list = [entity_example]

        return {
            'entities': video_list_model,
            'total_records': len(video_list_model)
        }

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(upload_parser)
    def post(self):
        '''Añade y procesa un video en la plataforma'''
        args = upload_parser.parse_args()
        video_path = args['video']
        algo = args['algorithm']
        print(video_path)
        print(algo)
        url = send_to_service(algo, video_path)
        return {'url': url}, 201