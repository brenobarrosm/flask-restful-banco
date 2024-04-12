from conta_corrente.services.ContaCorrenteService import ContaCorrenteService


class CreditoService:

    __service__ = ContaCorrenteService()

    def creditar(self, id, valor):
        for conta in self.__service__.buscar_contas():
            if conta['id'] == id:
                conta['saldo'] += valor
