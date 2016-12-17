from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .models import curso, pesquisa
from .forms import PesquisaForm,CursoForm

def login(request):
    context = {}
    if request.method == "GET":
        template = loader.get_template('login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            template = loader.get_template('index.html')
        else:
            template = loader.get_template('login.html')
    return HttpResponse(template.render(context, request))

def logout(request):
    auth_logout(request)
    context = {}
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def selecionarCurso(request):
    template = loader.get_template('pesquisa/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def avaliarCurso(request):
    codigoCurso = request.POST.get("codigo_curso", "")
    cursoQuery = curso.objects.filter(codigo=codigoCurso)
    if cursoQuery.count() == 1:
        form_pesquisa = PesquisaForm()
        context = {
            'curso': cursoQuery[0],
            'form_pesquisa' : form_pesquisa,
        }
        template = loader.get_template('pesquisa/avaliar.html')
    else:
        context = {}
        template = loader.get_template('pesquisa/nenhum.html')
    return HttpResponse(template.render(context, request))

def registrarAvaliacao(request):
    # import ipdb; ipdb.set_trace()
    # usar request.POST
    form_pesquisa = PesquisaForm(request.POST)
    if form_pesquisa.is_valid():
        p = pesquisa()
        p.curso_id = request.POST.get("codigo_curso", "")
        p.questao1 = request.POST.get("questao1", "")
        p.questao2 = request.POST.get("questao3", "")
        p.questao3 = request.POST.get("questao3", "")
        p.questao4 = request.POST.get("questao4", "")
        p.questao5 = request.POST.get("questao5", "")
        p.questao6 = request.POST.get("questao6", "")
        p.questao7 = request.POST.get("questao7", "")
        p.questao8 = request.POST.get("questao8", "")
        p.comentario  = request.POST.get("mensagem", "")
        p.save()
        template = loader.get_template('pesquisa/obrigado.html')
    else:
        template = loader.get_template('pesquisa/erroCadastrarAvaliacao.html')
    context = {}
    return HttpResponse(template.render(context, request))

def cursosAvaliados(request):
    if request.method == "GET":
        cursoQuery = curso.objects.all()
        context = {
            'cursos': cursoQuery,
        }
        template = loader.get_template('resultados/index.html')
    else: # via POST
        id_curso_procurado = request.POST.get("CursoAvaliadoAnteriormente", "")
        cursoQuery = curso.objects.filter(id=id_curso_procurado)
        #import ipdb; ipdb.set_trace()
        if cursoQuery.count() == 0 :
            context = {}
            template = loader.get_template('resultados/nenhum.html')
        else:
            cursoAvaliado = cursoQuery.first()
            pesquisaQuery = pesquisa.objects.filter(curso_id=id_curso_procurado)
            if pesquisaQuery.count() > 0 :
                total = 0
                questao1 = 0
                questao2 = 0
                questao3 = 0
                questao4 = 0
                questao5 = 0
                questao6 = 0
                questao7 = 0
                questao8 = 0
                for pesq in pesquisaQuery.all():
                    questao1 += int(pesq.questao1)
                    questao2 += int(pesq.questao2)
                    questao3 += int(pesq.questao3)
                    questao4 += int(pesq.questao4)
                    questao5 += int(pesq.questao5)
                    questao6 += int(pesq.questao6)
                    questao7 += int(pesq.questao7)
                    questao8 += int(pesq.questao8)
                    total = total + 4
                porcentagemAceitacao = []
                porcentagemAceitacao.append(round((100 * questao1)/total))
                porcentagemAceitacao.append(round((100 * questao2)/total))
                porcentagemAceitacao.append(round((100 * questao3)/total))
                porcentagemAceitacao.append(round((100 * questao4)/total))
                porcentagemAceitacao.append(round((100 * questao5)/total))
                porcentagemAceitacao.append(round((100 * questao6)/total))
                porcentagemAceitacao.append(round((100 * questao7)/total))
                porcentagemAceitacao.append(round((100 * questao8)/(total/4)))
                form_pesquisa = PesquisaForm()
                context = {
                    # 'notas': porcentagemAceitacao,
                    'questao1': porcentagemAceitacao[0],
                    'questao2': porcentagemAceitacao[1],
                    'questao3': porcentagemAceitacao[2],
                    'questao4': porcentagemAceitacao[3],
                    'questao5': porcentagemAceitacao[4],
                    'questao6': porcentagemAceitacao[5],
                    'questao7': porcentagemAceitacao[6],
                    'questao8': porcentagemAceitacao[7],
                    'curso': cursoAvaliado,
                    'form_pesquisa' : form_pesquisa,
                }
            else:
                #Nenhuma avaliação feita no curso selecionado
                context = {
                    'curso': cursoAvaliado,
                }
            template = loader.get_template('resultados/resultados.html')

    return HttpResponse(template.render(context, request))



@login_required
def cadastrarCurso(request):
    if request.method == "GET":
        c = curso()
        template = loader.get_template('pesquisa/cadastrarCurso.html')
        form_curso = CursoForm()
        context = {
            'form_curso' : form_curso,
            }
    else:
        try:
            c = curso()
            if request.POST.get("nome", "") == "":
                raise ValueError('Nome do Curso não pode ser vazio')
            else:
                c.nome = request.POST.get("nome", "")
            c.setDataInicio(request.POST.get("dataInicio", ""))
            c.setDataFim(request.POST.get("dataFim", ""))
            if request.POST.get("professor", "") == "":
                raise ValueError('Nome do Instrutor não pode ser vazio')
            else:
                c.professor = request.POST.get("professor", "")
            c.codigo =  c.gerarChave()
            c.save()
            context = {
                'voucher' : c.codigo,
            }
            template = loader.get_template('pesquisa/cadastrarCurso2.html')
        except:
            template = loader.get_template('pesquisa/cadastrarCurso.html')
            form_curso = CursoForm()
            context = {
                'form_curso' : form_curso,
                'erro_encontrado' : str('Orlando Saraiva Júnior'),
                }

    return HttpResponse(template.render(context, request))
