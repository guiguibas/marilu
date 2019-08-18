from django.db import models

# Create your models here.
class SimulaModel(models.Model):
    cpf = models.IntegerField()
    dt_nasc = models.DateField()
    celular = models.IntegerField()
    ocupacao = models.CharField(max_length=100)
    cep = models.IntegerField()
    renda_mensal = models.DecimalField(max_digits=6,decimal_places=2)
    renda_comple = models.BooleanField()
    tipo_rend = models.CharField(max_length=100)
    vlr_renda = models.DecimalField(max_digits=6,decimal_places=2)
    vlr_finan = models.DecimalField(max_digits=6, decimal_places=2)
    vlr_entra = models.DecimalField(max_digits=6, decimal_places=2)
    qtd_parcela = models.IntegerField()
    tx_cet_aa = models.DecimalField(max_digits=6, decimal_places=2)
    tx_cet_mm = models.DecimalField(max_digits=6, decimal_places=2)
    iof = models.DecimalField(max_digits=6, decimal_places=2)
    tarifa_cad = models.DecimalField(max_digits=6, decimal_places=2)
    registro_ctt = models.DecimalField(max_digits=6, decimal_places=2)
    retorno = models.DecimalField(max_digits=6, decimal_places=2)
    tarifa_aval = models.DecimalField(max_digits=6, decimal_places=2)
    vlr_finan_fim = models.DecimalField(max_digits=6, decimal_places=2)
    img_placa = models.ImageField(upload_to='img_placa')
    num_placa = models.CharField(max_length=100)

    def __str__(self):
        return str(self.cpf)


class CarroLojaModel(models.Model):
    modelo_carro = models.CharField(max_length=100)
    placa_carro = models.CharField(max_length=100)
    vlr_finan = models.DecimalField(max_digits=6, decimal_places=2)
    cor_carro = models.CharField(max_length=100)
    cidade_loja = models.CharField(max_length=100)
    uf_loja = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_loja
