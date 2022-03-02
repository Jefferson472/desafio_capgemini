import pytest
from desafio2 import AnalisaSenha


senha_valida = AnalisaSenha('Abc123!')


def test_senha_qntd_caract_maior_6():
    assert senha_valida.verifica_qntd_caracteres() is True


def test_verifica_min_digito():
    assert senha_valida.verifica_min_digito() is True


def test_verifica_letra_minuscula():
    assert senha_valida.verifica_letra_minuscula() is True


def test_verifica_letra_maiuscula():
    assert senha_valida.verifica_letra_maiuscula() is True


def test_verifica_caract_especial():
    assert senha_valida.verifica_caract_especial() is True
