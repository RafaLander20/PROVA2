#Aluno: Rafael Lopes Moraes
#Matrícula: 202017740028
d=5


class Contatos():
    def _init_(self):
        self.nome = None
        self.email = None
        self.telefone = None

    def transforma_em_dicionario(self):
        contato = {}  # dicionario
        contato["nome"] = self.nome
        contato["email"] = self.email
        contato["telefone"] = self.telefone
        return contato

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_email(self):
        return self.email

    def set_email(self, novo_email):
        self.email = novo_email

    def get_telefone(self):
        return self.email

    def set_telefone(self, novo_telefone):
        self.telefone = novo_telefone


class Agenda():

    def AdicionarContato(self, objeto, contatos):
        contatos.append(objeto)  # seleciono onde quero adicionar
        print('Adicionado com sucesso!')

    def listar(self, contatos):
        for index, contatos in enumerate(contatos):
            print("Contato " + str(index) + ":")
            print("Nome completo: " + contatos["nome"])
            print("Email: " + contatos["email"])
            print("Telefone: " + contatos["telefone"])

    def buscar(self, contatos):
        termo = input("Digite o termo que você gostaria de buscar: ")
        for index, contatos in enumerate(contatos):
            if (contatos['nome'].find(termo) + contatos['email'].find(termo) + contatos[
                'telefone'].find(termo)) >= -2:
                print("Contato " + str(index) + ":")
                print("Nome completo: " + contatos["nome"])
                print("Email: " + contatos["email"])
                print("Telefone: " + contatos["telefone"])

    def editar(self, contatos):
        print("Escolha o contato que você gostaria de editar:")
        self.listar(contatos)
        id_contato = int(input("Contato para editar: "))
        novoNome = input("Novo valor para o Nome " + contatos[id_contato]["nome"] + ": ")
        if novoNome != "":
            contatos[id_contato]["nome"] = novoNome

        novoEmail = input("Novo valor para o Email " + contatos[id_contato]["email"] + ": ")
        if novoEmail != "":
            contatos[id_contato]["email"] = novoEmail

        novoTelefone = input("Novo valor para o Telefone " + contatos[id_contato]["telefone"] + ": ")
        if novoTelefone != "":
            contatos[id_contato]["telefone"] = novoTelefone

    def apagar(self, contatos):
        print("Escolha o contato que você gostaria de apagar:")
        self.listar(contatos)
        id_contato = int(input("Contato para apagar: "))
        del contatos[id_contato]


def menu():
    opcao = None  # null, void
    a = Agenda()
    contatos = []
    while opcao != "6":

        print("Escolha uma das opções abaixo:")
        print("1 - Incluir contato")
        print("2 - Buscar contato")
        print("3 - Editar contato")
        print("4 - Excluir contato")
        print("5 - Listar contatos")
        print("6 - Sair")

        opcao = input("Opção desejada: ")

        if opcao == "1":
            objeto_contato = Contatos()

            objeto_contato.set_nome(input('Digite o nome:'))
            objeto_contato.set_email(input('Digite o email:'))
            objeto_contato.set_telefone(input('Digite o telefone:'))

            a.AdicionarContato(objeto_contato.transforma_em_dicionario(), contatos)
        elif opcao == "2":
            a.buscar(contatos)
        elif opcao == "3":
            a.editar(contatos)
        elif opcao == "4":
            a.apagar(contatos)
        elif opcao == "5":
            a.listar(contatos)
            # print(objeto_contato.transforma_em_dicionario())#
        else:
            print("Opção inválida, tente novamente!")


menu()