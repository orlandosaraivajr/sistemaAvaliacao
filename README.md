# Avaliação de treinamentos presenciais


### Sistema para avaliação de treinamentos presenciais

Este sistema permite criar e avaliar cursos/treinamento presenciais.

	$ git clone https://github.com/orlandosaraivajr/sistemaAvaliacao.git
	$ cd sistemaAvaliacao .
	$ virtualenv -p python3 .
	$ source bin/activate
	$ pip install -r requirements.txt
	$ cd avaliacao
	$ chmod +x manage.py
	$ ./manage.py migrate
	$ ./manage.py createsuperuser
	$ ./manage.py test
	$ ./manage.py runserver




