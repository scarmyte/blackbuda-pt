import requests
from constants import BLACKBUDA_START, BLACKBUDA_END, BLACKBUDA_END_2023, BLACKBUDA_START_2023, MARKET_TRADES_URL

def calcular_volumen_transado_2023():
    params = {
        'timestamp': BLACKBUDA_END_2023,
        'limit': 100
    }

    total_btc = 0.0

    while True:
        response = requests.get(MARKET_TRADES_URL, params=params)
        data = response.json()

        if data['trades']['entries']:
            for entry in data['trades']['entries']:
                timestamp = int(entry[0])
                if(BLACKBUDA_START_2023 <= timestamp <= BLACKBUDA_END_2023):
                    total_btc += float(entry[1])
                else:
                    break
        
        if not data['trades']['entries'] or timestamp <= BLACKBUDA_START_2023:
            break

        params['timestamp'] = timestamp - 1
    
    total_btc = (total_btc * 100) // 1 / 100
    return total_btc


def calcular_volumen_transado_2024():
    params = {
        'timestamp': BLACKBUDA_END,
        'limit': 100
    }

    total_btc = 0.0

    while True:
        response = requests.get(MARKET_TRADES_URL, params=params)
        data = response.json()

        if data['trades']['entries']:
            for entry in data['trades']['entries']:
                timestamp = int(entry[0])
                if(BLACKBUDA_START <= timestamp <= BLACKBUDA_END):
                    total_btc += float(entry[1])
                else:
                    break
        
        if not data['trades']['entries'] or timestamp <= BLACKBUDA_START:
            break

        params['timestamp'] = timestamp - 1
    
    total_btc = (total_btc * 100) // 1 / 100
    return total_btc


total_2023 = calcular_volumen_transado_2023()
total_2024 = calcular_volumen_transado_2024()

porcentaje = ((total_2024 - total_2023) / total_2023) * 100

print(f'el porcentaje de incremento comparando con el mismo de dia un año antes es de {porcentaje:.2f}%')