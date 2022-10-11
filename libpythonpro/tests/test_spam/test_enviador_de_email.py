from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'rafaelkrc@hotmail.com',
        'rafaelkrc@gmail.com',
        'Curso Pytools',
        'Teste de enviador de email para testes TDD e Baby test.'
    )
    assert 'rafaelkrc@hotmail.com' in resultado
