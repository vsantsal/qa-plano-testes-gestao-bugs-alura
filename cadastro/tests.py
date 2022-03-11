from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from cadastro.views import pagina_cadastro


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_cai_na_view_pagina_cadastro(self):
        encontrou = resolve('/')
        self.assertEqual(encontrou.func, pagina_cadastro)

    def test_pagina_cadastro_retorna_html_esperado(self):
        request = HttpRequest()
        resposta = pagina_cadastro(request)
        html_pagina_cadastro: str = resposta.content.decode('utf8')
        self.assertTrue(html_pagina_cadastro.startswith('<html>'))
        self.assertIn('<title>Cadastro</title>', html_pagina_cadastro)
        self.assertTrue(html_pagina_cadastro.endswith('</html>'))
