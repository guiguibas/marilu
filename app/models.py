from django.db import models

# Create your models here.
class SimulaModel(models.Model):
    cpf = models.IntegerField(null=True)
    dt_nasc = models.DateField(null=True)
    celular = models.IntegerField(null=True)
    ocupacao = models.CharField(max_length=100,null=True)
    cep = models.IntegerField(null=True)
    renda_mensal = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    renda_comple = models.BooleanField(null=True)
    tipo_rend = models.CharField(max_length=100,null=True)
    vlr_renda = models.DecimalField(max_digits=6,decimal_places=2,null=True)
    vlr_finan = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    vlr_entra = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    qtd_parcela = models.IntegerField(null=True)
    tx_cet_aa = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    tx_cet_mm = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    iof = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    tarifa_cad = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    registro_ctt = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    retorno = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    tarifa_aval = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    vlr_finan_fim = models.DecimalField(max_digits=6, decimal_places=2,null=True)
    img_placa = models.ImageField(upload_to='img_placa',null=True)
    num_placa = models.CharField(max_length=100,null=True)

    def __str__(self):
        return str(self.cpf)


class CarroLojaModel(models.Model):
    fk_loja = models.IntegerField()
    modelo_carro = models.CharField(max_length=100)
    placa_carro = models.CharField(max_length=100)
    vlr_finan = models.DecimalField(max_digits=6, decimal_places=2)
    cor_carro = models.CharField(max_length=100)

    def __str__(self):
        return self.placa_carro

class LojaModel(models.Model):
    id = models.AutoField(primary_key=True)
    cidade_loja = models.CharField(max_length=100)
    uf_loja = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)

class CarroApi(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    ano = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)