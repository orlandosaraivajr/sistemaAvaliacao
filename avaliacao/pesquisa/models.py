from django.db import models
from django.contrib.auth.models import User

class curso(models.Model):
    nome = models.CharField('nome', max_length=200)
    dataInicio = models.DateTimeField('data_inicio_curso')
    dataFim = models.DateTimeField('data_fim_curso')
    professor = models.CharField('professor', max_length=100)
    codigo = models.CharField('chave_acesso', max_length=10)

    def cursoNome(self):
        return '%s - %s' % (self.nome, self.professor)

    def gerarChave(self):
        import hashlib
        a = self.nome + self.dataFim + self.dataInicio
        x = hashlib.sha224(a.encode('UTF-8')).hexdigest()
        self.codigo = x[10:18].lower()
        return self.codigo

    def setDataInicio(self, dataInicio):
        import datetime
        data = dataInicio.split('/')
        d = datetime.datetime(int(data[2]), int(data[1]), int(data[0]), int("00"),int("00"), int("00"))
        self.dataInicio = d.strftime('%Y-%m-%d %H:%M:%S')

    def setDataFim(self, dataFim):
        import datetime
        data = dataFim.split('/')
        d = datetime.datetime(int(data[2]), int(data[1]), int(data[0]), int("00"),int("00"), int("00"))
        self.dataFim = d.strftime('%Y-%m-%d %H:%M:%S')

# Perguntas:
# 1. O professor apresentou adequadamente seu plano de trabalho.
# 2. O professor demonstrou possuir conhecimento técnico e segurança na abordagem dos conteúdos.
# 3. O professor foi pontual no cumprimento dos horários de início e término.
# 4. O professor mostrou­se motivado na condução do curso.
# 5. O professor desenvolveu o conteúdo de maneira clara, de modo a facilitar a compreensão.
# 6. O professor utilizou­-se adequadamente de outras estratégias de ensino, além da aula expositiva (como, por exemplo: vídeos, dinâmicas, estudos de casos, etc).
# 7. O professor relacionou os conteúdos teóricos com a aplicação prática.
# 8. Se você pudesse optar, cursaria outro treinamento com esse professor ?

class pesquisa(models.Model):
    OPCOES = (
        ('0', 'Discordo Totalmente'),
        ('1', 'Discordo'),
        ('2', 'Nem concordo, nem discordo'),
        ('3', 'Concordo'),
        ('4', 'Concordo Totalmente'),
    )
    SIM_NAO = (
        ('1', 'Sim'),
        ('0', u'Não'),
    )
    curso = models.ForeignKey(curso, on_delete=models.CASCADE)
    questao1 = models.CharField(max_length=1, choices=OPCOES)
    questao2 = models.CharField(max_length=1, choices=OPCOES)
    questao3 = models.CharField(max_length=1, choices=OPCOES)
    questao4 = models.CharField(max_length=1, choices=OPCOES)
    questao5 = models.CharField(max_length=1, choices=OPCOES)
    questao6 = models.CharField(max_length=1, choices=OPCOES)
    questao7 = models.CharField(max_length=1, choices=OPCOES)
    questao8 = models.CharField(max_length=1, choices=SIM_NAO)
    comentario = models.CharField(max_length=200)
