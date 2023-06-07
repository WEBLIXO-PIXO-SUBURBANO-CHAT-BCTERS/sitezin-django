from django.db import models

class Orcamento(models.Model):
    ESTILO_CHOICES = (
        ('freestyle', 'Freestyle'),
        # ('grafite', 'Grafite'),
        ('pixo', 'Pixo'),
        ('canetao', 'Canetão')
        ('grapixo', 'Grapixo'),
        # ('stencil', 'Stencil'),
        # ('muralismo', 'Muralismo'),
        # ('wheatpaste', 'WheatPaste'),
        # ('mbomb', 'MBomb'),
    )
    ESTILO_VALORES = {
        'freestyle': 100,
        # 'grafite': 300,
        'pixo': 80,
        'grapixo': 130,
        'canetao': 50,
        # 'stencil': 600,
        # 'muralismo': 1500,
        # 'wheatpaste': 700,
        # 'mbomb': 900,
    }


    cliente = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    superficie = models.CharField(max_length=100)
    estilo = models.CharField(max_length=20, choices=ESTILO_CHOICES)
    cores = models.CharField(max_length=500)
    preparacao_superficie = models.TextField()
    prazo_conclusao = models.DateField()
    orcamento_estabelecido = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    restricao_acesso = models.BooleanField(default=False)
    servicos_adicionais = models.TextField(blank=True)
    tema = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Cálculo do orçamento_estabelecido com base em outros campos
        # Implemente a lógica de cálculo de acordo com suas necessidades
        # Exemplo de cálculo: self.orcamento_estabelecido = self.area * 10
        self.orcamento_estabelecido = self.calcular_orcamento_estabelecido()
        super().save(*args, **kwargs)

    def calcular_orcamento_estabelecido(self):
        return self.area * 10

    def __str__(self):
        return f'Orcamento para {self.cliente}'
