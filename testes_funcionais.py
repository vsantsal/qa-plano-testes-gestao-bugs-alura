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
        self.browser = webdriver.Firefox()
        self.dados_email_padrao: DadosEntrada = DadosEntrada(valor='fulana@meuemail.com',
                                                             atributo_html='placeholder',
                                                             valor_atributo_html='E-mail',
                                                             id_html='id_email')
        self.dados_senha_padrao: DadosEntrada = DadosEntrada(valor='123abcABC',
                                                             atributo_html='placeholder',
                                                             valor_atributo_html='Senha',
                                                             id_html='id_senha')
        self.dados_confirmacao_senha_padrao: DadosEntrada = DadosEntrada(valor='123abcABC',
                                                                         atributo_html='placeholder',
                                                                         valor_atributo_html='Confirmar senha',
                                                                         id_html='id_confirmar_senha')
        self.dados_entrada: List[DadosEntrada] = [self.dados_email_padrao,
                                                  self.dados_senha_padrao,
                                                  self.dados_confirmacao_senha_padrao]

    def tearDown(self) -> None:
        self.browser.quit()

    @tag('teste_funcional')
    def test_deve_cadastrar_novo_usuario_com_preenchimento_correto(self):
        # Fulana acessa página de cadastro da AluraPic desejando se cadastrar na plataforma
        self.browser.get('http://localhost:8000')
        # Ela confirma que há no título e no cabeçalho da página menção à sua funcionalidade ("Cadastro")
        self.assertIn("cadastro", self.browser.title.lower())
        texto_cabecalho: str = self.browser.find_element_by_tag_name('h1').text.lower()
        self.assertIn('cadastro', texto_cabecalho)

        # Ela visualiza a página e identifica três caixas de input:
        # 1. E-mail
        # 2. Senha
        # 3. Confirmar senha
        input_email = self.browser.find_element_by_id('id_email')
        self.assertIsNotNone(input_email)
        input_senha = self.browser.find_element_by_id('id_senha')
        self.assertIsNotNone(input_senha)
        input_confirmar_senha = self.browser.find_element_by_id('id_confirmar_senha')
        self.assertIsNotNone(input_confirmar_senha)

        # Satisfeita, ela decide inputar seus dados para fazer o cadastro na plataforma
        for dado in self.dados_entrada:
            inputbox = self.browser.find_element_by_id(dado.id_html)
            self.assertEqual(
                inputbox.get_attribute(dado.atributo_html),
                dado.valor_atributo_html
            )

        # Após inserir os dados, ela confirma o cadastro
        inputbox = self.browser.find_element_by_id('id_confirmar')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Após confirmação, ela é redirecionada para página de login
        self.assertIn("login", self.browser.title.lower())

        # Ela sai do navegador para apresentar em paz sua dissertação de mestrado!


if __name__ == '__main__':
    unittest.main()
