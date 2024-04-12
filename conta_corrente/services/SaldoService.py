from conta_corrente.services.ContaCorrenteService import ContaCorrenteService


class SaldoService:

    __service__ = ContaCorrenteService()

    def consulta_saldo(self, id):

        for conta in self.__service__.buscar_contas():
            if conta['id'] == id:
                return conta['saldo']
