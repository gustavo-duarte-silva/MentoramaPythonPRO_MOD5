import pytest
from testes.calculadora import multiple
class TesteNumeroNatural:
    """
    Esta Classe verifica se o numero é multiplo de 3 e 7
    """
    def teste_multiple(self):
        """
        Este Modulo de teste verifica se o numero é multiplo de 3 e 7
        """
        with pytest.raises(OSError):
            results = multiple()
            assert results == 0
