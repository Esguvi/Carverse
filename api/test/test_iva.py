from api.web.funciones_auxiliares import calculariva

def test_iva():
    resultado_esperado = 21
    resultado = calculariva(100)
    assert resultado == resultado_esperado
