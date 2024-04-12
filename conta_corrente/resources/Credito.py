from flask import jsonify
from flask_restful import Resource, reqparse

from conta_corrente.services.CreditoService import CreditoService
class Credito(Resource):
    __service__ = CreditoService()

    parser = reqparse.RequestParser()
    parser.add_argument(
        'valor',
        type=float,
        required=True,
        help='Informe uma valor para ser debitado na conta.'
    )

    def put(self, id):
        jsonData = Credito.parser.parse_args()
        self.__service__.creditar(id, jsonData['valor'])
        return jsonify({'valor': "%.2f" % jsonData['valor']})

