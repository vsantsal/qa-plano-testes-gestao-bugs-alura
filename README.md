# qa-plano-testes-gestao-bugs-alura

Repositório para acompanhar o curso "Quality Assurance" (https://cursos.alura.com.br/course/quality-assurance-plano-testes-gestao-bugs) da Alura, desenvolvendo e testando a funcionalidade Cadastro com o framework Django

## Roteiro

Desenvolveremos no presente repositório funcionalidades utilizadas como exemplos/exercícios no curso "Quality Assurance: plano de testes e gestão de bugs", utilizando o framework Django.

Como processo de desenvolvimento, nos basearemos no roteiro ilustrado nos capítulos iniciais do livro "TDD com Python", de Harry Percival (https://www.obeythetestinggoat.com/book).


### Funcionalidade Cadastro

A primeira funcionalidade a desenvolvermos será a de Cadastro, cuja implementação deverá obedecer às regras:

```
Funcionalidade: Cadastro

Comportamento esperado: Ao digitar e-mail, nome completo, usuário e senha e confirmar a senha, o usuário será cadastrado na plataforma.

Quando o cadastro for efetuado corretamente, o usuário deverá ser redirecionado para a tela de login. Em caso de erro, usuário deve receber uma mensagem informando qual é o erro.

Todos os campos são obrigatórios e o sistema deve indicar caso um campo não tenha sido digitado.

A senha deve ter no mínimo 8 caracteres.
```


## Anotações do desenvolvimento

### Testes 

### Unitários

O script `testes_funcionais.py` possui classes responsáveis por execução de testes funcionais do sistema.

Para não impactarem os testes unitários que usualmente desejamos executar ao rodar o comando `python manage.py test`, 
recomenda-se marcá-los com flags, de nome "testes_funcionais" (para ler mais sobre a anotação do Django, ler https://docs.djangoproject.com/en/4.0/topics/testing/tools/#tagging-tests).

Assim, recomenda-se rodar os testes unitários com o comando `python manage.py test --exclude-tag=teste_funcional`.

#### Funcionais

Rodar o script `testes_funcionais.py` com o comando `python testes_funcionais.py`.

### Formulários

Dado que a funcionalidade cadastro demandava conhecimento formulários HTML, sentiu-se necessidade de estudar a documentação do Django sobre como trabalhar com eles (https://docs.djangoproject.com/en/4.0/topics/forms/).

Para utilizar *placeholders* nos forms em vez *label*, consultamos a documentação de widgets (https://docs.djangoproject.com/en/4.0/ref/forms/widgets/).

Para realização das validações expressas nas regras de negócios, consultamos a documentação de *Forms and field validation* (https://docs.djangoproject.com/en/4.0/ref/forms/validation/).

Como estudo complementar, assistir ao curso da Alura "Formulários no Django 3: criando e validando dados" (https://cursos.alura.com.br/course/django-validando-formularios).