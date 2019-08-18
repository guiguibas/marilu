"""
    transforma a imagem da placa em string

    como utilizar:
        Plate2Str.process(im=r"img\anexo1.jpg")
    retorno:
        {'result': 'OK', 'plate': 'AQQ0J49', 'score': 0.896}
"""
import requests
from __key__ import token


class Plate2Str(object):
    def __init__(self):
        pass

    def process(self, im):
        regions = ['fr', 'it']
        with open(im, 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),
                files=dict(upload=fp),
                headers={'Authorization': f'Token {token["car_plate"]}'})
            response = response.json()
            plate = str(response['results'][0]['plate']).upper().strip()
            plate = plate.replace('-', '')
            if len(plate) != 7:
                return {'result': 'erro'}
            score = response['results'][0]['score']
            dicio = {'result': 'OK', 'plate': plate, 'score': score}
        return dicio


Plate2Str = Plate2Str()
