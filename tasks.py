"""Gerenciador de tarefas mínimo (repositório de teste do MAESTRO)."""


def pendentes(tarefas, ocultar_concluidas=True):
    """Devolve as tarefas visíveis; com o filtro ativo, esconde as concluídas."""
    if not ocultar_concluidas:
        return list(tarefas)
    return [t for t in tarefas if not t.get("concluida")]


def mensagem_vazia(tarefas_visiveis):
    """Estado vazio exibido quando o filtro não deixa nenhuma tarefa."""
    return "Nenhuma tarefa pendente" if not tarefas_visiveis else ""
