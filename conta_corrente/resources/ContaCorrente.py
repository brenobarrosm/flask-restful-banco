from flask import jsonify
from flask_restful import Resource, reqparse

from conta_corrente.services.ContaCorrenteService import ContaCorrenteService


class ContaCorrente(Resource):
    __service__ = ContaCorrenteService()

    parser = reqparse.RequestParser()
    parser.add_argument(
        'banco',
        type=str,
        required=True,
        help='Você deve informar o número do Banco (ex: 072).'
    )
    parser.add_argument(
        'agencia',
        type=str,
        required=True,
        help='Você deve informar uma Agência (ex: 1738).'
    )
    parser.add_argument(
        'conta',
        type=str,
        required=True,
        help='Você deve informar o número da Conta (ex: 10789).'
    )

    def post(self):
        jsonData = ContaCorrente.parser.parse_args()
        self.__service__.criar_conta(**jsonData)
        responseData = {'id': self.__service__.buscar_contas()[-1].get('id')}
        return responseData, 201

    def get(self):
        return self.__service__.buscar_contas()
