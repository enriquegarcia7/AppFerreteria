import requests

def obtener_tipo_cambio():
    api_url = 'https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx'
    params = {
        'user': 'ni.sabando@duocuc.cl   ',
        'pass': 'tu_contrasena',
        'timeseries': 'F073.TCO.PRE.Z.D',
        'function': 'GetSeries',
    }

    response = requests.get(api_url, params=params)
    data = response.json()
    tipo_cambio = float(data['Series']['Obs'][0]['value'])
    return tipo_cambio