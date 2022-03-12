import time
from collections import namedtuple
from django.test import tag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from typing import List
import unittest


DadosEntrada = namedtuple('DadosEntrada', 'valor atributo_html valor_atributo_html id_html')


class CadastroDeNovoUsuarioTest(unittest.TestCase):
    def setUp(self) -> None:
        self._url_cadastro: str = 'http://localhost:8000/cadastro'
        self.browser = webdriver.Firefox()
        self.id_submissao_dados: str = 'confirmar_cadastro'
        self.dados_email_padrao: DadosEntrada = DadosEntrada(valor='fulana@meuemail.com',
                                                             atributo_html='placeholder',
                                                             valor_atributo_html='E-mail',
                                                             id_html='email')
        self.dados_senha_padrao: DadosEntrada = DadosEntrada(valor='123abcABC',
                                                             atributo_html='placeholder',
                                                             valor_atributo_html='Senha',
                                                             id_html='senha')
        self.dados_confirmacao_senha_padrao: DadosEntrada = DadosEntrada(valor='123abcABC',
                                                                         atributo_html='placeholder',
                                                                         valor_atributo_html='Confirmar senha',
                                                                         id_html='confirmar_senha')
        self.dados_entrada: List[DadosEntrada] = [self.dados_email_padrao,
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
        input_email = self.browser.find_element_by_id(self.dados_email_padrao.id_html)
        self.assertIsNotNone(input_email)
        input_senha = self.browser.find_element_by_id(self.dados_senha_padrao.id_html)
        self.assertIsNotNone(input_senha)
        input_confirmar_senha = self.browser.find_element_by_id(self.dados_confirmacao_senha_padrao.id_html)
        self.assertIsNotNone(input_confirmar_senha)

        # Satisfeita, ela decide inputar seus dados para fazer o cadastro na plataforma
        for dado in self.dados_entrada:
            inputbox = self.browser.find_element_by_id(dado.id_html)
            inputbox.send_keys(dado.valor)
            self.assertEqual(
                inputbox.get_attribute(dado.atributo_html),
                dado.valor_atributo_html
            )

        # Após inserir os dados, ela confirma o cadastro
        inputbox = self.browser.find_element_by_id(self.id_submissao_dados)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # Após confirmação, ela é redirecionada para página de login
        self.assertIn("login", self.browser.title.lower())
        self.assertIn("login", self.browser.current_url)
        # Ela sai do navegador para apresentar em paz sua dissertação de mestrado!

    # @unittest.skip('later')
    @tag('teste_funcional')
    def test_nao_deve_redirecionar_para_pagina_de_login_se_pelo_menos_um_campo_estiver_vazio(self):
        self._helper_cenario_nao_preenchimento_de_campo(self.dados_senha_padrao.id_html)
        self._helper_cenario_nao_preenchimento_de_campo(self.dados_confirmacao_senha_padrao.id_html)
        self._helper_cenario_nao_preenchimento_de_campo(self.dados_email_padrao.id_html)

    def _helper_cenario_nao_preenchimento_de_campo(self, id_campo_vazio: str):
        # Fulana acessa página de cadastro da AluraPic desejando testar se pode se cadastrar
        # sem preencher um de seus campos
        self.browser.get(self._url_cadastro)

        # Ela preenche os demais campos que não o campo em teste a ficar vazio
        for dado in self.dados_entrada:
            if dado.id_html != id_campo_vazio:
                inputbox = self.browser.find_element_by_id(dado.id_html)
                inputbox.send_keys(dado.valor)

        # Após inserir os dados, ela tenta confirmar o cadastro
        inputbox = self.browser.find_element_by_id(self.id_submissao_dados)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # E verifica que continuou na página
        self.assertIn("cadastro", self.browser.title.lower())


if __name__ == '__main__':
    unittest.main()
