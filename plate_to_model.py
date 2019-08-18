'''
    exemplo
        Plate2Car.exec('IMI-0175')
    retorno
        {'marca': 'VOLKSWAGEN', 'modelo': 'POLO 1.6 SEDAN', 'cor': 'PRATA', 'ano': '2004 / 2005', 'cidade': 'VIAMÃO', 'estado': 'RS'}
'''

import requests
from bs4 import BeautifulSoup


class Plate2Car(object):

    def exec(self, plate):
        url = 'https://www.qualveiculo.net/'
        headers = {"content-type": "application/x-www-form-urlencoded",
                   "User-Agent": "PostmanRuntime/7.15.2",
                   "Accept": "*/*",
                   "Cache-Control": "no-cache",
                   "Host": "www.qualveiculo.net",
                   "Cookie": "__cfduid=d5de75a3b4f8bf134d17b8037c9f9df861566082245; USID=29fbe229d00c9126fb7e579bcc28ebe3",
                   "Accept-Encoding": "gzip, deflate"}

        r = requests.post(url, data={'placa': plate}, headers=headers)
        s = r.text

        soup = BeautifulSoup(s, 'html.parser')
        carro = soup.find("span", {"class": "dados"}).text
        carro = carro.upper()
        num = carro.find(' ')
        marca = carro[:num]
        modelo = carro[num+1:]

        cor_ano = soup.find("span", {"class": "dados texto"}).text
        cor, ano = cor_ano.upper().split(' - ')
        cor = cor.replace('COR: ', '')
        ano = ano.replace('ANO: ', '')

        local = soup.find("span", {"class": "dados localidade"}).text
        cidade, estado = local.upper().split(' - ')

        dicio = {'marca': marca, 'modelo': modelo, 'cor': cor, 'ano': ano, 'cidade': cidade, 'estado': estado}

        return dicio


Plate2Car = Plate2Car()
