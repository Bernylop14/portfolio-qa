import pytest
from ayama_funciones import validar_edad_halcon, evaluar_señal, obtener_estado_servidor

@pytest.fixture
def halcon_de_prueba():
    halcon = {
        "nombre": "Apolo",
        "edad": 5,
        "ultima_señal": "98%"
    }
    return halcon

@pytest.fixture
def receptor_conectado():
    print("\n🔌 Conectando con el receptor...")  # esto es el SETUP
    receptor = {"conectado": True, "señal": "98%"}
    yield receptor  # esto es lo que recibe el test
    print("\n🔌 Desconectando el receptor...")  # esto es el TEARDOWN

@pytest.mark.parametrize("edad, resultado_esperado", [
    (0, False),
    (1, True),
    (30, True),
    (31, False),
])
def test_validar_edad_halcon(edad, resultado_esperado):
    assert validar_edad_halcon(edad) == resultado_esperado

def test_halcon_tiene_edad_valida(halcon_de_prueba):
    assert validar_edad_halcon(halcon_de_prueba["edad"]) == True

def test_halcon_tiene_nombre(halcon_de_prueba):
    assert halcon_de_prueba["nombre"] == "Apolo"

def test_receptor_esta_conectado(receptor_conectado):
    assert receptor_conectado["conectado"] == True

from unittest.mock import Mock

def test_señal_perdida():
    receptor_simulado = Mock(return_value=0)  # ← esto es el Stub
    resultado = evaluar_señal(receptor_simulado)
    assert resultado == "Señal perdida"

def test_servidor_responde_correctamente():
    respuesta = obtener_estado_servidor()
    assert respuesta.status_code == 200

def test_servidor_devuelve_datos():
    respuesta = obtener_estado_servidor()
    datos = respuesta.json()
    assert "id" in datos