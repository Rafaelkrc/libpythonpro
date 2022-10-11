import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['rafaelkrc@hotmail.com', 'gestaocasacoelho@gmail.com']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'rafaelkrc@gmail.com',
        'Curso Pytools',
        'Teste de enviador de email para testes TDD e Baby test.'
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'rafael']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'rafaelkrc@gmail.com',
            'Curso Pytools',
            'Teste de enviador de email para testes TDD e Baby test.'
        )
