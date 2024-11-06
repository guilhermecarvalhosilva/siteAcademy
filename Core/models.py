from django.db import models

# Create your models here.

#Cores

class Paleta_Core(models.Model):
    nome = models.CharField(max_length=255)
    cor_principal = models.CharField(max_length=7)
    cor_detalhes = models.CharField(max_length=7)

    def save(self, *args, **kwargs):
        # Remove o '#' no início, caso exista
        if self.cor_principal.startswith('#'):
            self.cor_principal = self.cor_principal[1:]
        
        if self.cor_detalhes.startswith('#'):
            self.cor_detalhes = self.cor_detalhes[1:]
        
        super().save(*args, **kwargs)

    



class Imagens_Beneficios_Core(models.Model):
    cor = models.ForeignKey(Paleta_Core, on_delete=models.CASCADE)
    alt = models.CharField(max_length=100)
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor}/beneficios/{filename}'


    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'beneficio da cor {self.cor.nome}'

class Imagens_Ideal_Para_Core(models.Model):
    cor = models.ForeignKey(Paleta_Core, on_delete=models.CASCADE)
    
    def gerar_rota(self, filename):
        return f'static/images/global/cores/{self.cor.nome}/ideal_para/{filename}'
    
    alt = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to=gerar_rota)
    
    def __str__(self):
        return f'Imagem de Texto Ideal para da cor {self.cor.nome}'

#fim cores


#Estações
class Estacoe(models.Model):
    nome = models.CharField(max_length=255)
    def gerar_rota(self, filename):
        return f'static/images/estacoes/{self.nome}/logo/{filename}'
    logo = models.ImageField(upload_to=gerar_rota)
    def gerar_rota_icon(self, filename):
        return f'static/images/estacoes/{self.nome}/icon/{filename}'
    icon = models.ImageField(upload_to=gerar_rota_icon)
    cor = models.ForeignKey(Paleta_Core, on_delete=models.CASCADE)
    descricao_estacao = models.TextField(max_length=2000)
    texto_funcionamento = models.TextField(max_length=1000)
    responsabilidade = models.TextField(max_length=1000)
    

    def __str__(self):
        return self.nome


class Texto_Ideal_para_Estacoe(models.Model):
    estacao = models.ForeignKey(Estacoe, on_delete=models.CASCADE)
    Ideal_para =models.CharField(max_length=100) 

    def __str__(self):
        return f'texto de Ideal para da estação {self.estacao}'


class Texto_Beneficios_Estacoe(models.Model):
    estacao = models.ForeignKey(Estacoe, on_delete=models.CASCADE)
    beneficio = models.CharField(max_length=100)

    def __str__(self):
        return f'texto de beneficio da estação {self.estacao}'


class Texto_Servicos_Estacoe(models.Model):
    estacao = models.ForeignKey(Estacoe, on_delete=models.CASCADE)
    servico = models.CharField(max_length=100)

    def __str__(self):
        return f'texto de servico da estação {self.estacao}'

class Texto_Competencias_Estacoe(models.Model):
    estacao = models.ForeignKey(Estacoe, on_delete=models.CASCADE)
    competencia = models.CharField(max_length=100)

    def __str__(self):
        return f'texto de competencia da estação {self.estacao}' 




class Imagens_equipe(models.Model):
    estacao = models.ForeignKey(Estacoe, on_delete=models.CASCADE)
    def gerar_rota(self, filename):
        return f'static/images/estacoes/{self.estacao.nome}/equipe/{filename}'
    imagem = models.ImageField(upload_to=gerar_rota)
    alt = models.CharField(max_length=100)

    def __str__(self):
        return self.estacao

