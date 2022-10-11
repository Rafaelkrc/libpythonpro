import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['rafaelkrc@hotmail.com', 'gestaocasacoelho@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'rafaelkrc@gmail.com',
        'Curso Pytools',
        'Teste de enviador de email para testes TDD e Baby test.'
    )
    assert destinatario in resultado
