import pytest
from testes.calculadora import multiple

class TesteNumeroNatural:
    def teste_multiple(self):
        with pytest.raises(OSError):
            results = multiple()
            assert results == 0
