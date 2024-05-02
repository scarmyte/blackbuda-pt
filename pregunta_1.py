import requests
from constants import BLACKBUDA_START, BLACKBUDA_END, MARKET_TRADES_URL

def calcular_dinero_transado():
    params = {
        'timestamp': BLACKBUDA_END,
        'limit': 100
    }

    total_clp = 0.0

    while True:
        response = requests.get(MARKET_TRADES_URL, params=params)
        data = response.json()

        if data['trades']['entries']:
            for entry in data['trades']['entries']:
                timestamp = int(entry[0])
                if(BLACKBUDA_START <= timestamp <= BLACKBUDA_END):
                    total_clp += float(entry[2])
                else:
                    break
        
        if not data['trades']['entries'] or timestamp <= BLACKBUDA_START:
            break

        params['timestamp'] = timestamp - 1

    return (total_clp * 100) // 1 / 100


print("Dinero transado durante BlackBuda en CLP: ", calcular_dinero_transado())