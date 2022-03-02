import pytest
from desafio1 import CriaEscada

e = CriaEscada()

def test_desenha_escada_um_degrau():
    entrada = 1
    saida_esperada = '*\n'
    assert e.desenha_escada(entrada) == saida_esperada


def test_desenha_escada_dois_degraus():
    entrada = 2
    saida_esperada = ' *\n**\n'
    assert e.desenha_escada(entrada) == saida_esperada


def test_desenha_escada_tres_degraus():
    entrada = 3
    saida_esperada = '  *\n **\n***\n'
    assert e.desenha_escada(entrada) == saida_esperada
