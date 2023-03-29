'''
Nome: Konrrado Tulio Sicalski
Curso: Análise e Desenvolvimento de sistemas
'''

while True:
    print("Bem Vindo ao sistema de cadastro. Selecione o número correspondente à opção desejada (apenas o número). \nApós, pressione a tecla ENTER")
    opcao = input(" 1 Estudante\n 2 Disciplina\n 3 Professor\n 4 Turma\n 5 Ma1trícula\n 0 Sair\n")
    print("Você selecionou: " + opcao)
    if opcao == "1": #mantive em str, para evitar conversões, o que seria mais recomendável?
        alunos = []
        while True:
            print("Olá, Estudante! Selecione o número correspondente à opção desejada (apenas o número). \nApós, pressione a tecla ENTER")
            opcao = input(" 1 Listar\n 2 Incluir\n 3 Alterar\n 4 Excluir\n 0 retornar ao menu principal\n")
            print("Você selecionou: " + opcao)
            if opcao == "1" and alunos == []:
                print("\n*** Não há alunos cadastrados ***\n")
            elif opcao == "1":
                print("\n *** Listagem ***\n")
                print(sorted(alunos))
                print("")
            elif opcao == "2":
               nome = input("Digite o nome do esudante: ")
               alunos.append(nome)
               print("cadastrado!")
            elif opcao == "3" or opcao == "4":
                print("\n *** Em desenvolvimento ***\n")
            elif opcao == "0":
                break
            else:
                print("\n *** Opção inválida ***\n")
    elif opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
        print("\n *** Em desenvolvimento ***\n")
    elif opcao == "0":
         print("\n *** programa encerrado\n ***")
         break
    else:
        print("Opção inválida")