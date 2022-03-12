from django import forms
from django.core import validators


class CadastroUsuarioForm(forms.Form):
    email = forms.CharField(label="",
                            max_length=100,
                            validators=[validators.validate_email],
                            widget=forms.TextInput(attrs={'placeholder': 'E-mail',
                                                          'id': 'email'}))
    senha = forms.CharField(label="",
                            max_length=100,
                            min_length=8,
                            widget=forms.PasswordInput(attrs={'placeholder': 'Senha',
                                                              'id': 'senha'}))

    confirmar_senha = forms.CharField(label="",
                                      max_length=100,
                                      min_length=8,
                                      widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar senha',
                                                                        'id': 'confirmar_senha'}))

    def clean(self):
        self._cleaned_data = super(CadastroUsuarioForm, self).clean()

        if self._senhas_sao_incompatives():
            self._errors['confirmar_senha'] = self.error_class(['Passwords do not match.'])

        del self.cleaned_data
        return None

    def _senhas_sao_incompatives(self):
        senha1 = self._cleaned_data.get('senha')
        senha2 = self._cleaned_data.get('confirmar_senha')
        return senha1 and senha2 and senha1 != senha2

    def _email_eh_invalido(self):
        return 'email' not in self._cleaned_data.keys()
