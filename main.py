def criar_tarefa(tarefa):
    print(f"Tarefa criada: {tarefa}")

def listar_tarefas():
    print("Listando todas as tarefas...")

def atualizar_tarefa(id_tarefa, nova_descricao):
    print(f"Tarefa {id_tarefa} atualizada para: {nova_descricao}")

def deletar_tarefa(id_tarefa):
    print(f"Tarefa {id_tarefa} deletada com sucesso no sistema principal.")

if _name_ == "_main_":
    criar_tarefa("Configurar o repositório Git")
    listar_tarefas()
    atualizar_tarefa(1, "Configurar as branches e PR")
    deletar_tarefa(1)