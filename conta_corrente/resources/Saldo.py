from flask import jsonify
from flask_restful import Resource, reqparse

from conta_corrente.services.SaldoService import SaldoService

class Saldo(Resource):

    __service__ = SaldoService()

    def get(self, id):

        saldo = self.__service__.consulta_saldo(id)

        if saldo is not None:
            return jsonify({'valor': "%.2f" % saldo})

        return jsonify({'message': 'Conta não encontrada.'})

