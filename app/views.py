from django.shortcuts import render
from .models import SimulaModel, CarroLojaModel, CarroApi, LojaModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.plate_to_car import Plate2Car
import pandas as pd


# Create your views here.
def SimulaView(request):
    # --- setando variaveis ----
    cpf = 123 # request.POST.get('cpf')
    dt_nasc = request.POST.get('dt_nasc')
    celular = request.POST.get('celular')
    ocupacao = request.POST.get('ocupacao')
    cep = request.POST.get('cep')
    renda_mensal = request.POST.get('renda_mensal')
    renda_comple = request.POST.get('renda_comple')
    tipo_rend = request.POST.get('tipo_rend')
    vlr_renda = request.POST.get('vlr_renda')
    vlr_finan = request.POST.get('vlr_finan')
    qtd_parcela = request.POST.get('qtd_parcela')
    tx_cet_aa = request.POST.get('tx_cet_aa')
    tx_cet_mm = request.POST.get('tx_cet_mm')
    iof = request.POST.get('iof')
    tarifa_cad = request.POST.get('tarifa_cad')
    registro_ctt = request.POST.get('registro_ctt')
    retorno = request.POST.get('retorno')
    tarifa_aval = request.POST.get('tarifa_aval')
    vlr_finan_fim = request.POST.get('vlr_finan_fim')
    img_placa = request.POST.get('img_placa')
    num_placa = request.POST.get('num_placa')



    simulador = SimulaModel.objects.all()

    if request.method == 'POST':
        simula = SimulaModel(
            cpf,
            dt_nasc,
            celular,
            ocupacao,
            cep,
            renda_mensal,
            renda_comple,
            tipo_rend,
            vlr_renda,
            vlr_finan,
            qtd_parcela,
            tx_cet_aa,
            tx_cet_mm,
            iof,
            tarifa_cad,
            registro_ctt,
            retorno,
            tarifa_aval,
            vlr_finan_fim,
            img_placa,
            num_placa,
        )
        carroApi = Plate2Car.exec(num_placa)

        #simula.save()

        carro = CarroApi(
            carroApi['marca'],
            carroApi['modelo'],
            carroApi['cor'],
            carroApi['ano'],
            carroApi['cidade'],
            carroApi['estado'],
        )
        carro.save()

    return render(request, 'SimuladorFinanciamento.html', {'simulador':simulador})


class simula_api(APIView):
    def get(self, request):
        simula = pd.DataFrame(SimulaModel.objects.all().values())
        simula = simula.to_dict('index')
        return Response(data=simula, status=status.HTTP_200_OK)

class carro_loja_api(APIView):
    def get(self, request):
        carro_loja = pd.DataFrame(CarroLojaModel.objects.all().values())
        carro_loja = carro_loja.to_dict('index')
        return Response(data=carro_loja, status=status.HTTP_200_OK)

class loja_api(APIView):
    def get(self, request):
        loja = pd.DataFrame(LojaModel.objects.all().values())
        loja = loja.to_dict('index')
        return Response(data=loja, status=status.HTTP_200_OK)

class carro_api(APIView):
    def get(self, request):
        carro = pd.DataFrame(CarroApi.objects.all().values())
        carro = carro.to_dict('index')
        return Response(data=carro, status=status.HTTP_200_OK)



# Create your views here.
