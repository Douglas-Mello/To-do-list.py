tarefa = list()
while True:
    print("===  Menu de opções:  ====")
    print("1.Adicionar Tarefa \n2.Ver tarefas\n3.Conclui uma tarefa\n4.Remover tarefa\n5.Sair")
    opc=int(input('Escolha uma opção: '))
    if(opc not in range(1,6)):
        print()
        print("\n     ERRO!!!  \n     opção inválida")
        print()
        continue