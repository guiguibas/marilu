import requests
from __key__ import token


class Plate2Str(object):
    def __init__(self, im):
        self.im = im

    def process(self):
        regions = ['fr', 'it']
        with open(self.im, 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),
                files=dict(upload=fp),
                headers={'Authorization': f'Token {token["car_plate"]}'})
            response = response.json()
            plate = str(response['results'][0]['plate']).upper()
            score = response['results'][0]['score']
            dicio = {'result': 'ok', 'plate': plate, 'score': score}
        return dicio
