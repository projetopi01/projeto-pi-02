import unittest

# Função de exemplo para testar
def exemplo_funcao():
    return "Olá, mundo!"

# Classe de teste
class TestExemplo(unittest.TestCase):
    def test_exemplo_funcao(self):
        # Testando se a função retorna o esperado
        self.assertEqual(exemplo_funcao(), "Olá, mundo!")

# Roda os testes quando o script é executado
if __name__ == '__main__':
    unittest.main()
