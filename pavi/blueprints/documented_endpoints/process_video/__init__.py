from flask import request
from flask_restplus import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('process_video', 'Video processing endpoint')

video_model = namespace.model('Video', {
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
        '''List with all the entities'''
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
        '''Create a new entity'''

        if request.json['name'] == 'Entity name':
            namespace.abort(400, 'Entity with the given name already exists')

        return entity_example, 201