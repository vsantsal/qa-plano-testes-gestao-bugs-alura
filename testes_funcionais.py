import time
from django.test import tag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from typing import Dict, List
import unittest


class CadastroDeNovoUsuarioTest(unittest.TestCase):
    def setUp(self) -> None:
        self._url_cadastro: str = 'http://localhost:8000/cadastro'
        self.browser = webdriver.Firefox()
        self.id_submissao_dados: str = 'confirmar_cadastro'
        self.dados_email_padrao: Dict[str, str] = {
            'valor': 'fulana@meuemail.com',
            'atributo_html': 'placeholder',
            'valor_atributo_html': 'E-mail',
            'id_html': 'email',

        }
        self.dados_senha_padrao: Dict[str, str] = {
            'valor': '123abcABC',
            'atributo_html': 'placeholder',
            'valor_atributo_html': 'Senha',
            'id_html': 'senha',
        }
        self.dados_confirmacao_senha_padrao: Dict[str, str] = {
            'valor': '123abcABC',
            'atributo_html': 'placeholder',
            'valor_atributo_html': 'Confirmar senha',
            'id_html': 'confirmar_senha',
        }
        self.dados_entrada: List[Dict[str, str]] = [self.dados_email_padrao,
                                                    self.dados_senha_padrao,
                                                    self.dados_confirmacao_senha_padrao]

    def tearDown(self) -> None:
        self.browser.quit()

    @tag('teste_funcional')
    def test_deve_cadastrar_novo_usuario_com_preenchimento_correto(self):
        # Fulana acessa página de cadastro da AluraPic desejando se cadastrar na plataforma
        self.browser.get(self._url_cadastro)
        # Ela confirma que há no título e no cabeçalho da página menção à sua funcionalidade ("Cadastro")
        self.assertIn("cadastro", self.browser.title.lower())
        texto_cabecalho: str = self.browser.find_element_by_tag_name('h1').text.lower()
        self.assertIn('cadastro', texto_cabecalho)

        # Ela visualiza a página e identifica três caixas de input:
        # 1. E-mail
        # 2. Senha
        # 3. Confirmar senha
        input_email = self.browser.find_element_by_id(self.dados_email_padrao['id_html'])
        self.assertIsNotNone(input_email)
        input_senha = self.browser.find_element_by_id(self.dados_senha_padrao['id_html'])
        self.assertIsNotNone(input_senha)
        input_confirmar_senha = self.browser.find_element_by_id(self.dados_confirmacao_senha_padrao['id_html'])
        self.assertIsNotNone(input_confirmar_senha)

        # Satisfeita, ela decide inputar seus dados para fazer o cadastro na plataforma
        for dado in self.dados_entrada:
            inputbox = self.browser.find_element_by_id(dado['id_html'])
            inputbox.send_keys(dado['valor'])
            self.assertEqual(
                inputbox.get_attribute(dado['atributo_html']),
                dado['valor_atributo_html']
            )

        # Após inserir os dados, ela confirma o cadastro
        inputbox = self.browser.find_element_by_id(self.id_submissao_dados)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Após confirmação, ela é redirecionada para página de login
        self.assertIn("login", self.browser.title.lower())
        self.assertIn("login", self.browser.current_url)
        # Ela sai do navegador para apresentar em paz sua dissertação de mestrado!

    @tag('teste_funcional')
    def test_nao_deve_redirecionar_para_pagina_de_login_se_pelo_menos_um_campo_estiver_vazio(self):
        self.browser.get(self._url_cadastro)
        self._helper_cenario_com_preenchimento_invalido_de_campo_customizado(
            self.dados_senha_padrao['id_html'])
        self._helper_cenario_com_preenchimento_invalido_de_campo_customizado(
            self.dados_confirmacao_senha_padrao['id_html'])
        self._helper_cenario_com_preenchimento_invalido_de_campo_customizado(
            self.dados_email_padrao['id_html'])

    @tag('teste_funcional')
    def test_nao_deve_redirecionar_para_pagina_de_login_se_padrao_email_invalido(self):
        self.browser.get(self._url_cadastro)
        emails_invalidos = ('fulanameuemail.com',
                            'fulana@meuemail',
                            'fulana',
                            'fulana@fulana@meuemail.com')

        for valor in emails_invalidos:
            self._helper_cenario_com_preenchimento_invalido_de_campo_customizado(
                self.dados_email_padrao['id_html'],
                valor
            )

    @unittest.skip('Sob investigação - unclosed sockets')
    @tag('teste_funcional')
    def test_nao_deve_redirecionar_para_pagina_de_login_se_senha_e_confirmacao_diferentes(self):
        self.dados_confirmacao_senha_padrao['valor'] = '456abcABC'
        self._helper_cenario_com_preenchimento_invalido_de_campo_customizado(
            self.dados_senha_padrao['id_html'],
            self.dados_senha_padrao['valor']
        )

    @unittest.skip('Sob investigação - unclosed sockets')
    @tag('teste_funcional')
    def test_nao_deve_redirecionar_para_pagina_de_login_se_senha_invalida(self):
        senhas_invalidas = ('1234567',
                            '123abc')

        for valor in senhas_invalidas:
            self.dados_confirmacao_senha_padrao['valor'] = valor
            self._helper_cenario_com_preenchimento_invalido_de_campo_customizado(
                self.dados_senha_padrao['id_html'],
                valor
            )

    def _helper_cenario_com_preenchimento_invalido_de_campo_customizado(self,
                                                                        id_campo_customizado: str,
                                                                        valor_campo_customizado: str = ''):

        # Fulana acessa página de cadastro da AluraPic desejando testar preenchimentos
        # inválidos
        self.browser.get(self._url_cadastro)

        for dado in self.dados_entrada:
            if dado['id_html'] == id_campo_customizado and valor_campo_customizado == '':
                continue
            inputbox = self.browser.find_element_by_id(dado['id_html'])
            if dado['id_html'] == id_campo_customizado:
                inputbox.send_keys(valor_campo_customizado)
            else:
                inputbox.send_keys(dado['valor'])

        # Após inserir os dados, ela tenta confirmar o cadastro
        inputbox = self.browser.find_element_by_id(self.id_submissao_dados)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # E verifica que continuou na página
        self.assertIn("cadastro", self.browser.title.lower())


if __name__ == '__main__':
    unittest.main()
