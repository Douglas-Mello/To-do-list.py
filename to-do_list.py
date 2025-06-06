from time import sleep
tarefa_dic = dict()
tarefa= list()
while True:
    print("===  Menu de opções:  ====")
    print("1.Adicionar Tarefa \n2.Ver tarefas\n3.Conclui uma tarefa\n4.Remover tarefa\n5.Sair")
    opc=int(input('Escolha uma opção: '))
    if(opc not in range(1,6)):
        print("\n     ERRO!!!  \n     opção inválida")
        print()
        sleep(1.5)
    if(opc ==1):
        while True:
            tarefa_dic['tarefas'] = input("Qual sua tarefa: ")
            tarefa_dic['status'] = False
            tarefa.append(tarefa_dic.copy())##Tem q fazer copia, o py faz 'ligação' n copia
            tarefa_dic.clear()
            print('Adicionando Tarefa ...')
            sleep(1.3)
            cont=input('Quer adicionar outra tarefa[s/n]: ')
            if(cont[0] in 'Nn'):
                print()
                break
            
        
    elif( opc == 2):
        print()
        print("Suas tarefas: ")
        for i, v in enumerate(tarefa):
            print(f'{i+1}. {v}')
            sleep(1)
        sleep(1)
        print()
        print()
    elif(opc == 3):
        print("Qual tarefa foi concluida: ")
        for i, v in enumerate(tarefa):
            print(f'{i+1}. {v}')
        status


