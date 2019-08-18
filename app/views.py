from django.shortcuts import render
from .models import SimulaModel, CarroLojaModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pandas as pd


# Create your views here.
def SimulaView(request):
    # --- setando variaveis ----
    cpf = request.POST.get('cpf')
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
        simula.save()
    return render(request, 'SimuladorFinanciamento.html')


class simula_api(APIView):
    def get(self, request):
        simula = pd.DataFrame(list())

        return Response(data=dicio, status=status.HTTP_200_OK)


