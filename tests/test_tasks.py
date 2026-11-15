import unittest

from tasks import mensagem_vazia, pendentes


class FiltroTest(unittest.TestCase):
    def test_oculta_concluidas(self):
        tarefas = [{"titulo": "a", "concluida": True}, {"titulo": "b", "concluida": False}]
        self.assertEqual([t["titulo"] for t in pendentes(tarefas)], ["b"])

    def test_filtro_desativado_mostra_tudo(self):
        tarefas = [{"titulo": "a", "concluida": True}]
        self.assertEqual(len(pendentes(tarefas, ocultar_concluidas=False)), 1)

    def test_estado_vazio(self):
        self.assertEqual(mensagem_vazia([]), "Nenhuma tarefa pendente")


if __name__ == "__main__":
    unittest.main()
