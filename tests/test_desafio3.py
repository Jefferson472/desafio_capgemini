import pytest
from desafio3 import AnalisaAnagramas


def test_retorna_2_string_ovo():
    entrada = 'ovo'
    a = AnalisaAnagramas(entrada)
    output = a.verifica_anagrama()
    assert output == 2


def test_retorna_3_string_ifailuhkqq():
    entrada = 'ifailuhkqq'
    a = AnalisaAnagramas(entrada)
    output = a.verifica_anagrama()
    assert output == 3
