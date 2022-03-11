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


