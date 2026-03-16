from calculadora import sumar, restar, multiplicar, dividir

import pytest

# ----- FIXTURES -----

@pytest.fixture
def numeros_enteros():
    """Prepara dos enteros comunes."""
    return 20, 5

@pytest.fixture
def numeros_decimales():
    """Prepara dos números decimales para pruebas de precisión."""
    return 0.1, 0.2

@pytest.fixture
def numeros_negativos():
    """Prepara dos números negativos para pruebas de operaciones con signos."""
    return -5, -3

@pytest.fixture
def signos_diferentes():
    """Prepara dos números con signo distintos """
    return -10, 5

@pytest.fixture
def numeros_cero():
    """Prepara dos números donde uno es cero para pruebas de casos límite."""
    return 10, 0

@pytest.fixture
def string_add():
    """Prepara dos cadenas de texto para pruebas de manejo de tipos."""
    return "Hola, ", 5

@pytest.fixture
def dos_strings():
    """Prepara dos cadenas de texto para pruebas de manejo de tipos."""
    return "Hola, ", "mundo!"

@pytest.fixture
def numeros_grandes():
    """Prepara dos números grandes para pruebas de rendimiento y precisión."""
    return 1e10, 1e10

@pytest.fixture
def numeros_pequenos():
    """Prepara dos números pequeños para pruebas de precisión en decimales."""
    return 1e-10, 1e-10


# ----- TESTS CON FIXTURES -----
def test_sumar_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la suma."""
    a, b = numeros_enteros
    assert sumar(a, b) == 25
    
def test_sumar_decimales(numeros_decimales):
    """Test que usa la fixture de números decimales para probar la suma."""
    a, b = numeros_decimales
    resultado = sumar(a, b)
    # Usando pytest.approx para comparación con tolerancia
    assert resultado == pytest.approx(0.3, rel=1e-8)
    
def test_sumar_diferent_signos(signos_diferentes):
    """Test que usa la fixture de números con signos diferentes para probar la suma."""
    a, b = signos_diferentes
    assert sumar(a, b) == -5
    
def test_restar_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la resta."""
    a,b = numeros_enteros
    assert restar(a,b) == 15
    
def test_restar_decimales(numeros_decimales):
    """Test que usa la fixture de números decimales para probar la resta."""
    a, b = numeros_decimales
    resultado = restar(a, b)
    # Usando pytest.approx para comparación con tolerancia
    assert resultado == pytest.approx(-0.1, rel=1e-8)
    
def test_multiplicar_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la multiplicación."""
    a, b = numeros_enteros
    assert multiplicar(a, b) == 100
    
def test_multiplicar_decimales(numeros_decimales):
    """Test que usa la fixture de números decimales para probar la multiplicación."""
    a, b = numeros_decimales
    resultado = multiplicar(a, b)
    # Usando pytest.approx para comparación con tolerancia
    assert resultado == pytest.approx(0.02, rel=1e-8)
    
def test_multiplicar_diferentes_Signos(signos_diferentes):
    """Test que usa la fixture de números con signos diferentes para probar la multiplicación."""
    a, b = signos_diferentes
    assert multiplicar(a, b) == -50

def test_multiplicar_ceros(numeros_cero):
    """Test que usa la fixture de números donde uno es cero para probar la multiplicación."""
    a,b = numeros_cero
    assert multiplicar(a,b) == 0

    
def test_dividir_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la división."""
    a, b = numeros_enteros
    assert dividir(a, b) == 4
    
def test_dividir_decimales(numeros_decimales):
    """Test que usa la fixture de números decimales para probar la división."""
    a, b = numeros_decimales
    resultado = dividir(a, b)
    # Usando pytest.approx para comparación con tolerancia
    assert resultado == pytest.approx(0.5, rel=1e-8)

def test_dividir_por_cero(numeros_cero):
    """Test que usa la fixture de números donde uno es cero para probar la división por cero."""
    a, b = numeros_cero
    with pytest.raises(ValueError) as excinfo:
        dividir(a, b)
    # Verificamos también el mensaje de error
    assert "No se puede dividir por cero" in str(excinfo.value)
    
def test_sumar_error_dato_invalido(string_add):
    """Prueba que sumar lanza ValueError si se pasan textos."""
    a,b = string_add
    with pytest.raises(TypeError): # Cambiamos ValueError por TypeError
        sumar(a, b)
def test_restar_error_dato_invalido(string_add):
    """Prueba que restar lanza ValueError si se pasan textos."""
    a,b = string_add
    with pytest.raises(TypeError): # Cambiamos ValueError por TypeError
        restar(a, b)
def test_multiplicar_error_dato_invalido(dos_strings):
    """Prueba que multiplicar lanza ValueError si se pasan textos."""
    a,b = dos_strings
    with pytest.raises(TypeError):
        multiplicar(a, b)



# ----- TESTS PARAMETRIZADOS -----

@pytest.mark.parametrize(
    "a,b,esperado", 
    [
        (1, 2, 3),      # Enteros positivos
        (-1, -1, -2),   # Enteros negativos
        (2.5, 0.5, 3),  # Decimales
        (0, 0, 0)       # Caso cero
    ]
)
def test_sumar_varios(a, b, esperado):
    """Test parametrizado que prueba la función sumar con diversos valores."""
    assert sumar(a, b) == esperado

@pytest.mark.parametrize(
    "a,b,esperado", 
    [
        (10, 5, 5),     # Enteros positivos
        (-1, -2, 1),    # Enteros negativos
        (3.5, 1.5, 2),  # Decimales
        (0, 0, 0)       # Caso cero
    ]
)
def test_restar_varios(a, b, esperado):
    """Test parametrizado que prueba la función restar con diversos valores."""
    assert restar(a, b) == esperado

@pytest.mark.parametrize("a,b,esperado",
                         [
                             (2,2,4),          # Enteros positivos
                             (-1,-1,1),        # Enteros negativos
                             (2.5,0.5,1.25),    # Decimales
                             (0,5,0)           # Caso con cero
                         ])
def test_multiplicar_varios(a, b, esperado):
    """Test parametrizado que prueba la función multiplicar con diversos valores."""
    assert multiplicar(a, b) == esperado

@pytest.mark.parametrize("a,b,esperado",
                         [
                             (12,4,3),          # Enteros positivos
                             (-10,-2,5),        # Enteros negativos
                             (3.5,0.5,7),       # Decimales
                             (5,0,"Error")      # División por cero
                         ])
def test_dividir_varios(a, b, esperado):
    """Test parametrizado que prueba la función dividir con diversos valores."""
    if esperado == "Error":
        with pytest.raises(ValueError) as excinfo:
            dividir(a, b)
        assert "No se puede dividir por cero" in str(excinfo.value)
    else:
        assert dividir(a, b) == esperado

# ----- TESTS CON ETIQUETAS (MARKS) -----

@pytest.mark.smoke
def test_restar_smoke():
    """Test básico etiquetado como 'smoke' para pruebas rápidas."""
    assert restar(10, 8) == 2

@pytest.mark.smoke
def test_sumar_smoke():
    """Otro test etiquetado como 'smoke'."""
    assert sumar(5, 5) == 10

@pytest.mark.exception
def test_dividir_por_cero():
    """Test etiquetado como 'exception' que verifica manejo de error en división por cero."""
    with pytest.raises(ValueError) as excinfo:
        dividir(1, 0)
    # Verificamos también el mensaje de error
    assert "No se puede dividir por cero" in str(excinfo.value)

# ----- TESTS CON ASERCIONES DE PRECISIÓN -----
def test_multiplicar_preciso(numeros_decimales):
    """Test que verifica la precisión de multiplicación con números decimales."""
    a, b = numeros_decimales
    resultado = multiplicar(a, b)
    # Usando pytest.approx para comparación con tolerancia
    assert resultado == pytest.approx(0.02, rel=1e-8)

def test_dividir_preciso():
    """Test que verifica la precisión en división con resultado periódico."""
    resultado = dividir(1, 3)
    # Usando pytest.approx para comparación con tolerancia relativa
    # Usamos 1/3 para mayor precisión en la comparación
    assert resultado == pytest.approx(1/3, rel=1e-4)