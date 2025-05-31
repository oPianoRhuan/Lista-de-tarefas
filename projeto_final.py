def adicionar_tarefa (lista_de_tarefas, tarefa):
    lista_de_tarefas.append(tarefa)
    print(f"\n*>Tarefa '{tarefa}' adicionada<*\n")
    return (lista_de_tarefas)

def listar_tarefas (lista_de_tarefas):
        print("\n")
        n = 1
        print("-"*60)
        print (f"{' ' * 15}-->Lista de Tarefas<--\n")
        for tarefa in lista_de_tarefas:
            print(f"{n} - {tarefa}")
            n += 1
print("\n")       
        print("-"*60)

def excluir_tarefa (lista_de_tarefas, tarefa):
     lista_de_tarefas.pop((tarefa - 1 ))
     return lista_de_tarefas


def exibir_menu():
         print("Escolha uma opção: \n"\
    "1 - Inserir uma nova tarefa \n" \
    "2 - Listar tarefas \n" \
    "3 - Excluir tarefa \n" \
    "4 - Sair \n" \
 )
print(f"\n{' ' * 12} ***Organizador de tarefas***\n")

lista_de_tarefas = []

continuar = True
while continuar: 
    exibir_menu()
    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        tarefa = input('Insira uma nova tarefa: ')
        lista_de_tarefas = adicionar_tarefa(lista_de_tarefas, tarefa)
    elif opcao == "2":
        listar_tarefas(lista_de_tarefas)
    elif opcao == "3": 
         tarefa = input("Digite o número da tarefa que deseja excluir: ")
         if not tarefa.isnumeric():
              print ("Digite um NÚMERO válido.")
         elif int(tarefa) > len(lista_de_tarefas):
            print ("Opção inválida, tente novamente.")
         elif int(tarefa) <= 0:
            print ("Opção inválida, tente novamente.") 
         else: 
            excluir_tarefa(lista_de_tarefas, int(tarefa)) 
            print(f"Tarefa {tarefa} excluída com sucesso.")
    elif opcao == "4":
        print("Encerrando...")
        continuar = False 
    else: 
        print("Opção inválida, tente novamente.")
        print('\n')