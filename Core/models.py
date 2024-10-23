from django.db import models

# Create your models here.

#Cores

class Cores(models.Model):
    nome = models.CharField(max_length=255)
    cor_principal = models.CharField(max_length=7)
    cor_detalhes = models.CharField(max_length=7)
    
    def __str__(self):
        return self.nome


class Servicos(models.Model):
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE)
    
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor.nome}/servicos/{filename}'
    
    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'serviço da cor {self.cor.nome}'


class Imagens_beneficios_cores(models.Model):
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE)
    
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor}/beneficios/{filename}'


    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'beneficio da cor {self.cor.nome}'

class Ideal_para(models.Model):
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE)
    
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor.nome}/ideal_para/{filename}'

    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'Ideal para da cor {self.cor.nome}'

#fim cores


#Estações
class Estacao(models.Model):
    nome = models.CharField(max_length=255)
    def gerar_rota(self, filename):
        return f'static/images/estacoes/{self.nome}/logo/{filename}'
    logo = models.ImageField(upload_to=gerar_rota)
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE)
    descricao_estacao = models.TextField(max_length=2000)
    texto_funcionamento = models.TextField(max_length=1000)
    servico1 = models.TextField(max_length=100)
    servico2 = models.TextField(max_length=100)
    servico3 = models.TextField(max_length=100)
    responsabilidade = models.CharField(max_length=1000)
    beneficio1 = models.TextField(max_length=1000)
    beneficio2 = models.TextField(max_length=1000)
    beneficio3 = models.TextField(max_length=1000)
    ideal_para1 = models.TextField(max_length=1000)
    ideal_para2 = models.TextField(max_length=1000)
    ideal_para3 = models.TextField(max_length=1000)
    competencia = models.TextField(max_length=1000)
    
    

    def __str__(self):
        return self.nome


class Beneficios(models.Model):
    cor = models.ForeignKey(Cores, on_delete=models.CASCADE)
    def gerar_rota(self, filename):
        return f'static/images/cores/{self.cor.nome}/beneficios/{filename}'
    imagem = models.ImageField(upload_to=gerar_rota)

    def __str__(self):
        return f'Imagem de beneficio da estação {self.cor.nome}'




class Imagens_equipe(models.Model):
    estacao = models.ForeignKey(Estacao, on_delete=models.CASCADE)
    def gerar_rota(self, filename):
        return f'static/images/estacoes/{self.estacao.nome}/equipe/{filename}'
    imagem = models.ImageField(upload_to=gerar_rota)
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.estacao

