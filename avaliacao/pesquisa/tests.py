from django.test import TestCase
from pesquisa.models import pesquisa, curso
from django.contrib.auth.models import User
from pesquisa.forms import PesquisaForm, CursoForm

class TemplatesTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        self.UserName = 'admin'
        self.Password = '123mudar'
        self.user = User.objects.create_user(self.UserName, 'admin@admin.com', self.Password)

    def test_template_home(self):
        self.assertTemplateUsed(self.resp, 'index.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_selecionarCurso(self):
        self.resp = self.client.get('/selecionarCurso')
        self.assertTemplateUsed(self.resp, 'pesquisa/index.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_avaliarCurso_Fail(self):
        self.resp = self.client.get('/avaliarCurso')
        self.assertTemplateUsed(self.resp, 'pesquisa/nenhum.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_avaliarCurso_OK(self):
        self.client.login(username='admin', password='123mudar')
        self.curso = curso.objects.create(
            nome="Treinamento Java",
            professor="Orlando",
            dataInicio="2016-12-12 10:00:00",
            dataFim="2016-12-15 00:00:00",
            )
        voucher = self.curso.gerarChave()
        self.curso.save()
        self.resp = self.client.post('/avaliarCurso', {'codigo_curso': voucher})
        self.assertTemplateUsed(self.resp, 'pesquisa/avaliar.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_registrarAvaliacao_OK(self):
        self.curso = curso.objects.create(
            nome="Treinamento Java",
            professor="Orlando",
            dataInicio="2016-12-12 10:00:00",
            dataFim="2016-12-15 00:00:00",
            )
        voucher = self.curso.gerarChave()
        self.curso.save()
        self.resp = self.client.post('/registrarAvaliacao', {
            'codigo_curso' : "0",
            'questao1' : "1",
            'questao2' : "2",
            'questao3' : "3",
            'questao4' : "4",
            'questao5' : "3",
            'questao6' : "4",
            'questao7' : "2",
            'questao8' : "1",
            'mensagem' : ""
            })
        self.assertTemplateUsed(self.resp, 'pesquisa/obrigado.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_registrarAvaliacao_Fail(self):
        self.curso = curso.objects.create(
            nome="Treinamento Java",
            professor="Orlando",
            dataInicio="2016-12-12 10:00:00",
            dataFim="2016-12-15 00:00:00",
            )
        voucher = self.curso.gerarChave()
        self.curso.save()
        self.resp = self.client.post('/registrarAvaliacao', {
            'codigo_curso' : "0",
            'questao1' : "5", # Opção varia entre 0 e 4 somente.
            'questao2' : "5", # Opção varia entre 0 e 4 somente.
            'questao3' : "3",
            'questao4' : "4",
            'questao5' : "3",
            'questao6' : "4",
            'questao7' : "2",
            'questao8' : "1",
            'mensagem' : ""

            })
        self.assertTemplateUsed(self.resp, 'pesquisa/erroCadastrarAvaliacao.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_cadastrarCurso_OK(self):
        self.client.login(username=self.UserName, password=self.Password)
        self.resp = self.client.get('/cadastrarCurso')
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)
        self.resp = self.client.post('/cadastrarCurso', {
            'nome': 'Treinamento',
            'dataFim': '12/12/2016',
            'dataInicio': '15/12/2016',
            'professor': 'Orlando',
        })
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso2.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_cadastrarCurso_Fail01(self):
        self.client.login(username=self.UserName, password=self.Password)
        self.resp = self.client.get('/cadastrarCurso')
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)
        self.resp = self.client.post('/cadastrarCurso', {
            'nome': 'Treinamento',
            'dataFim': '12-12-2016',  # Formato da data não usa barra simples " / "
            'dataInicio': '15-12-2016', # Formato da data não usa barra simples " / "
            'professor': 'Orlando',
        })
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_cadastrarCurso_Fail02(self):
        self.client.login(username=self.UserName, password=self.Password)
        self.resp = self.client.get('/cadastrarCurso')
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)
        self.resp = self.client.post('/cadastrarCurso', {
            'nome': '', # Nome do Treinamento em Branco. Não pode !
            'dataFim': '12/12/2016',
            'dataInicio': '15/12/2016',
            'professor': 'Orlando',
        })
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_cadastrarCurso_Fail03(self):
        self.client.login(username=self.UserName, password=self.Password)
        self.resp = self.client.get('/cadastrarCurso')
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)
        self.resp = self.client.post('/cadastrarCurso', {
            'nome': 'Treinamento',
            'dataFim': '12/12/2016',
            'dataInicio': '15/12/2016',
            'professor': '', # Nome do instrutor não pode ser vazio.
        })
        self.assertTemplateUsed(self.resp, 'pesquisa/cadastrarCurso.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_cursosAvaliados_OK(self):
        self.curso = curso.objects.create(
            nome="I Treinamento OO",
            professor="Orlando",
            dataInicio="2016-12-12 00:00:00",
            dataFim="2016-12-15 00:00:00",
            )
        self.curso.save()
        self.resp = self.client.get('/cursosAvaliados')
        self.assertTemplateUsed(self.resp, 'resultados/index.html')
        self.assertEqual(200, self.resp.status_code)
        self.resp = self.client.post('/cursosAvaliados', {
            'CursoAvaliadoAnteriormente': '1',
        })
        self.assertTemplateUsed(self.resp, 'resultados/resultados.html')
        self.assertEqual(200, self.resp.status_code)

    def test_template_cursosAvaliados_Fail(self):
        self.resp = self.client.get('/cursosAvaliados')
        self.assertTemplateUsed(self.resp, 'resultados/index.html')
        self.assertEqual(200, self.resp.status_code)
        self.resp = self.client.post('/cursosAvaliados', {
            'CursoAvaliadoAnteriormente': '1',
        })
        self.assertTemplateUsed(self.resp, 'resultados/nenhum.html')
        self.assertEqual(200, self.resp.status_code)

class FormsTest(TestCase):
    def test_form_CursoForm(self):
        form_data = {'nome': 'Treinamento',
            'dataFim': '2016-12-12 00:00:00',
            'dataInicio': '2016-12-12 00:00:00',
            'professor': 'Orlando',
            'codigo' : '6d024204'
            }
        form = CursoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_PesquisaForm(self):
        form_data = {'codigo_curso' : "0",
            'questao1' : "1",
            'questao2' : "2",
            'questao3' : "3",
            'questao4' : "4",
            'questao5' : "3",
            'questao6' : "4",
            'questao7' : "2",
            'questao8' : "1",
            'mensagem' : ""
            }
        form = PesquisaForm(data=form_data)
        self.assertTrue(form.is_valid())

class PesquisaModelTest(TestCase):
    def setUp(self):
        self.curso = curso.objects.create(
            nome="I Treinamento OO",
            professor="Orlando",
            dataInicio="2016-12-12 00:00:00",
            dataFim="2016-12-15 00:00:00",
            )

    def test_model_gerarChave(self):
        self.assertEqual(self.curso.gerarChave(), '6d024204')

    def test_model_setDataInicio(self):
        self.curso.setDataInicio("30/01/2017")
        self.assertEqual(self.curso.dataInicio, '2017-01-30 00:00:00')

    def test_model_setDataInicio(self):
        self.curso.setDataFim("30/01/2017")
        self.assertEqual(self.curso.dataFim, '2017-01-30 00:00:00')
