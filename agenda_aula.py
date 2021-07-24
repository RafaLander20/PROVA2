#agenda: lista
#contato: dicionario
agenda = [] #lista

class Agenda():

    

    def incluir(agenda):
        contato = {} #dicionario
        contato["nome"] = input("Digite o Nome Completo: ")
        contato["email"] = input("Digite o Email: ")
        contato["telefone"] = input("Digite o Telefone: ")
        #adiciona um contato a agenda
        agenda.append(contato)

    def listar(agenda):
        for index, contato in enumerate(agenda):
            print("Contato "+str(index)+":")
            print("Nome completo: "+contato["nome"])
            print("Email: "+contato["email"])
            print("Telefone: "+contato["telefone"])

    def buscar(agenda):
        termo = input("Digite o termo que você gostaria de buscar: ")
        for index, contato in enumerate(agenda):
            if (contato['nome'].find(termo) + contato['email'].find(termo) + contato['telefone'].find(termo))>=-2:
                print("Contato "+str(index)+":")
                print("Nome completo: "+contato["nome"])
                print("Email: "+contato["email"])
                print("Telefone: "+contato["telefone"])

    def editar(agenda):
        print("Escolha o contato que você gostaria de editar:")
        listar(agenda)
        id_contato = int(input("Contato para editar: "))
        novoNome = input("Novo valor para o Nome "+agenda[id_contato]["nome"]+": ")
        if novoNome != "":
            agenda[id_contato]["nome"] = novoNome
        
        novoEmail = input("Novo valor para o Email "+agenda[id_contato]["email"]+": ")
        if novoEmail != "":
            agenda[id_contato]["email"] = novoEmail

        novoTelefone = input("Novo valor para o Telefone "+agenda[id_contato]["telefone"]+": ")
        if novoTelefone != "":
            agenda[id_contato]["telefone"] = novoTelefone

    def apagar(agenda):
        print("Escolha o contato que você gostaria de apagar:")
        listar(agenda)
        id_contato = int(input("Contato para editar: "))
        del agenda[id_contato]

    def menu():
        opcao = None #null, void
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
                incluir(agenda)
            elif opcao == "2":
                buscar(agenda)
            elif opcao == "3":
                editar(agenda)
            elif opcao == "4":
                apagar(agenda)
            elif opcao == "5":
                listar(agenda)
            elif opcao == "6":
                print("Bye bye :)")
            else:
                print("Opção inválida, tente novamente!")

    #Execução
    menu()
