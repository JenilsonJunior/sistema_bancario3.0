import textwrap

class PessoaFisica:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Transacao:
    def __init__(self, valor):
        self.valor = valor

class Deposito(Transacao):
    def __init__(self, valor):
        super().__init__(valor)

class Saque(Transacao):
    def __init__(self, valor):
        super().__init__(valor)

class Conta:
    def __init__(self, agencia, numero_conta, cliente):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._cliente = cliente
        self._saldo = 0
        self._limite = 500
        self._historico = []

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor
        self._historico.append(Deposito(valor))
        print("\n = Depósito realizado com sucesso! =")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo + self._limite:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor
        self._historico.append(Saque(valor))
        print("\n Saque realizado com sucesso!")

    def imprimir_historico(self):
        print("\n================ HISTÓRICO ================")
        if not self._historico:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in self._historico:
                if isinstance(transacao, Deposito):
                    print(f"Depósito:\tR$ {transacao.valor:.2f}")
                elif isinstance(transacao, Saque):
                    print(f"Saque:\t\tR$ {transacao.valor:.2f}")
        print(f"\nSaldo:\t\tR$ {self._saldo:.2f}")
        print("===========================================")


def menu():
    menu_text = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tImprimir Historico
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair
    ====================================== 
    : """
    return input(textwrap.dedent(menu_text))

def criar_usuario():
    nome = input("Informe o nome completo: ")
    cpf = input("Digite o CPF (somente números): ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro - nro - bairro - cidade/sigla estado): ")
    return PessoaFisica(nome, cpf, data_nascimento, endereco)

def criar_conta(agencia, numero_conta, cliente):
    return Conta(agencia, numero_conta, cliente)

def listar_contas(contas):
    print("\n=== Lista de Contas ===")
    for conta in contas:
        print(f"Agência: {conta._agencia}, C/C: {conta._numero_conta}, Titular: {conta._cliente.nome}")

def main():
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        try:
            opcao = menu()

            if opcao == "1":
                valor = float(input("Informe o valor do depósito: "))
                if not contas:
                    print("Nenhuma conta encontrada. Crie uma conta primeiro.")
                else:
                    numero_conta = int(input("Informe o número da conta: "))
                    conta = next((c for c in contas if c._numero_conta == numero_conta), None)
                    if conta:
                        conta.depositar(valor)
                    else:
                        print("Conta não encontrada.")
               
            elif opcao == "2":
                valor = float(input("Informe o valor do saque: "))
                if not contas:
                    print("Nenhuma conta encontrada. Crie uma conta primeiro.")
                else:
                    numero_conta = int(input("Informe o número da conta: "))
                    conta = next((c for c in contas if c._numero_conta == numero_conta), None)
                    if conta:
                        conta.sacar(valor)
                    else:
                        print("Conta não encontrada.")

            elif opcao == "3":
                if not contas:
                    print("Nenhuma conta encontrada. Crie uma conta primeiro.")
                else:
                    numero_conta = int(input("Informe o número da conta: "))
                    conta = next((c for c in contas if c._numero_conta == numero_conta), None)
                    if conta:
                        conta.imprimir_historico()
                    else:
                        print("Conta não encontrada.")

            elif opcao == "4":
                numero_conta = len(contas) + 1
                cliente = criar_usuario()
                conta = criar_conta(AGENCIA, numero_conta, cliente)
                contas.append(conta)
                print("\n = Conta criada com sucesso! =")
            
            elif opcao == "5":
                if not contas:
                    print("Nenhuma conta encontrada.")
                else:
                    listar_contas(contas)

            elif opcao == "6":
                usuario = criar_usuario()
                usuarios.append(usuario)
                print(" = Usuário criado com sucesso! =")

            elif opcao == "0":
                print("Obrigado por utilizar nossa instituição bancária!")
                print("Saindo...")
                break

            else:
                print("Opção inválida. Por favor, selecione uma opção válida!")
        
        except ValueError as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
