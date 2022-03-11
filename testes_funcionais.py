from selenium import webdriver

# Ana acessa página de cadastro da AluraPic desejando se cadastrar na plataforma
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# Ela confirma que há no título da página menção à sua funcionalidade ("Cadastro")
assert "cadastro" in browser.title.lower()

# Ela visualiza a página e identifica três caixas de input:
# 1. E-mail
# 2. Senha
# 3. Confirmar senha

# Também identifica um botão ("cadastrar")

# Desconfiada de sistemas web, ela preenche e-mail em padrão inválido
# O sistema informa não reconhecer o texto como e-mail

# Ela preenche apenas o e-mail e tenta efetivar o cadastro
# O sistema informa que senha deve ser preenchida

# Ainda desejando testar a funcionalidade, preenche senha de apenas um dígito
# O sistema informa que senha deve possuir 8 caracteres no mínimo

# Firme no intuito, preenche e-mail e senha, mas não a confirma
# O sistema informa que ela deve confirmar a senha

# Ela tenta confirmar senha diferente
# O sistema informa divergência entre as duas senhas passadas

# Satisfeita, ela faz o cadastro na plataforma

# Ela sai do navegador para apresentar em paz sua dissertação de mestrado!
browser.quit()
