from constants import NORMAL_COMMISSION_RATE
from pregunta_1 import calcular_dinero_transado

def calcular_perdida_comisiones():
    dinero_transado = calcular_dinero_transado()
    dinero_perdido = dinero_transado * NORMAL_COMMISSION_RATE
    return (dinero_perdido * 100) // 1 / 100

print("La perdida en comisiones durante el BlackBuda fue de", calcular_perdida_comisiones(), "CLP")