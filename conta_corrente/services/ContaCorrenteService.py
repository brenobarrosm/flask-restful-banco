from conta_corrente.models.ContaCorrenteModel import ContaCorrenteModel


class ContaCorrenteService:
    
    __model__ = ContaCorrenteModel()

    def criar_conta(self, **kwargs):

        contasExistentes = self.__model__.contas

        if len(contasExistentes) == 0:
            id = 1
        else:
            id = (contasExistentes[-1].get('id')) + 1

        contasExistentes.append({
            "id": id,
            "banco": kwargs["banco"],
            "agencia": kwargs["agencia"],
            "conta": kwargs["conta"],
            "saldo": 0
        })

    def buscar_contas(self):
        contasExistentes = self.__model__.contas
        return contasExistentes
