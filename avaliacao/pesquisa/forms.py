from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.admin import widgets


from .models import curso, pesquisa

class PesquisaForm(forms.Form):
#    questao1 = forms.MultipleChoiceField(
    questao1 = forms.ChoiceField(
        label=_('1. O instrutor apresentou adequadamente seu plano de trabalho.'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao2 = forms.ChoiceField(
        label=_('2. O professor demonstrou possuir conhecimento técnico e segurança na abordagem dos conteúdos.'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao3 = forms.ChoiceField(
        label=_('3. O professor foi pontual no cumprimento dos horários de início e término.'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao4 = forms.ChoiceField(
        label=_('4. O professor mostrou-­se motivado na condução do curso.'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao5 = forms.ChoiceField(
        label=_('5. O professor desenvolveu o conteúdo de maneira clara, de modo a facilitar a compreensão.'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao6 = forms.ChoiceField(
        label=_('6. O professor utilizou­-se adequadamente de outras estratégias de ensino, além da aula expositiva (como, por exemplo: código-fonte, dinâmicas, estudos de casos, etc).'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao7 = forms.ChoiceField(
        label=_('7. O professor relacionou os conteúdos teóricos com a aplicação prática.'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.OPCOES,
    )
    questao8 = forms.ChoiceField(
        label=_('8. Se você pudesse optar, cursaria outro treinamento com esse professor ?'),
        required=True, widget=forms.RadioSelect(), choices=pesquisa.SIM_NAO,
    )
    mensagem = forms.CharField(
        label=_('Deixe sua crítica, elogio ou comentário sobre o curso'),
        widget=forms.Textarea, max_length=200,required=False
    )


class CursoForm(ModelForm):
    nome = forms.CharField(
        max_length=200,
        required=True,
        help_text='Use puns liberally',
    )
    class Meta:
        model = curso
        exclude = ['id']

        widgets = {
#            'nome': forms.Textarea(attrs={'cols': 100, 'rows': 1}),
#            'dataInicio':  forms.Textarea(attrs={'cols': 20,'rows': 1,'maxlength': 10,'pattern': '[0-9]{2}\/[0-9]{2}\/[0-9]{4}$',}                ),
#            'dataInicio':  widgets.AdminSplitDateTime(),
            'dataInicio' : forms.DateInput(attrs={
                'id':'dataInicio',
                'pattern': '[0-9]{2}\/[0-9]{2}\/[0-9]{4}$'
                }),
            'dataFim': forms.DateInput(attrs={
                'id':'dataFim',
                'pattern': '[0-9]{2}\/[0-9]{2}\/[0-9]{4}$'
                }),
        }

        labels = {
            "nome": _("Curso"),
            "dataInicio": _("Data de Início"),
            "dataFim": _("Data de Término"),
            "professor": _("Instrutor"),
            "codigo": _("Voucher do curso"),
        }
