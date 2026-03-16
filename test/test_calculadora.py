from calculadora import sumar, restar, multiplicar, dividir
import pytest

@pytest.fixture
def numeros_enteros():
    return 20, 5

def test_dividir_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 4
    
@pytest.mark.parametrize("a, b, esperado",
                         [
                             (1, 2, 3),
                             (-1, -1, -2),
                             (2.5, 0.5, 3)
                        ]
                         )
def test_sumar_varios(a, b, esperado):
    assert sumar(a, b) == esperado

@pytest.mark.smoke
def test_sumar_smoke():
    assert sumar(10, 5) == 15

@pytest.mark.exception
def test_restar():
    assert restar(10, 5) == 5
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
    
def test_multiplicar():
    assert multiplicar(2, 3) == 6

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)
