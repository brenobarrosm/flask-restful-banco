from flask import Flask, jsonify
from flask_restful import Api

from conta_corrente.resources.ContaCorrente import ContaCorrente
from conta_corrente.resources.Saldo import Saldo
from conta_corrente.resources.Debito import Debito
from conta_corrente.resources.Credito import Credito


def create_app():

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(ContaCorrente, '/contas')
    api.add_resource(Saldo, '/contas/<int:id>/saldo')
    api.add_resource(Debito, '/contas/<int:id>/debito')
    api.add_resource(Credito, '/contas/<int:id>/credito')

    if __name__ == '__main__':
        app.run()

    return app
