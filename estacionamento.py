class Estacionamento:
    total_vagas_de_carro = 5
    total_vagas_de_moto = 5

    def __init__(self):
        self.vagas_de_carro = {1: 'livre', 2: 'livre', 3: 'livre', 4: 'livre', 5: 'livre'}
        self.vagas_de_moto = {6: 'livre', 7: 'livre', 8: 'livre', 9: 'livre', 10: 'livre'}

    def exibe_vagas_livres(self):
        count_vagas_carro = 0
        count_vagas_moto = 0
        for vaga in self.vagas_de_carro:
            if vagas_de_carro[vaga] == 'livre':
                count_vagas_carro += 1
        for vaga in self.vagas_de_moto:
            if vagas_de_moto[vaga] == 'livre':
                count_vagas_moto += 1
        print(f'\nVagas de carro livres: {count_vagas_carro}')
        print(f'Vagas de moto livres: {count_vagas_moto}')

    def __str__(self):
        return f'\nVagas de carro: {self.vagas_de_carro} \n' \
               f'Vagas de moto: {self.vagas_de_moto} \n\n'


class Veiculo:
    def __init__(self, placa, estacionado):
        self.placa = placa
        self.estacionado = estacionado


class Carro(Veiculo):
    def __init__(self, placa, estacionado):  # Sobrescrevendo o construtor da classe mãe
        super().__init__(placa, estacionado)  # Herdando os métodos da classe mãe

    def estacionar(self, vagas_de_carro):
        if 'livre' in vagas_de_carro.values():
            for vaga in vagas_de_carro:
                if vagas_de_carro[vaga] == 'livre':
                    vagas_de_carro[vaga] = self.placa
                    self.estacionado = True
                    break
        else:
            print(f'\nO estacionamento está lotado para carros.')

    def desocupar_vaga(self, vagas):
        if self.placa in vagas.values():
            for vaga in vagas:
                if vagas[vaga] == self.placa:
                    vagas[vaga] = 'livre'
                    self.estacionado = False
                    break
        else:
            print(f'\nEste carro não está estacionado nessas vagas!')


class Moto(Veiculo):
    def __init__(self, placa, estacionado):  # Sobrescrevendo o construtor da classe mãe
        super().__init__(placa, estacionado)  # Herdando os métodos da classe mãe

    def estacionar_nas_vagas_de_moto(self, vagas_de_moto):
        if 'livre' in vagas_de_moto.values():
            for vaga in vagas_de_moto:
                if vagas_de_moto[vaga] == 'livre':
                    vagas_de_moto[vaga] = self.placa
                    self.estacionado = True
                    break
        else:
            print(f'\nAs vagas de moto estão lotadas. Estacione nas vagas para carro')

    def estacionar_nas_vagas_de_carro(self, vagas_de_moto, vagas_de_carro):
        if 'livre' not in vagas_de_moto.values():
            if 'livre' in vagas_de_carro.values():
                for vaga in vagas_de_carro:
                    if vagas_de_carro[vaga] == 'livre':
                        vagas_de_carro[vaga] = self.placa
                        self.estacionado = True
                        break
            else:
                print('As vagas de carro também estão lotadas!')
        else:
            print('Não é permitido estacionar nas vagas de carro se ainda existem vagas livres para motos!')

    def desocupar_vaga(self, vagas):
        if self.placa in vagas.values():
            for vaga in vagas:
                if vagas[vaga] == self.placa:
                    vagas[vaga] = 'livre'
                    self.estacionado = False
                    break
        else:
            print(f'\nEsta moto não está estacionada nessas vagas!')


estacionamento1 = Estacionamento()

vagas_de_carro = estacionamento1.vagas_de_carro
vagas_de_moto = estacionamento1.vagas_de_moto

gol = Carro('ABC1234', False)

gol.estacionar(vagas_de_carro)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

gol.desocupar_vaga(vagas_de_carro)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

motinho = Moto('FG56', False)
motinho.estacionar_nas_vagas_de_moto(vagas_de_moto)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

# Não irá permitir estacionar nas vagas de carro, pois ainda há vagas de moto livres
motinho.estacionar_nas_vagas_de_carro(vagas_de_moto, vagas_de_carro)

yamaha = Moto('5645', False)
yamaha.estacionar_nas_vagas_de_moto(vagas_de_moto)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

harley = Moto('5464', False)
harley.estacionar_nas_vagas_de_moto(vagas_de_moto)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

scooter = Moto('222', False)
scooter.estacionar_nas_vagas_de_moto(vagas_de_moto)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

suzuki = Moto('222', False)
suzuki.estacionar_nas_vagas_de_moto(vagas_de_moto)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

motinho2 = Moto('(moto)333', False)
motinho2.estacionar_nas_vagas_de_carro(vagas_de_moto, vagas_de_carro)
estacionamento1.exibe_vagas_livres()
print(estacionamento1)

motinho3 = Moto('754', False)
motinho3.desocupar_vaga(vagas_de_moto)  # Irá retornar msg de que veículo não está estacionado