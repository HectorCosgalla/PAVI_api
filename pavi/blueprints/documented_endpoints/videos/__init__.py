from flask import request
from flask_restplus import Namespace, Resource, fields, reqparse, Api
from werkzeug.datastructures import FileStorage
from http import HTTPStatus

namespace = Namespace('video', 'Video processing endpoint')

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
    @namespace.expect(video_model)
    @namespace.marshal_with(video_model, code=HTTPStatus.CREATED)
    def post(self):
        '''Añade y procesa un video en la plataforma'''

        uploaded_file = args['file']  # This is FileStorage instance
        url = process_video(uploaded_file)

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return {'url:', url}, 201