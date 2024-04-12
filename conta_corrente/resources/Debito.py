from flask import jsonify
from flask_restful import Resource, reqparse

from conta_corrente.services.DebitoService import DebitoService
class Debito(Resource):
    __service__ = DebitoService()

    parser = reqparse.RequestParser()
    parser.add_argument(
        'valor',
        type=float,
        required=True,
        help='Informe uma valor para ser debitado na conta.'
    )

    def put(self, id):
        jsonData = Debito.parser.parse_args()
        self.__service__.debitar(id, jsonData['valor'])
        return jsonify({'valor': "%.2f" % jsonData['valor']})

