from datetime import datetime
import pytz
from random import randint
class Tv: # classe
    def __init__(self,tamanho): # Inicalizando a classe # sem a funçao 'self' nao iremos conseguir acessar a classe
        self.cor = 'preta' # criando atributos para a classe
        self.ligada = False
        self.tamanho = tamanho
        self.canal = 'Nenhum canal selecionado' ###
        self.volume = 10 #  sem o self os atributos da classe nao irao poder ser acessados,/
        # pois sem o self o atributo vira uma variavel que so existe dentro da funcao
        self.entrada = 'Entradas detectadas hdmi/xbox/playstation/radio/Tv'

    def mudar_canal(self, novo_canal):
        self.canal = novo_canal ### voce pode chamar atributos para criar metodos em sua classe
        print(f'canal alterado para {novo_canal}')

    def ligar_tv(self):
        self.ligada = True
        print('a Tv agora esta ligada')
    def desligar_tv(self):
        self.ligada = False
        print('a tv agora esta desligada')
    def mudar_entrada(self,escolher_entrada):
        self.entrada = escolher_entrada
        print(f'voce mudou a entrada para {escolher_entrada} para voltar basta digitar a antecessora',)


'''
tv_sala = Tv(tamanho=45) # chamando a classe em uma variavel
tv_sala.cor = 'branca' # Mundado atributos da classe Tv
tv_quarto = Tv(tamanho=70)

tv_sala.cor = 'amarelo' # repare que para usar/mudar um atributo da classe nao usa o ()
tv_sala.mudar_canal('Record') # repare que para executar um metodo usamos o ()
tv_quarto.mudar_canal('disney xd')

tv_cozinha = Tv(tamanho=40)
'''

"""
Seguir o padrao de doctring PEP 257
 A classe abaixo cria o Objeto Contacorrente para gerenciar as contas dos clientes.
 Atributos:
    nome: Nome do cliente
    cpf: Cpf do cliente
    agencia: Agencia Responsavel pela conta do Cliente
    num_conta: numero da conta corrente do cliente
    saldo: Saldo Disponivel na conta do cliente
    limite: limite do Cheque especial daquele cliente
    transaçoes: historico de transçoes do cliente
    :return:
"""

class ContaCorrente:



# atributos que vale para toda a classe # atributo estatico
    @staticmethod
    def _data_hora(): # criando uma funçao ue mostra o horario em que as transaçoes foram efetuadas
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')


    def __init__(self, nome, cpf , agencia , num_conta): # criando metodos para a classe
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []


    def consultar_saldo(self):
        print(f'seu Saldo atual é de R${self._saldo:,.2f}') # formatando o método saldo

    def depositar(self, valor):
        if valor > 10000:
            print('nao deposite numeros altos para facilitar a conta')
            self.consultar_saldo()
        else:
            self._saldo += valor
            self.consultar_saldo()
            self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))# para adicionar mais de 1 item em/
            # uma lista no /
            # append basta fazer uma tupla de tuplas (())

    def _limite_conta(self): # o udernline siginifa um método não publico
        self._limite = -1000
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('voce nao possui saldo suficiente pra sacar esse valor')
            self.consultar_saldo() # voce pode chamar metodos em outros metodos
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
            self.consultar_saldo()

    def consultar_limite_chequeespecial(self):
        print(f'seu limite do chequeespecial é de R${self._limite_conta():,.2f}')

    def consultar_historico_transações(self):
        print('Historia transaçoes')
        print('valor,Saldo,Data e Hora')
        for transaçao in self._transacoes:
            print(transaçao)

    def tranferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito():

    @staticmethod
    def _data_hora():  # criando uma funçao ue mostra o horario em que as transaçoes foram efetuadas
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR


    def __init__(self, titular,conta_corrente):
        self.numero = randint(100000000000000,9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}/{}/{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self._senha = '1234'
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)
    @property #tornando o metodo senha uma propriedade(atributo) # getter and setter
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self._senha = valor
        else:
            print('nova senha invalida')

class Agencia:

    def __init__(self, telefone, cnpj , numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print(f'caixa abaixo do nivel recomendado. Caixa atual {self.caixa:,.2f}')
        else:
            print(f'Valor valido. caixa atual {self.caixa:,.2f} ')
    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor,cpf,juros))
        else:
            print(f'Emprestimo nao disponivel , dinheiro nao sufuciente , caixa atual {self.caixa:,.2f}')

    def adicionar_cliente(self,nome,cpf,patrimonio):
        self.clientes.append((nome,cpf,patrimonio))

#uma classe 'filha' da classe agencia) #subclasse de uma classe / # por isso recebe o "agencia" como parametro
                                                 


class AgenciaVirtual(Agencia):


    def __init__(self, site,telefone,cnpj):
        super().__init__(telefone,cnpj,1000) # chamando o __init__ da Superclasse 'Agencia'
        self.site = site
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor



    def sacar_paypal(self):
        self.caixa_paypal -= valor
        self.caixa

    def verificar_caixa_paypal(self):
        print(f'seu caixa no paypal é de {self.caixa_paypal:,.2f}')






class AgenciaComum(Agencia):

    def __init__(self,telefone,cnpj,):
        super().__init__(telefone,cnpj,numero=randint(1001,9999))
        self.caixa = 1000000



class AgenciaPremium(Agencia):

    def __init__(self,telefone,cnpj,):
        super().__init__(telefone,cnpj,numero=randint(1001,9999))
        self.caixa = 10000000

    def adicionar_cliente(self,nome,cpf,patrimonio): #polimorfimso,chamei  um metodo de uma classe /
    # porem com atributos diferentes
        if patrimonio > 1000000:
            super().adicionar_cliente(nome,cpf,patrimonio)
        else:
            print(f'o cliente nao tem o patrimonio minimo nescessário para entrar na Agencia premium {patrimonio:,.2f}')



















if __name__ == '__main__':

    #programa
    conta_jorje = ContaCorrente('Jorje', '111.222.333-45', 1111, 22222)
    conta_narga = ContaCorrente('narga','111.222.333-45',1111,2222)
    cartao_jorje = CartaoCredito('jorje', conta_jorje)
    print(cartao_jorje.conta_corrente._cpf)
    print(cartao_jorje.conta_corrente.nome)
    print(conta_jorje.cartoes)
    print(cartao_jorje.validade)
    print(cartao_jorje.numero)
    print(cartao_jorje.cod_seguranca)
    cartao_jorje.senha = '1212'
    print(cartao_jorje.senha)
    print('-' * 50)
    agencia1 = Agencia(22223333,2222000000000,2345)
    
    agencia1.caixa = 1000000000
    agencia1.verificar_caixa()
    agencia1.emprestar_dinheiro(15,600,0.02)
    print(agencia1.emprestimos)
    
    agencia1.adicionar_cliente('jorje',121211221,900000)
    print(agencia1.clientes)
    agencia_vitural = AgenciaVirtual('www.agenciavirtual',1111111,2211313132) # como a classe 'Agencia virtual é uma subclasse da classe agencia /
    # o init da classe agencia tambem e puchado , com isso devemos passar cpf cnpj e numero,A herança de uma classe
    
    
    agencia_vitural.verificar_caixa()
    print(agencia_vitural.clientes)
    print('-'* 50)
    agencia_comum = AgenciaComum(21312332,5343)
    agencia_comum.verificar_caixa()
    print('-'*60)
    agencia_premium = AgenciaPremium(323324432,4342432)
    agencia_premium.verificar_caixa()
    print('-'*70)
    agencia_vitural.depositar_paypal(30000)
    print(agencia_vitural.caixa)
    agencia_vitural.verificar_caixa_paypal()
    
    agencia_premium.adicionar_cliente('jorje_amado',32323232,999238932893289)
    print(agencia_premium.clientes)


