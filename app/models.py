from django.db import models

# Create your models here.
class Continente(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome
  
    
class Pais(models.Model):
    nome = models.CharField(max_length=255)
    continente = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.nome} {self.continente}'


class Ator(models.Model):
    nome = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    insta = models.CharField(max_length=255)
    face = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} {self.site} {self.insta} {self.face} {self.twitter} {self.nacionalidade}'


class Diretor(models.Model):
    nome = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    insta = models.CharField(max_length=255)
    face = models.CharField(max_length=255)
    twitter = models.CharField(max_length=255)
    nacionalidade = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} {self.site} {self.insta} {self.face} {self.twitter} {self.nacionalidade}'


class Epsodio(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.DecimalField(max_digits=6, decimal_places=2)
    data_disponivel = models.DateField('data_disponivel')

    def __str__(self):
        return f'{self.nome} {self.duracao} {self.data_disponivel}'


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Serie(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.DecimalField(max_digits=7, decimal_places=2)
    sinopse = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    data_lancamento = models.DateField('data_lancamento')
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1, max_length=10)
    categoria = models.ManyToManyField(Categoria)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.duracao} {self.sinopse} {self.site} {self.data_lancamento} {self. nota_avaliacao} {self.categoria} {self.pais} {self.diretor}'


class Temporada(models.Model):
    temporada = models.CharField(max_length=255)
    
    def __str__(self):
        return self.temporada
  
    
class Filme(models.Model):
    nome = models.CharField(max_length=255)
    duracao = models.DecimalField(max_digits=7, decimal_places=2)
    sinopse = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    data_lancamento = models.DateField('data_lancamento')
    nota_avaliacao = models.DecimalField(max_digits=3, decimal_places=1, max_length=10)
    categoria = models.ManyToManyField(Categoria)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.nome} {self.duracao} {self.sinopse} {self.site} {self.data_lancamento} {self. nota_avaliacao} {self.categoria} {self.pais} {self.diretor}'


class Elenco(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator = models.ManyToManyField(Ator)
    diretor = models.ForeignKey(Diretor, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.filme} {self.ator} {self.diretor}'
    
    
class Serie_Epsodio(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE)
    temporada = models.ManyToManyField(Temporada)
    epsodio = models.ManyToManyField(Epsodio)

    def __str__(self):
        return f'{self.serie} {self.temporada} {self.epsodio}'