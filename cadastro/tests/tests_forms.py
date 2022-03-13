from collections import namedtuple
from django.test import (
    TestCase,
)
from typing import Dict

from cadastro.forms import CadastroUsuarioForm


class CadastroUsuarioFormTest(TestCase):
    def setUp(self) -> None:
        self.cadastro_correto: Dict[str, str] = {
            'email': 'fulana@meuemail.com',
            'senha': '123abcAB',
            'confirmar_senha': '123abcAB',

        }

    def test_deve_ser_valido_para_dados_validos(self):
        formulario = CadastroUsuarioForm(self.cadastro_correto)
        self.assertTrue(formulario.is_valid())

    def test_deve_ser_invalido_para_pelo_menos_um_campo_vazio(self):
        for campo in self.cadastro_correto.keys():
            valor_original = self.cadastro_correto[campo]
            self.cadastro_correto[campo] = ''
            formulario = CadastroUsuarioForm(self.cadastro_correto)
            self.assertFalse(formulario.is_valid())
            self.assertEqual(formulario.errors[campo][0],
                             'Este campo é obrigatório.')
            self.cadastro_correto[campo] = valor_original

    def test_deve_ser_invalido_para_senha_com_menos_de_8_caracteres(self):
        self.cadastro_correto['senha'] = self.cadastro_correto.get('senha')[:-1]
        self.cadastro_correto['confirmar_senha'] =self.cadastro_correto['senha']
        formulario = CadastroUsuarioForm(self.cadastro_correto)
        self.assertFalse(formulario.is_valid())
        self.assertEqual(formulario.errors['confirmar_senha'][0],
                         'Certifique-se de que o valor tenha no mínimo 8 caracteres (ele possui 7).')

    def test_deve_ser_invalido_se_senha_e_confirmacao_sao_diferentes(self):
        self.cadastro_correto['confirmar_senha'] = '987654321'
        formulario = CadastroUsuarioForm(self.cadastro_correto)
        self.assertFalse(formulario.is_valid())
        self.assertEqual(formulario.errors['confirmar_senha'][0],
                         'Senhas divergentes.')

    def test_deve_ser_invalido_se_email_nao_eh_valido(self):
        for remetente in ('fulana', 'fulanameuemail.com', 'fulana@meuemail'):
            self.cadastro_correto['email'] = remetente
            formulario = CadastroUsuarioForm(self.cadastro_correto)
            self.assertFalse(formulario.is_valid())
            self.assertEqual(formulario.errors['email'][0],
                             'Informe um endereço de email válido.')
