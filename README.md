## Info Gerais

##### Sobre o projeto
Simulador para financiamento de veiculos desenvolvido para atender a proposta do Hackathon do Grupo Pan.

O foco da equipe para a solucao foi reduzir o maximo de preenchimento manual dos campos e ajustar a ordem para trazer uma experiencia melhor para os usuarios, reduzindo assim o funil de desistencia.

Para isso foi identificado alguns sistemas facilitadores que auxiliaram no preenchimento, reduzindo assim o input manual dos dados. Sao eles:
* 1 - Interesse no modelo do veiculo
* 2 - Filtro dos veiculos geolocalizacao
* 3 - Filtro por opcionais do veiculo
* 4 - Escolha do veiculo
* 5 - Metodos de pagamento
* 6 - Conclusao do contrato

Para agilizar o desenvolvimento aproveitamos algumas APIS livres, dentre elas:
* platerecognizer.com: Algoritmo de IA para identificacao de placas;
* qualveiculo.net: Crawler de informacoes basicas sobre o Veiculo;

Obs: Nao ha dependencia desses servicos, sabendo que o desenvolvimento pode ser realizado no futuro.

##### Tecnologias utilizadas
* [Python 3.7.3] - backend 
* [Django 2.2.4] - backend api rest
* [Vue.js] - frontend
* [HTML] - frontend
* [CSS] - frontend
* [SASS] - frontend


##### Link
backend: https://github.com/guiguibas/marilu/tree/back_end

frontend: https://github.com/guiguibas/marilu/tree/frontend

PPT: https://docs.google.com/presentation/d/1Py4A5jA3VGxEuDbtp40u9RfaYMiBwAIsws-QW24SOkQ/edit?ts=5d590380#slide=id.p6


##### Grupo
| Nome | GitHub | Email 
|---|---|---|
| Guilherme Neto |  @guiguibas | guigui.silva.neto@gmail.com |
| Joao Scheuermann  | @joaoscheuermann  | jvitor.sche@gmail.com |
| Tamara Ingrid | @ | tamara.mlsf@gmail.com |
| Thales Gibbon | @thalesgibbon | thales.gibbon@gmail.com |


## Deploy

##### Acessos
* IP AWS: ec2-18-205-23-188.compute-1.amazonaws.com:80
* USER: Administrator
* PASS: u-E)oQm=rhJ.gGUme(VOF%TM@BxSD7aS
* DJANGO PORT: 80

##### Passo a passo de deploy
* python 3.6 [+] (ok)
* Git (ok)
* Liberar porta 80 (ok)
* Liberar grupo de seguranca na cloud (ok)
* Instalar requirement (ok)
* Ajustar host no settings.py (ok)
* Clonar repositorio (ok)
* Subir servico (ok)

##### Como subir o servico
```cmd
python manage.py runserver ec2-18-205-23-188.compute-1.amazonaws.com:80
```

## Comandos recorrentes

##### windows

##### git
git pull origin back_end

##### libs
pip freeze > requirements.txt
pip install -r requirements.txt

##### django
python manage.py runserver ec2-18-205-23-188.compute-1.amazonaws.com:80

##### python