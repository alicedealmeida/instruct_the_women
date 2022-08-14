class Cliente:
    def __init__(self, nome, tel, renda_mensal, genero):
        self._nome = nome.title()
        self._tel = tel
        self._renda_mensal = renda_mensal
        self._genero = genero
        self._cheque_especial = False

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, tel):
        self._tel = tel

    @property
    def renda_mensal(self):
        return self._renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, renda):
        self._renda_mensal = renda

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, genero):
        self._genero = genero

    def concede_cheque_especial(self):
        if self._genero == 'F':
            self._cheque_especial = True
            print(f'Cheque especial concedido à cliente {self._nome} no valor de {self._renda_mensal}.')
        else:
            print(f'O cliente {self._nome} não possui direito à cheque especial.')

    def __str__(self):
        return f'Nome: {self._nome} - Telefone: {self._tel} - Renda Mensal: {self._renda_mensal} - Gênero: {self._genero} - ' \
               f'Possui cheque especial?: {self._cheque_especial}'


class ContaCorrente:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular = titular

    def __tem_cheque_especial(self):
        return self._titular._cheque_especial

    def saca(self, valor):
        if self.__tem_cheque_especial():
            if self._saldo + self._titular._renda_mensal >= valor:
                self._saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso.')
            else:
                print(f'Limite de saque atingido!')
        else:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso.')
            else:
                print(f'Limite de saque atingido!')

    def deposita(self, valor):
        self._saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso.')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)  # destino é outro objeto da classe Conta
        # destino = objeto tipo Conta / titular = objeto tipo Cliente e atributo do objeto Conta / nome = atributo
        # objeto Cliente
        print(f'Transferência de R${valor} para a conta de {destino.titular._nome} realizada com sucesso.')

    def __str__(self):
        return f'Titular da conta: {self._titular._nome} - Saldo: {self._saldo}'


class ContaConjunta(ContaCorrente):  # Herança
    def __init__(self, _titular, _saldo):
        super().__init__(_titular, _saldo)
        self.qtde_titulares = len(_titular)

    def media_rendas(self):
        renda_total = 0
        for pessoa in self.titular:
            renda_total += pessoa._renda_mensal
        return renda_total / self.qtde_titulares

    def __tem_cheque_especial(self):  # Polimofirsmo, pois sobrescreve o método da classe mãe
        for pessoa in self.titular:
            if pessoa._cheque_especial == 'True':  # existe algum titular com cheque especial?
                return True
            else:
                return False

    def saca(self, valor):  # Polimorfismo - agora usa a média das rendas e não uma só renda na condição
        if self.__tem_cheque_especial():
            if self._saldo + self.media_rendas() >= valor:
                self._saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso.')
            else:
                print(f'Limite de saque atingido!')
        else:
            if self._saldo >= valor:
                self._saldo -= valor
                print(f'Saque de R${valor} efetuado com sucesso.')
            else:
                print(f'Limite de saque atingido.')

    def __str__(self):
        return f'Titulares da conta: {self._titular[0]._nome} - Saldo: {self._saldo}'


# ************* TESTE COM CONTAS INDIVIDUAIS *************

arnaldo = Cliente('Arnaldo', 41987875454, 1500.0, 'M')
claudia = Cliente('Cláudia', 48565879643, 2000.0, 'F')

print(claudia.nome)  # usando o getter
claudia.nome = 'claudia silva'  # usando o setter

claudia.concede_cheque_especial()

arnaldo.concede_cheque_especial()  # teste para não conceder cheque à cliente homem

conta_claudia = ContaCorrente(claudia, 500)
conta_claudia.saca(2500)  # permite mulher sacar valores que deixam a sua conta com valor negativo até -renda_mensal.
conta_claudia.saca(1)  # teste de limite de saque atingido para cliente mulher
print(conta_claudia)
print(claudia)

conta_arnaldo = ContaCorrente(arnaldo, 100)
conta_arnaldo.saca(50)
conta_arnaldo.saca(51)  # não permite cliente homem utilizar cheque especial
print(conta_arnaldo)
print(arnaldo)

conta_claudia.deposita(2100)  # tirando a conta do vermelho
print(conta_claudia)

conta_claudia.transfere(50, conta_arnaldo)
print(conta_claudia)
print(conta_arnaldo)

# ************* TESTE COM CONTAS CONJUNTAS *************
# ************* Caso 1 - Cliente homem e mulher *************

renato = Cliente('renato', 41987875454, 2000.0, 'M')
roberta = Cliente('roberta', 48565879643, 3000.0, 'F')

renato.concede_cheque_especial()  # não pode conceder

roberta.concede_cheque_especial()

conta_casal_1 = ContaConjunta([renato, roberta], 1000)

# deve permitir uso de cheque especial pois um dos titulares é mulher
# valor limite do saldo é a média da renda dos titulares, nesse caso tem que ser = -2500

conta_casal_1.saca(1000)
print(conta_casal_1)

conta_casal_1.saca(2500)
print(conta_casal_1)

conta_casal_1.saca(1)  # não permite sacar além do cheque especial

# ************* Caso 2 - Apenas clientes homens *************

vanderlei = Cliente('vanderlei', 41987875454, 2000.0, 'M')
odilon = Cliente('odilon', 48565879643, 3000.0, 'M')

vanderlei.concede_cheque_especial()  # não pode conceder

odilon.concede_cheque_especial()  # não pode conceder

conta_casal_2 = ContaConjunta([vanderlei, odilon], 1000)

conta_casal_2.saca(1000)
print(conta_casal_2)

# não deve permitir uso de cheque especial pois ambos os titulares são homens

conta_casal_2.saca(1)
print(conta_casal_2)
